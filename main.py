from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import duckdb
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
ARCHIVE_DIR = DATA_DIR / "archive"

RAW_ARXIV_PATH = RAW_DIR / "arxiv-metadata-oai-snapshot.json"
RAW_GRANT_PATH = RAW_DIR / "grant.gov.xml"
LEGACY_ARXIV_DB_PATH = ARCHIVE_DIR / "arxiv.duckdb"
PROCESSED_DB_PATH = PROCESSED_DIR / "srmatcher.duckdb"

GRANT_NAMESPACE = {"g": "http://apply.grants.gov/system/OpportunityDetail-V1.0"}
GRANT_DATE_COLUMNS = ["PostDate", "CloseDate", "LastUpdatedDate", "ArchiveDate"]
GRANT_START = pd.Timestamp("2004-01-01")
GRANT_END = pd.Timestamp("2026-12-31")
ARXIV_START = "1995-01-01"


def clean_text(value: object) -> str | None:
    if pd.isna(value):
        return None
    text = html.unescape(str(value))
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*\n\s*", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip() or None


def parse_grant_date(series: pd.Series) -> pd.Series:
    cleaned = (
        series.astype("string")
        .str.replace(r"\.0+$", "", regex=True)
        .str.replace(r"\D", "", regex=True)
        .str.zfill(8)
    )
    parsed = pd.to_datetime(cleaned, format="%m%d%Y", errors="coerce")
    return parsed.where(parsed.dt.year.between(2000, 2100))


def join_text_columns(frame: pd.DataFrame, columns: list[str]) -> pd.Series:
    combined = frame[columns].fillna("").agg(" ".join, axis=1)
    combined = combined.str.replace(r"\s+", " ", regex=True).str.strip()
    return combined.where(combined.ne(""), None)


def ensure_data_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)


def load_and_clean_grants(xml_path: Path) -> pd.DataFrame:
    if not xml_path.exists():
        raise FileNotFoundError(f"Grant XML file not found: {xml_path}")

    grants = pd.read_xml(
        xml_path,
        xpath=".//g:OpportunitySynopsisDetail_1_0",
        namespaces=GRANT_NAMESPACE,
        parser="lxml",
    )

    for column in GRANT_DATE_COLUMNS:
        if column in grants.columns:
            grants[f"{column}_parsed"] = parse_grant_date(grants[column])

    grants = grants.assign(
        OpportunityID=grants["OpportunityID"].astype("Int64").astype("string"),
        Description_clean=grants["Description"].map(clean_text),
        Eligibility_clean=grants["AdditionalInformationOnEligibility"].map(clean_text),
        GrantorContact_clean=grants["GrantorContactText"].map(clean_text),
    )

    grants["demand_text"] = join_text_columns(
        grants,
        [
            "OpportunityTitle",
            "Description_clean",
            "CategoryExplanation",
            "CategoryOfFundingActivity",
            "AgencyName",
        ],
    )

    grants = grants.sort_values(
        by=["OpportunityID", "LastUpdatedDate_parsed", "PostDate_parsed"],
        na_position="last",
    ).drop_duplicates(subset=["OpportunityID"], keep="last")

    grants = grants.loc[
        grants["OpportunityID"].notna()
        & grants["Description_clean"].notna()
        & grants["PostDate_parsed"].between(GRANT_START, GRANT_END)
    ].copy()

    grants["grant_year"] = grants["PostDate_parsed"].dt.year

    grants = grants.rename(
        columns={
            "OpportunityID": "opportunity_id",
            "OpportunityTitle": "opportunity_title",
            "OpportunityNumber": "opportunity_number",
            "OpportunityCategory": "opportunity_category",
            "FundingInstrumentType": "funding_instrument_type",
            "CategoryOfFundingActivity": "category_of_funding_activity",
            "CategoryExplanation": "category_explanation",
            "CFDANumbers": "cfda_numbers",
            "EligibleApplicants": "eligible_applicants",
            "AgencyCode": "agency_code",
            "AgencyName": "agency_name",
            "Description_clean": "description",
            "Eligibility_clean": "eligibility",
            "GrantorContact_clean": "grantor_contact",
            "PostDate_parsed": "posted_date",
            "CloseDate_parsed": "close_date",
            "LastUpdatedDate_parsed": "last_updated_date",
            "ArchiveDate_parsed": "archive_date",
        }
    )

    return grants[
        [
            "opportunity_id",
            "opportunity_title",
            "opportunity_number",
            "opportunity_category",
            "funding_instrument_type",
            "category_of_funding_activity",
            "category_explanation",
            "cfda_numbers",
            "eligible_applicants",
            "agency_code",
            "agency_name",
            "description",
            "eligibility",
            "grantor_contact",
            "posted_date",
            "close_date",
            "last_updated_date",
            "archive_date",
            "grant_year",
            "demand_text",
        ]
    ].reset_index(drop=True)


