# TF-IDF First Baseline Reviewed Summary

## Scope

This summary consolidates the human review stored in `TF-IDF First baseline Reviewed.xlsx`. It is meant to lock the current interpretation of the raw-text TF-IDF baseline before the first controlled tuning experiment.

## Coverage

- Reviewed rows: `60`
- Filled numeric review rows: `59` of `60`
- Keep-for-eval rows: `37`

## Main Quantitative Findings

- Mean theme relevance: `0.804`
- Mean granularity fit: `0.708`
- Mean temporal plausibility: `0.362`

### By Domain

| domain | mean theme relevance | mean granularity fit | mean temporal plausibility | keep rate |
| --- | --- | --- | --- | --- |
| `biomed` | 0.742 | 0.649 | 0.381 | 75.0% |
| `cs` | 0.838 | 0.747 | 0.359 | 75.0% |
| `env_energy` | 0.830 | 0.724 | 0.348 | 35.0% |

### Overall Labels

- `Strong Relavance`: `35`
- `partial relavance`: `17`
- `Not Related at all`: `3`
- `weak relavance`: `3`
- `strong relavance`: `2`

### Error Types

- `none`: `19`
- `duplicate_candidate`: `16`
- `scope_mismatch`: `14`
- `temporal_mismatch`: `6`
- `domain_mismatch`: `2`
- `language gap  mismatching`: `1`
- `review later than grant`: `1`
- `repeat_error`: `1`

## Interpretation

1. The baseline is not failing mainly because it cannot find topical overlap. Theme relevance and granularity are both moderate-to-high on average.
2. The weakest dimension is temporal plausibility, which confirms that the raw baseline is still behaving more like a lexical retriever than a temporally interpretable matcher.
3. The most important non-temporal error modes are `duplicate_candidate` and `scope_mismatch`, which means the retriever often lands in the right neighborhood but over-favors repeated review papers or broad shared terminology.
4. `env_energy` has the lowest keep rate, so that domain is the clearest signal that lexical overlap alone is not enough.

## Recommended First Controlled Improvement

The first tuning step should still be a conservative stopword ablation, not a model jump. Based on the review comments, the main target is generic institutional wording on the grant side and paper-writing boilerplate on the arXiv side.

### Proposed Grant-Side Stopword Candidates v1

- `program`, `funding`, `announcement`, `support`, `project`, `research`, `opportunity`, `award`, `cooperative`, `application`, `development`

### Proposed arXiv-Side Stopword Candidates v1

- `paper`, `review`, `perspective`, `overview`, `approach`, `study`, `using`, `based`, `present`, `results`, `analysis`

## Next Step

Run one controlled TF-IDF ablation with only these conservative side-specific stopwords, then compare it against the raw baseline using the reviewed sample and the existing domain summary tables.
