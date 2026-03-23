# SRMatcher

SRMatcher is a graduation-paper project for building a complete pipeline for text-based academic supply and industry requirement matching, then using the best matching method to analyze topic adoption gaps across realms.

## Project Goals

1. Build a reliable baseline for supply and requirement text cleaning, alignment, and retrieval.
2. Improve supply-requirement matching beyond TF-IDF with stronger semantic and structured signals.
3. Analyze the time gap between academic topic emergence and industry-side appearance, then compare that lag across realms such as computer science and medicine.

## Branch Strategy

1. `baseline`: data exploration, descriptive analysis, data cleaning, and TF-IDF baseline establishment.
2. `match`: improved matching methods, including embedding-based and hierarchical multi-signal matching.
3. `analysis`: all step-3 work, including temporal-gap analysis, cross-realm comparison, and interpretation of differences in lag.

## Current Baseline State

- Raw datasets are present under `data/raw`.
- `main.py` builds cleaned `grant_clean` and `arxiv_clean` tables into `data/processed/srmatcher.duckdb`.
- `code.ipynb` now covers Phase-1 EDA, pilot-domain wrangling review, side-specific stopword-candidate diagnosis, and the raw-text domain-wise TF-IDF baseline.

## Current Data Snapshot

- `grant_clean`: 80,748 rows from 2004-03-22 to 2026-03-11.
- `arxiv_clean`: 2,954,910 rows from 1995-01-01 to 2026-03-05.

## Phase 1 EDA Snapshot

- Effective overlap window for analysis is now treated as `2005-2024`, leaving edge years as buffers.
- Grant `description` quality is strong after cleaning:
  - raw missing rate is only `0.02%`;
  - average non-empty description length is `197.86` words;
  - `16.98%` of non-empty descriptions are shorter than 50 words.
- arXiv `abstract` quality is also strong:
  - non-empty rate in `arxiv_clean` is `100%`;
  - average abstract length is `145.11` words;
  - `5.38%` of abstracts are shorter than 50 words.
- Critical-field availability is good for matching, but metadata coverage is asymmetric:
  - grant `cfda_numbers` has `0.99%` missing;
  - arXiv `doi` has `56.65%` missing and `journal_ref` has `68.79%` missing, so those fields are not suitable as primary matching signals.
- arXiv version history is highly concentrated near the first few revisions:
  - `version_count = 1` for `1,778,489` papers;
  - `version_count = 2` for `793,361` papers;
  - `version_count = 3` for `260,327` papers.
- Pilot domain wrangling tables have been materialized into DuckDB:
  - `grant_pilot_labeled`: `cs` 6,739, `biomed` 29,966, `env_energy` 35,510
  - `arxiv_pilot_labeled`: `cs` 726,273, `biomed` 125,208, `env_energy` 346,484
- Matching-readiness diagnostics make the retrieval setup more explicit:
  - within `2005-2024`, the overall `arXiv:grant` ratio is `29.56:1`;
  - by domain, the ratio is `4.18:1` in `biomed`, `9.76:1` in `env_energy`, and `107.77:1` in `cs`;
  - grant-side concentration is strong, with the top-5 agencies contributing `38.31%` of records and the top-10 agencies `48.54%`.
- Text-style EDA confirms that the two sides are related but not stylistically aligned:
  - grant descriptions are longer on average in the sample (`190.01` words vs `121.42`);
  - grant descriptions also contain more sentences on average (`9.5` vs `5.94`);
  - top-20 term overlap is extremely low, with only `data` shared across both sampled vocabularies.
- Domain-level comparison further shows that lexical difficulty is not uniform:
  - grant `cs` descriptions average `379.35` words, versus `166.01` for arXiv `cs` abstracts;
  - cross-side vocabulary-overlap Jaccard is `0.2931` in `cs`, `0.2733` in `biomed`, and `0.2225` in `env_energy`.

## Baseline Snapshot

- Side-specific stopword candidates are now diagnosed but not yet applied to retrieval:
  - grant-side candidates are dominated by institutional terms such as `program`, `research`, `funding`, `support`, and `announcement`;
  - arXiv-side candidates are dominated by paper-writing terms such as `model`, `results`, `using`, `based`, and `present`.
- The raw-text TF-IDF baseline has been materialized into DuckDB:
  - `tfidf_baseline_matches_raw`: `1,444,300` top-20 matches across the three pilot domains;
  - `tfidf_baseline_domain_summary_raw`;
  - `tfidf_baseline_runtime_raw`.
- Domain-wise baseline summary:
  - `biomed`: top-1 average similarity `0.1818`, top-1 temporal coherence `28.12%`, median top-1 lag `-1280.5` days;
  - `cs`: top-1 average similarity `0.2059`, top-1 temporal coherence `22.97%`, median top-1 lag `-1467.0` days;
  - `env_energy`: top-1 average similarity `0.1698`, top-1 temporal coherence `29.63%`, median top-1 lag `-1242.0` days.
- The current baseline is therefore usable as a retrieval starting point, but not yet suitable as direct evidence for temporal-lag interpretation because most top-1 matches still place arXiv later than grant posting dates.

## Immediate Execution Path

1. Use `tfidf_baseline_matches_raw` to perform error analysis on high-scoring pairs, especially the large share of temporally inverted top-1 matches.
2. Convert the current side-specific candidate terms into a first controlled custom stopword list and compare it against the raw-text baseline.
3. Only after the stopword ablation is stable, move on to temporal candidate-window constraints such as `0/6/12/18` month retrieval.
4. Move to `match` to compare embedding-based matching against the accepted TF-IDF baseline.
5. Move the full lag-analysis pipeline to `analysis` once the preferred matcher is selected.