def build_arxiv_table(con: duckdb.DuckDBPyConnection, json_path: Path, replace: bool) -> None:
    if not json_path.exists():
        raise FileNotFoundError(f"arXiv JSON file not found: {json_path}")

    if not replace:
        exists = con.execute(
            "SELECT 1 FROM information_schema.tables WHERE table_name = 'arxiv_clean'"
        ).fetchone()
        if exists is not None:
            return

    con.execute(
        """
        CREATE OR REPLACE TABLE arxiv_clean AS
        WITH source AS (
            SELECT
                id AS arxiv_id,
                trim(regexp_replace(coalesce(title, ''), '\\s+', ' ', 'g')) AS title,
                trim(regexp_replace(coalesce(abstract, ''), '\\s+', ' ', 'g')) AS abstract,
                trim(coalesce(categories, '')) AS categories,
                coalesce(doi, '') AS doi,
                coalesce("journal-ref", '') AS journal_ref,
                coalesce("report-no", '') AS report_no,
                CAST(try_strptime(versions[1].created, '%a, %d %b %Y %H:%M:%S GMT') AS DATE) AS submitted_date,
                CAST(update_date AS DATE) AS updated_date,
                array_length(versions) AS version_count
            FROM read_json_auto(?, format = 'newline_delimited')
        )
        SELECT
            arxiv_id,
            title,
            abstract,
            categories,
            doi,
            journal_ref,
            report_no,
            submitted_date,
            year(submitted_date) AS submitted_year,
            updated_date,
            year(updated_date) AS updated_year,
            version_count,
            trim(regexp_replace(title || ' ' || abstract || ' ' || categories, '\\s+', ' ', 'g')) AS paper_text
        FROM source
        WHERE submitted_date >= CAST(? AS DATE)
          AND nullif(title, '') IS NOT NULL
          AND nullif(abstract, '') IS NOT NULL
        """,
        [str(json_path), ARXIV_START],
    )


def write_grant_table(
    con: duckdb.DuckDBPyConnection,
    grants: pd.DataFrame,
    replace: bool,
) -> None:
    if not replace:
        exists = con.execute(
            "SELECT 1 FROM information_schema.tables WHERE table_name = 'grant_clean'"
        ).fetchone()
        if exists is not None:
            return

    con.register("grant_clean_df", grants)
    con.execute("CREATE OR REPLACE TABLE grant_clean AS SELECT * FROM grant_clean_df")
    con.unregister("grant_clean_df")


def build_summary_table(con: duckdb.DuckDBPyConnection) -> dict[str, object]:
    con.execute(
        """
        CREATE OR REPLACE TABLE dataset_summary AS
        SELECT 'grant_clean' AS dataset_name,
               COUNT(*) AS row_count,
               MIN(posted_date) AS min_date,
               MAX(posted_date) AS max_date
        FROM grant_clean
        UNION ALL
        SELECT 'arxiv_clean' AS dataset_name,
               COUNT(*) AS row_count,
               MIN(submitted_date) AS min_date,
               MAX(submitted_date) AS max_date
        FROM arxiv_clean
        """
    )

    summary_rows = con.execute(
        "SELECT dataset_name, row_count, min_date, max_date FROM dataset_summary ORDER BY dataset_name"
    ).fetchall()

    return {
        dataset_name: {
            "row_count": row_count,
            "min_date": min_date,
            "max_date": max_date,
        }
        for dataset_name, row_count, min_date, max_date in summary_rows
    }


def build_database(replace: bool = False) -> dict[str, object]:
    ensure_data_dirs()
    grants = load_and_clean_grants(RAW_GRANT_PATH)

    with duckdb.connect(str(PROCESSED_DB_PATH)) as con:
        write_grant_table(con, grants, replace=replace)
        build_arxiv_table(con, RAW_ARXIV_PATH, replace=replace)
        summary = build_summary_table(con)

    return {
        "database_path": str(PROCESSED_DB_PATH),
        "grant_clean": summary["grant_clean"],
        "arxiv_clean": summary["arxiv_clean"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build cleaned and time-aligned datasets for SRMatcher.",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Rebuild the cleaned DuckDB tables even if they already exist.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = build_database(replace=args.replace)
    print(f"Built cleaned database at {summary['database_path']}")
    print(
        "grant_clean:",
        summary["grant_clean"]["row_count"],
        summary["grant_clean"]["min_date"],
        summary["grant_clean"]["max_date"],
    )
    print(
        "arxiv_clean:",
        summary["arxiv_clean"]["row_count"],
        summary["arxiv_clean"]["min_date"],
        summary["arxiv_clean"]["max_date"],
    )


if __name__ == "__main__":
    main()
