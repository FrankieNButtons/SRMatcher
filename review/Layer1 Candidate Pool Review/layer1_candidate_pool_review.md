# Layer 1 Candidate-Pool Review

## Purpose

Review how the main Layer 1 candidate-pool controls change the top-1 match on the already reviewed sample.

## What To Compare

1. `raw_baseline`: the original top-1.
2. `layer1_1a_language_filter`: whether minor non-English noise removal changes anything meaningful.
3. `layer1_1b_time_window_36m`: a history-only pool with the best similarity among the tested time windows.
4. `layer1_1c_duplicate_cap_k5`: the duplicate-control variant.

## Review Standard

1. Is the tuned result semantically more on-topic than the raw result?
2. Does the tuned result improve temporal plausibility without becoming too generic?
3. Which control is more acceptable for the next baseline row: time window or duplicate cap?

## Expected Decision

Decide whether Layer 2 should start from the raw baseline, a time-window variant, a duplicate-cap variant, or a combined Layer 1 final candidate pool.

## Sample Columns

- `raw_*`: current reviewed baseline match.
- `lang_*`: language-filter top-1.
- `tw36_*`: 36-month history-only top-1.
- `dup_*`: duplicate-cap top-1.
- `overall_label`, `error_type`, `review_notes`: your original human judgments.

The structured table is in `layer1_candidate_pool_review.csv`.
