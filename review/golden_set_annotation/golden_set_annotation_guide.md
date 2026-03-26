# Golden Set Annotation Guide

## Purpose

This folder contains the candidate package for the baseline branch golden set.
The goal is to lock a human-reviewed comparison set without changing any existing notebook section or DuckDB table.

The current annotation uses only two judgments:

1. `temporal_ok`
   This field is prefilled by code.
   Rule: `delta_t_days > 0` means `1`, otherwise `0`.
2. `topic_ok`
   This field must be filled manually.
   Rule: `1` means the grant topic and the arXiv paper are meaningfully related.
   Rule: `0` means the pair is not topically relevant enough for the golden set.

## File List

1. `golden_set_candidates.csv`
   The annotation candidate file.
2. `golden_set_reviewer.html`
   A single-file browser review tool for loading the CSV, reviewing one pair at a time, and exporting a reviewed `.xlsx`.

## Sampling Logic

The candidate set is intentionally split into three groups so later evaluation remains interpretable.

### 1. Raw Group

- Source: `delta_t_pairs`
- Filter:
  - `pool_used = 'raw'`
  - `similarity >= 0.10`
- Size:
  - `20` pairs per domain
  - `60` pairs total
- Time coverage:
  - `early_2008_2012`: `7` pairs
  - `mid_2013_2018`: `7` pairs
  - `recent_2019_2024`: `6` pairs
- Sampling strategy:
  - within each `domain × year_segment`, candidates are sorted by similarity;
  - selected rows are spread across the ranking range so the sample includes high, mid, and low similarity cases.

### 2. TW36 Group

- Source: `delta_t_pairs`
- Filter:
  - `pool_used = 'tw36'`
  - `similarity >= 0.10`
- Size:
  - `10` pairs per domain
  - `30` pairs total
- Time coverage:
  - `early_2008_2012`: `3` pairs
  - `mid_2013_2018`: `3` pairs
  - `recent_2019_2024`: `4` pairs

This group is kept separate because its temporal direction is partly helped by the `36`-month window constraint.

### 3. Negative Group

- Source:
  - grants from `grant_pilot_labeled`
  - papers from `arxiv_pilot_labeled`
- Construction:
  - random cross-domain pairings, not retrieved by the matcher
- Size:
  - `15` pairs total
  - `5` pairs for each unordered domain pair:
    - `biomed__x__cs`
    - `biomed__x__env_energy`
    - `cs__x__env_energy`
- Time coverage:
  - each domain pair includes early, mid, and recent years on the grant side

For negative rows:

- `source_group = negative`
- `pool_used = negative`
- `similarity` is intentionally left blank because these rows are synthetic cross-domain controls rather than retrieval outputs

## Column Notes

- `annotation_id`: stable row id for review tracking
- `source_group`: `raw`, `tw36`, or `negative`
- `pool_used`: original pool label; for synthetic negatives this is set to `negative`
- `domain`: common domain for positive rows, cross-domain label for negative rows
- `grant_domain`: grant-side domain
- `arxiv_domain`: arXiv-side domain
- `domain_pair`: explicit pair label
- `year_segment`: `early_2008_2012`, `mid_2013_2018`, or `recent_2019_2024`
- `similarity_band`: `high`, `mid`, `low`, or `random_cross_domain`
- `grant_year`: year extracted from the grant `posted_date`
- `similarity`: baseline similarity score; blank for negative controls
- `delta_t_days`: `grant_posted_date - arxiv_submitted_date`
- `temporal_ok`: prefilled temporal direction label
- `topic_ok`: manual label to fill
- `review_notes`: optional free-text note

## Annotation Standard

Use a conservative relevance rule.

Mark `topic_ok = 1` only if the pair is clearly aligned in research topic, problem setting, or funding need.

Mark `topic_ok = 0` if any of the following dominates:

1. only very generic vocabulary overlaps
2. same broad domain but different substantive problem
3. same technology words but different application setting
4. obvious cross-domain mismatch
5. a review/survey style paper that is too broad to be a meaningful topic match

## Recommended Workflow

1. Open `golden_set_reviewer.html` in a browser.
2. Load `golden_set_candidates.csv`.
3. Review one row at a time.
4. Fill `topic_ok` and optional `review_notes`.
5. Export the reviewed file as `.xlsx`.

The HTML tool automatically renames the export to a `...reviewed.xlsx` filename when possible.
