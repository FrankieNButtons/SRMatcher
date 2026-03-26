# Note Of Change

This file records substantive project edits, their purpose, and their observed result so future iterations can reuse good directions and avoid repeated mistakes.

## Logging Rule

- Record meaningful improvement attempts, pipeline changes, evaluation changes, and analysis-direction changes.
- Skip tiny bug fixes unless they materially affect results or interpretation.
- When a change is based on external sources, add the source to `REFERENCE.md` and cite it here.

## Entries

### 2026-03-26 - Recorded Match-Branch Readiness in Project Instructions

- Purpose: preserve the project-level instruction change that formally repositions the repository from a completed `baseline` branch to a not-yet-opened but ready-to-start `match` branch.
- Change:
  - recorded that `AGENTS.md` and `CLAUDE.md` were updated to show:
    - all baseline exit conditions satisfied,
    - statistical verification completed,
    - `match` not yet opened and waiting for Frankie's authorization from the baseline tip;
  - recorded that both instruction files now reference `srmatcher_match_roadmap.svg` as the visual roadmap for the `match` branch;
  - recorded that both instruction files now reserve notebook Section `19` as the first `match`-branch section unless that section number is already present in `code.ipynb`.
- Result:
  - the instruction-level branch state change is now logged in project memory instead of existing only inside `AGENTS.md` and `CLAUDE.md`;
  - future agents can recover why the repository is considered baseline-complete but still branch-frozen pending Frankie's explicit authorization;
  - the first `match`-branch notebook step is now explicitly anchored to Section `19` and the embedding baseline plan.

### 2026-03-26 - Deliberately Skipped Layer 2 Text-Representation Tuning

- Purpose: document the deliberate decision to skip Layer 2 before entering the `match` branch.
- Reasoning:
  - stopword-v1 confirmed that representation signals are drowned out by candidate-pool noise before Layer 1 cleanup;
  - Layer 1 Final achieved approximately `60%` temporal coherence and established a stable `Δt` baseline; further TF-IDF tuning would not materially change the `Δt` distribution;
  - the primary research goal is `Δt` measurement, not TF-IDF optimization; embedding methods in the `match` branch will supersede TF-IDF representation quality entirely;
  - statistical validation in Section `18` confirmed that the current baseline already has `Precision@10 = 90%` on the golden set, which is sufficient as a comparison target.
- Result: Layer 2 officially skipped. `tfidf_baseline_layer1_final` is treated as `tfidf_baseline_final`.
- Future reuse: do not revisit Layer 2 unless embedding results show unexpected degradation pointing back to text-field issues.

### 2026-03-26 - Baseline Statistical Validation and Branch Closure

- Purpose: formally close the `baseline` branch with hypothesis-level statistical validation, convert the already-built descriptive findings into explicit inferential evidence, and check whether the reviewed golden set supports the baseline as a valid comparison target for the later `match` branch.
- Change:
  - extended `code.ipynb` with a new self-contained section:
    - `## 18. Baseline 统计检验与收尾`;
  - added a reuse-first validation block with `BASELINE_STATS_REUSE_EXISTING = True`;
  - implemented fallback loading logic so the section:
    - reuses `delta_t_pairs`, `delta_t_yearly_trend`, and `tfidf_baseline_matches_raw` when they already exist;
    - rebuilds the needed dataframes from the current pilot tables and `tfidf_baseline_layer1_final` if those reused tables are missing;
  - added four groups of inferential tests for the baseline temporal structure:
    - one-sample Wilcoxon signed-rank tests for the main `raw + tw36` `Δt` distributions by domain;
    - cross-domain Kruskal-Wallis plus Bonferroni-corrected Mann-Whitney U pairwise comparisons;
    - Spearman trend tests on `delta_t_yearly_trend` for `2008-2024`;
    - main-vs-`dup` Mann-Whitney U tests by domain;
  - integrated the reviewed golden set workbook:
    - `review/golden_set_annotation/golden_set_candidates_reviewed.xlsx`;
  - added a retrieval-side evaluation layer:
    - `Precision@5`,
    - `Precision@10`,
    - positive-vs-negative average observed rank,
    - topic-label similarity difference test;
  - added publication-ready English plots for all five result groups while keeping the interpretation cells in Chinese.
- Result:
  - the main `Δt` distribution is significantly positive in all three domains:
    - `biomed`: `W = 465135402.0`, `p < 1e-16`, rank-biserial `0.929`;
    - `cs`: `W = 142111207.0`, `p < 1e-16`, rank-biserial `0.922`;
    - `env_energy`: `W = 631544062.0`, `p < 1e-16`, rank-biserial `0.957`;
  - cross-domain differences are also significant:
    - Kruskal-Wallis: `H = 467.123`, `p = 3.68e-102`;
    - pairwise Bonferroni-corrected tests:
      - `biomed vs cs`: `U = 290263883.5`, `p < 1e-16`;
      - `biomed vs env_energy`: `U = 539745332.5`, `p = 2.67e-14`;
      - `cs vs env_energy`: `U = 274593516.5`, `p < 1e-16`;
  - yearly `Δt` medians rise significantly over time:
    - `biomed`: `rho = 0.718`, `p = 1.17e-03`;
    - `cs`: `rho = 0.593`, `p = 1.21e-02`;
    - `env_energy`: `rho = 0.819`, `p = 5.90e-05`;
  - the main distribution and the `dup` diagnostic group are decisively different:
    - `biomed`: `U = 936421078.5`, `p < 1e-16`, rank-biserial `0.610`;
    - `cs`: `U = 233813844.0`, `p < 1e-16`, rank-biserial `0.634`;
    - `env_energy`: `U = 1307193766.0`, `p < 1e-16`, rank-biserial `0.642`;
  - the reviewed golden set gives a strong retrieval signal for the current baseline:
    - `Precision@5 = 87.5%`;
    - `Precision@10 = 90.0%`;
    - positive reviewed pairs have average observed rank `3.10`;
    - synthetic negative controls have average observed rank `21.00`;
    - `topic_ok = 1` vs `topic_ok = 0` similarity difference:
      - `U = 1564.0`,
      - `p = 4.75e-06`,
      - rank-biserial `0.564`.
- Statistical summary table:

| 假设 | 检验方法 | 统计量 | p 值 | 结论 |
|------|---------|--------|------|------|
| 主分布 Δt > 0（biomed） | Wilcoxon | `W=465135402.0` | `<1e-16` | 显著 |
| 主分布 Δt > 0（cs） | Wilcoxon | `W=142111207.0` | `<1e-16` | 显著 |
| 主分布 Δt > 0（env_energy） | Wilcoxon | `W=631544062.0` | `<1e-16` | 显著 |
| 三域 Δt 差异 | Kruskal-Wallis | `H=467.123` | `<1e-16` | 显著 |
| biomed vs cs | Mann-Whitney U | `U=290263883.5` | `<1e-16` | 显著 |
| biomed vs env_energy | Mann-Whitney U | `U=539745332.5` | `2.67e-14` | 显著 |
| cs vs env_energy | Mann-Whitney U | `U=274593516.5` | `<1e-16` | 显著 |
| CS Δt 年度上升趋势 | Spearman | `rho=0.593` | `1.21e-02` | 显著 |
| 主分布 vs dup（biomed） | Mann-Whitney U | `U=936421078.5` | `<1e-16` | 显著 |
| golden set Precision@10 | — | — | — | `90.0%` |

- Baseline closure statement:
  - the baseline branch now has:
    - a locked main `Δt` benchmark,
    - a separated `dup` diagnostic subgroup,
    - a yearly trend benchmark,
    - a reviewed golden set with retrieval-side validation;
  - therefore, the baseline methodology is formally complete as a comparison target;
  - however, the branch should not be switched automatically: the next step should be to recommend moving to `match` and wait for explicit approval before creating or switching branches.

### 2026-03-25 - Prepared Golden Set Annotation Candidates

- Purpose: prepare the final human-annotation package needed to lock the baseline-branch golden set, while keeping `raw` and `tw36` temporally interpretable and ensuring that the sample spans the early, middle, and recent grant periods.
- Change:
  - created a new review package under `review/golden_set_annotation/`;
  - generated `golden_set_candidates.csv` without changing any notebook section or DuckDB table;
  - built the candidate file from three components:
    - `raw` main baseline group:
      - `20` pairs per domain, `60` total,
      - sampled from `pool_used = 'raw'` and `similarity >= 0.10`;
    - `tw36` constrained comparison group:
      - `10` pairs per domain, `30` total,
      - sampled from `pool_used = 'tw36'` and `similarity >= 0.10`;
    - synthetic cross-domain negative group:
      - `15` total,
      - `5` rows for each unordered domain pair:
        - `biomed__x__cs`,
        - `biomed__x__env_energy`,
        - `cs__x__env_energy`;
  - enforced year coverage on the grant side:
    - `early_2008_2012`,
    - `mid_2013_2018`,
    - `recent_2019_2024`;
  - stratified the positive samples inside each `domain × year_segment` cell so the review set includes higher-, middle-, and lower-similarity cases instead of only top-scoring rows;
  - prefilled `temporal_ok` from `delta_t_days > 0`, left `topic_ok` blank for manual review, and included grant/arXiv text fields for side-by-side annotation;
  - added two review-support files:
    - `golden_set_annotation_guide.md`,
    - `golden_set_reviewer.html`, a single-file browser tool that loads the CSV and exports a reviewed `.xlsx`.
- Result:
  - the candidate package contains `105` rows in total:
    - `60` raw,
    - `30` tw36,
    - `15` negative;
  - the positive sample coverage is balanced across the three time periods for every domain:
    - raw:
      - `7 / 7 / 6` per `early / mid / recent`,
    - tw36:
      - `3 / 3 / 4` per `early / mid / recent`;
  - the negative controls also span all three periods, preventing the golden set from collapsing into a single recent-era slice;
  - the project now has a review-ready golden-set package that can be labeled in the browser and exported as a reviewed spreadsheet without adding more notebook or DuckDB complexity.
- Conclusion for reuse:
  - this package should be the baseline-branch annotation starting point unless the project explicitly decides to redraw the golden-set sampling logic;
  - later revisions should preserve the distinction between `raw`, `tw36`, and `negative`, because mixing them would weaken the interpretability of both topic and temporal judgments.

### 2026-03-25 - Updated the Baseline Status Board to Reflect the Remaining Exit Gate

- Purpose: synchronize the agent instruction files with the current baseline state so future agents see that the main `Δt` benchmark and yearly trend work are already complete, and that the golden set is now the only remaining exit condition.
- Change:
  - updated the `Status Board` in `AGENTS.md` and `CLAUDE.md`;
  - replaced the prior stage summary with a checklist-style current-stage description showing:
    - Layer 1 Final combined rule completed,
    - main `Δt` baseline locked with `raw + tw36` separated from `dup`,
    - yearly trend analysis completed via `delta_t_yearly_trend`,
    - golden-set construction and locking as the only remaining baseline exit requirement.
- Result:
  - the instruction files now present a clearer and more up-to-date branch state;
  - future agents should be less likely to revisit already-completed `Δt` baseline work;
  - the next gating task before `match` is now explicit as golden-set completion only.

### 2026-03-24 - Added Yearly Main-Distribution `Δt` Trend by Grant Posted Year

- Purpose: extend the locked baseline `Δt` analysis from one pooled summary into a year-by-year trend view, so later `match`-branch methods can be compared not only on the overall median but also on whether they preserve the temporal shape of the main signal over time.
- Change:
  - extended `code.ipynb` with a new self-contained section:
    - `## 17. Δt 年度趋势（按 Grant Posted Year）`;
  - added a reuse-first notebook block with `DT_TREND_REUSE_EXISTING = True`;
  - materialized a new DuckDB table:
    - `delta_t_yearly_trend`;
  - implemented yearly aggregation from the main `Δt` subgroup only:
    - source pairs: `delta_t_pairs`,
    - join target: `grant_pilot_labeled` for `posted_date`,
    - filters: `pool_used IN ('raw', 'tw36')`, `similarity >= 0.10`, and grant year `2005-2024`,
    - yearly metric: median `delta_t_days` by `grant_year` and `domain`;
  - added an English publication-ready line chart with:
    - one line per domain,
    - marker size proportional to yearly valid-pair count,
    - a zero-reference line,
    - explicit annotation of the low-support `cs` outlier in `2005`.
- Result:
  - the yearly main-distribution trend is now persisted for all three pilot domains across `2005-2024`;
  - after the low-support early years, all three domains show consistently positive yearly median `Δt`, especially from `2010` onward;
  - by `2024`, the yearly medians reach:
    - `biomed`: `1145` days,
    - `cs`: `857` days,
    - `env_energy`: `1222.5` days;
  - `biomed` and `env_energy` exhibit longer academic-to-grant lags overall, while `cs` remains shorter and more consistent with a faster research-demand cycle;
  - the `cs` value in `2005` is an obvious outlier at `-5276` days, but it is based on only `82` valid pairs and should be interpreted as early low-support noise rather than as the start of the main trend.
- Conclusion for reuse:
  - the baseline branch now has both a locked pooled `Δt` benchmark and a yearly-shape benchmark for the main distribution;
  - later matching methods should be evaluated not only on whether they improve similarity or shrink the `dup` subgroup, but also on whether they preserve this domain-wise yearly temporal structure;
  - the annual trend makes it easier to detect whether a new matcher introduces temporal distortion in specific periods even when its overall median looks acceptable.

### 2026-03-24 - Separated Main `Δt` Distribution from `dup` Diagnostic Group

- Purpose: lock the baseline temporal benchmark in the form required by the updated project rules, so the main `Δt` signal and the duplicate-driven lexical-convergence noise are reported separately before later matcher comparison.
- Change:
  - extended `code.ipynb` with a new self-contained section:
    - `## 16. Δt 主分布与 dup 诊断群分离报告`;
  - added a reuse-first notebook block with `DT_SEPARATION_REUSE_EXISTING = True`;
  - materialized two new DuckDB tables from `delta_t_pairs`:
    - `delta_t_main_summary` for `pool_used IN ('raw', 'tw36')`,
    - `delta_t_dup_diagnostic` for `pool_used = 'dup'`;
  - added side-by-side boxplots to compare the main temporal distribution against the `dup` diagnostic subgroup by domain;
  - added a locked notebook declaration stating that only the `raw + tw36` subgroup should be used as the baseline `Δt` benchmark for later `match`-branch comparison.
- Result:
  - the main temporal distribution is strongly positive and stable across domains:
    - `biomed`: median `583` days, mean `806.5`, positive-direction ratio `97.82%`, `n = 31,099`;
    - `cs`: median `484` days, mean `668.8`, positive-direction ratio `97.52%`, `n = 17,257`;
    - `env_energy`: median `609` days, mean `904.3`, positive-direction ratio `98.63%`, `n = 35,958`;
  - the `dup` subgroup is strongly negative in all three domains and behaves like noise rather than signal:
    - `biomed`: median `-1170` days, mean `-1199.4`, positive-direction ratio `28.58%`, `n = 37,397`;
    - `cs`: median `-1054` days, mean `-1206.4`, positive-direction ratio `26.37%`, `n = 16,581`;
    - `env_energy`: median `-1271` days, mean `-1270.9`, positive-direction ratio `27.08%`, `n = 44,287`;
  - the separation removes the misleading mixed-average interpretation from the main baseline report and makes the candidate-pool problem visible without letting it dominate the substantive `Δt` conclusion.
- Conclusion for reuse:
  - the baseline `Δt` benchmark should now be treated as locked on the main subgroup `pool_used IN ('raw', 'tw36')` with `similarity >= 0.10`;
  - the `dup` subgroup should remain in later reports only as a TF-IDF candidate-pool diagnostic, not as part of the primary temporal comparison target;
  - future `match`-branch methods should be judged in part by whether they preserve the positive main-distribution medians while reducing the size and influence of the `dup` diagnostic subgroup.

### 2026-03-24 - Refined `dup` Interpretation and Split the `Δt` Baseline Reporting Rule

- Purpose: prevent the baseline temporal analysis from treating duplicate-dominated convergence as if it were genuine temporal signal, and make the exit-stage `Δt` benchmark explicitly separable into main and diagnostic subgroups.
- Change:
  - updated `AGENTS.md` and `CLAUDE.md` to replace the earlier shorthand explanation of duplicate-hit papers with a stricter `dup pool` interpretation tied to `raw top-1` convergence by `10` or more grants;
  - added an explicit rule that `dup` should be reported separately from the main `raw + tw36` temporal distribution and should be interpreted as a TF-IDF candidate-pool quality diagnostic rather than as an independent substantive finding;
  - added a `Rule B` reporting constraint requiring the baseline `Δt` benchmark to be split into:
    - the main distribution for `pool_used IN ('raw', 'tw36')`,
    - the separate `dup` diagnostic subgroup;
  - updated the status board so the next required step is to separate the main distribution and the `dup` subgroup in the baseline `Δt` report before exit to `match`.
- Result:
  - the instructions now distinguish much more clearly between usable temporal signal and duplicate-driven lexical collapse;
  - future baseline summaries should avoid using mixed `raw + tw36 + dup` averages as the main conclusion;
  - the path to `match` is now more tightly tied to a cleanly interpreted `Δt` baseline report.

### 2026-03-24 - Added the First Full `Δt` Baseline Distribution Analysis

- Purpose: establish the first full-domain `Δt` benchmark inside the `baseline` branch so later embedding and skill-aware matchers can be compared against a fixed temporal baseline instead of only against similarity summaries.
- Change:
  - extended `code.ipynb` with a new self-contained section:
    - `## 15. Δt 分布初步分析（baseline 全量)`;
  - added a reuse-first notebook block with `DT_ANALYSIS_REUSE_EXISTING = True`;
  - materialized three new DuckDB tables:
    - `delta_t_pairs`,
    - `delta_t_domain_summary`,
    - `delta_t_pool_summary`;
  - implemented the requested valid-pair construction:
    - source table: `tfidf_baseline_layer1_final`,
    - joins: `grant_pilot_labeled` for `posted_date`, `arxiv_pilot_labeled` for `submitted_date`,
    - filters: `pool_used IN ('raw', 'tw36', 'dup')` and `similarity >= 0.10`,
    - metric: `delta_t_days = posted_date - submitted_date`;
  - added notebook outputs for:
    - domain-level summary statistics,
    - full-distribution boxplots,
    - overlay and per-domain histograms with `180`-day bins,
    - pool-used stratified comparison.
- Result:
  - the valid-pair set contains `182,579` rows:
    - `biomed 68,496`,
    - `cs 33,838`,
    - `env_energy 80,245`;
  - at the domain level, the medians are all positive and close to six months:
    - `biomed`: median `192` days, positive-direction ratio `60.02%`,
    - `cs`: median `184` days, positive-direction ratio `62.66%`,
    - `env_energy`: median `182` days, positive-direction ratio `59.14%`;
  - however, all three domain means are negative:
    - `biomed -288.7`,
    - `cs -250.1`,
    - `env_energy -296.2`,
    which shows that the baseline `Δt` distribution still has a substantial negative tail;
  - pool-used stratification makes the source of that tail explicit:
    - `raw` and `tw36` are strongly positive in all three domains,
    - `dup` is strongly negative in all three domains, with median `Δt` around `-1054` to `-1271` days and positive-direction ratio only about `26%` to `29%`.
- Conclusion for reuse:
  - the baseline branch now has its first fixed `Δt` benchmark for later matcher comparison;
  - the current baseline is partially reasonable because its domain medians are positive and stable, but it is not yet temporally clean because the `dup` pool creates a heavy negative tail;
  - future matching improvements should be evaluated not only by similarity, but by whether they preserve or improve the positive mid-distribution while shrinking the negative `Δt` tail.

### 2026-03-24 - Reframed Baseline Around `Δt` Rather Than Unique-Match Retrieval

- Purpose: align the baseline branch with the paper’s real analytical target by shifting the evaluation focus from top-1 retrieval toward temporal-lag measurement and by relaxing the golden-set role from a hard retrieval gate to a directional validation aid.
- Change:
  - updated `AGENTS.md` and `CLAUDE.md` with a new section inserted after `Baseline Ablation Strategy`;
  - added Rule A to redefine the task around high-similarity pair sets and `Δt` distribution analysis instead of unique best-paper retrieval;
  - added Rule B to require that the `Δt` formula, valid-pair similarity threshold, and one full three-domain `Δt` distribution baseline be locked inside the `baseline` branch before any move to `match`;
  - added Rule C to reposition the golden set as a temporal-direction and topic-relevance validation tool rather than an exact-retrieval ground truth, and to allow it to proceed in parallel with initial `Δt` analysis instead of acting as the sole gating item.
- Result:
  - the project instructions now better match the stated research question of measuring topic lag between academic appearance and funding-side uptake;
  - duplicate-hit papers can now be interpreted as topic anchors rather than only as noise;
  - future baseline evaluation should emphasize `Δt` distribution behavior in addition to similarity-based metrics;
  - the path to the `match` branch is now tied more directly to a locked `Δt` comparison baseline than to a prematurely rigid golden-set requirement.

### 2026-03-24 - Implemented Layer 1 Final Combined Candidate-Pool Rule

- Purpose: turn the completed Layer 1 ablation plus human review into an actual executable combined candidate-pool rule, while keeping the implementation inside the `baseline` branch and preserving all earlier baseline tables unchanged.
- Change:
  - extended `code.ipynb` with a new self-contained section:
    - `## 14. Layer 1 Final：组合候选池规则`;
  - added a reuse-first notebook module with `LAYER1_FINAL_REUSE_EXISTING = True`, so the new section can run independently in a fresh kernel without rerunning earlier notebook sections;
  - implemented and materialized three new DuckDB tables:
    - `arxiv_top1_frequency`,
    - `tfidf_baseline_layer1_final`,
    - `tfidf_baseline_layer1_exclusions`;
  - implemented the requested fixed-priority routing rule:
    - `excluded` for the hard-coded reviewed exclusions (`BIOMED_01`, `BIOMED_08`, `CS_14`, `ENV_ENERGY_17`) mapped to their grant ids through `tfidf_baseline_reviewed_top1`,
    - `dup` when the raw top-1 `arxiv_id` appears in at least `10` distinct grants and the duplicate-controlled Layer-1 row exists,
    - `tw36` when raw is temporally inverted and the `tw36` similarity is no more than `0.15` below raw,
    - `raw` otherwise;
  - added notebook output blocks for:
    - top-50 raw top-1 repetition frequencies,
    - exclusion summary,
    - raw-vs-final domain comparison,
    - pool-used distribution by domain.
- Result:
  - the raw top-1 repetition problem is extremely concentrated:
    - the most reused paper (`2303.10871`) appears as top-1 for `1164` grants,
    - the next few most reused papers appear `884`, `520`, `447`, and `419` times;
  - the exclusion rule removes exactly `4` rows:
    - `biomed 2`,
    - `cs 1`,
    - `env_energy 1`;
  - the implemented `layer1_final` substantially increases temporal coherence relative to raw:
    - `biomed`: `28.12% -> 60.00%`,
    - `cs`: `22.97% -> 63.53%`,
    - `env_energy`: `29.63% -> 59.65%`;
  - but the same rule lowers average similarity:
    - `biomed`: `0.1818 -> 0.1546`,
    - `cs`: `0.2059 -> 0.1641`,
    - `env_energy`: `0.1698 -> 0.1501`;
  - the fixed `dup >= 10` threshold makes the final routing highly dominated by `dup` and `tw36`:
    - `dup` share is `54.41%` in `biomed`, `50.34%` in `cs`, and `55.41%` in `env_energy`,
    - `tw36` share is `32.03%`, `36.13%`, and `31.06%`,
    - raw is left with only about `13.5%` of rows in every domain.
- Conclusion for reuse:
  - the implementation is correct with respect to the fixed rule requested in the prompt;
  - however, the resulting routing is no longer a light-touch correction over raw, but a strongly `dup + tw36` dominated candidate-pool regime;
  - this result should be treated as a baseline-stage finding to evaluate in the next prompt, not as proof that the current thresholds are optimal.

### 2026-03-24 - Interpreted the Completed Layer 1 Human Review and Locked the Next Decision

- Purpose: convert the completed Layer 1 human review from a temporary inspection artifact into an explicit project conclusion that can guide the next baseline-stage implementation without prematurely starting Layer 2.
- Change:
  - read the completed review files:
    - `review/Layer1 Candidate Pool Review/layer1_candidate_pool_review_completed.csv`,
    - `review/Layer1 Candidate Pool Review/layer1_candidate_pool_review_completed.md`;
  - summarized the human choices across `raw`, `tw36`, `dup`, and `none`;
  - compared the preferred pool choices against:
    - domain,
    - `keep_for_eval_bool`,
    - error type,
    - similarity loss and lag improvement relative to raw;
  - prepared the interpretation for notebook and project-memory use, but deliberately did **not** implement the combined Layer 1 final rule yet, because that work is deferred to the next prompt.
- Result:
  - the completed human review rejects the idea of replacing the raw baseline with one global Layer 1 alternative:
    - `raw = 32`,
    - `tw36 = 14`,
    - `dup = 10`,
    - `none = 4`;
  - `raw` remains the dominant default among keepable cases:
    - within `keep_for_eval = True`, the preferred counts are `raw 28`, `tw36 8`, `dup 1`, `none 0`;
  - `lang` is effectively confirmed as cleanup only:
    - no reviewed row selected `lang` as the preferred Layer 1 pool;
  - `tw36` behaves like a temporal-correction tool rather than a new universal baseline:
    - it is preferred mainly for `review later than grant`, `temporal_mismatch`, and part of the `duplicate_candidate` cases;
    - when selected, it improves lag by about `1737` days on average relative to raw, but at a large average similarity loss of about `0.148`;
  - `dup` behaves like a low-semantic-cost de-duplication control:
    - it is preferred almost entirely on `duplicate_candidate` cases;
    - when selected, its average similarity loss relative to raw is only about `0.012`, with median similarity loss `0.0`;
  - the `none = 4` rows confirm that some reviewed pairs should be excluded from downstream evaluation rather than force-matched:
    - these cases are dominated by domain drift or unrecoverable mismatch.
- Conclusion for reuse:
  - the project should not choose a single global winner among `raw`, `tw36`, and `dup`;
  - the next implementation step should be a **combined Layer 1 final rule** with:
    - `raw` as the default,
    - `dup` as the duplicate-candidate control,
    - `tw36` as the temporal-correction fallback,
    - `none`-like cases excluded from downstream evaluation when appropriate;
  - that implementation step is intentionally postponed until the next prompt.

### 2026-03-24 - Completed Layer 1 Candidate-Pool Ablation and Prepared the Next Human Review

- Purpose: finish the mandatory Layer 1 candidate-pool ablation before any further text-representation tuning, then convert the results into reusable notebook, DuckDB, and human-review artifacts.
- Change:
  - ran the full Layer 1 joint ablation against the raw baseline, covering:
    - `1a` language filter,
    - `1b` time-window variants (`12m`, `24m`, `36m`),
    - `1c` duplicate-candidate cap with `K = 5`;
  - materialized the Layer 1 result tables in DuckDB:
    - `tfidf_baseline_layer1_ablation`,
    - `tfidf_baseline_layer1_top1_matches`,
    - `tfidf_baseline_layer1_comparison`,
    - `tfidf_baseline_layer1_review_delta`,
    - `tfidf_baseline_layer1_review_summary`;
  - corrected an initial review-summary join bug after the first run, so the per-domain human-review counts now align with the `20` reviewed rows per domain instead of incorrectly aggregating across all domains;
  - extended `code.ipynb` with a new self-contained Layer 1 notebook section that reads the materialized tables instead of rerunning the full pipeline;
  - created a new human-review packet under `review/Layer1 Candidate Pool Review/` so the next decision can be made by directly comparing:
    - `raw_baseline`,
    - `layer1_1a_language_filter`,
    - `layer1_1b_time_window_36m`,
    - `layer1_1c_duplicate_cap_k5`
    on the already reviewed sample.
- Result:
  - language filtering is now clearly identified as cleanup, not a meaningful optimization:
    - `top1_avg_similarity` moved only from `-0.0004` to `0.0000`,
    - temporal coherence moved only from `-0.12` to `-0.01` percentage points relative to raw;
  - time windows are the strongest temporal intervention:
    - all three windows reach `100%` top-1 temporal coherence in all three domains,
    - all three keep `100%` top-1 coverage,
    - but they also reduce `top1_avg_similarity` by `0.0380` to `0.0614`;
  - inside the time-window family, `36m` is the least damaging variant and should be the representative one for the next human review:
    - `biomed`: similarity `0.1376`, median lag `455.0`,
    - `cs`: similarity `0.1586`, median lag `413.0`,
    - `env_energy`: similarity `0.1318`, median lag `465.0`;
  - duplicate control is not a universal gain:
    - `cs` improves from `22.97%` to `26.87%` temporal coherence and from `-1467.0` to `-1149.0` median lag, but coverage drops to `90.74%`,
    - `biomed` changes only marginally,
    - `env_energy` worsens from `29.63%` to `27.79%` temporal coherence;
  - the reviewed-sample deltas confirm that Layer 1 variants are not cosmetic:
    - `tw36` changes `18/20` reviewed top-1 pairs in every domain,
    - `dupK5` changes `1/20` in `biomed`, `2/20` in `cs`, and `5/20` in `env_energy`.
- Conclusion for reuse:
  - Layer 1 is now complete and should be treated as the finished candidate-pool ablation block for the baseline branch;
  - do not jump straight into Layer 2 field-combination tuning before resolving the current human-in-the-loop decision;
  - the immediate next decision is to review whether `tw36`, `dupK5`, or a combined candidate-pool rule is the right baseline substrate for Layer 2.

### 2026-03-24 - Added SVG-Roadmap Reference and Notebook-Extension Rule

- Purpose: make the project instructions explicitly recognize the baseline SVG roadmap as a useful reference while also locking in the notebook workflow preference of extension over replacement.
- Change:
  - updated `AGENTS.md` and `CLAUDE.md` to treat `srmatcher_baseline_roadmap.svg` as a visual roadmap for baseline sequencing and exit criteria when it agrees with the written rules;
  - added an explicit notebook rule preferring extension of `code.ipynb` through new self-contained sections rather than notebook replacement or wholesale rewrites;
  - added an execution rule saying that if the SVG and the written instructions ever disagree, the written instructions remain authoritative and the mismatch should be stated explicitly.
- Result:
  - future agents now have both a text rule set and a visual roadmap for the baseline branch;
  - notebook work is less likely to break continuity by replacing the existing exploratory and ablation history;
  - the project keeps the SVG as guidance without allowing it to silently override the written execution contract.

### 2026-03-24 - Added Baseline Two-Layer Ablation Gate to Project Guidance

- Purpose: convert the baseline branch from a loose sequence of tuning attempts into a hard-gated two-layer ablation program so later agents cannot skip candidate-pool cleanup or leave the baseline branch too early.
- Change:
  - updated `AGENTS.md` and `CLAUDE.md` with a dedicated baseline ablation strategy section;
  - defined the core rule that each baseline experiment must become one row in a single ablation table with explicit configuration name, top-1 similarity, temporal coherence, and notes;
  - enforced Layer 1 before Layer 2, with Layer 1 requiring the joint completion of:
    - `1a` language filter,
    - `1b` time window (`12` / `24` / `36` months),
    - `1c` duplicate-candidate cap;
  - enforced Layer 2 order as:
    - `2a` field combination,
    - `2b` stopword tuning,
    - `2c` hyperparameter and n-gram tuning;
  - added a hard baseline exit gate requiring:
    - `tfidf_baseline_final` in DuckDB,
    - a locked `100` to `150` pair golden set,
    - a complete two-layer ablation log in `NoteOfChange.md`;
  - updated the stopword rule so pre-Layer-1 stopword results are treated only as dirty-candidate-pool negative evidence, not as final proof that stopwords are ineffective;
  - updated the status board so the next required action is the Layer 1 joint ablation rather than more isolated stopword work.
- Result:
  - the baseline branch now has a much stricter execution order and completion definition;
  - future execution agents should be less likely to jump prematurely into representation tuning or switch to `match` too early;
  - the experimental chapter structure is now aligned with a single progressive ablation table instead of disconnected tuning attempts.

### 2026-03-24 - Added Stopword-v1 Notebook Module and Confirmed Negative Tuning Result

- Purpose: run the first controlled baseline-improvement attempt after human review, while also reducing notebook rerun cost by making the new tuning block self-contained and table-reuse-first.
- Change:
  - extended `code.ipynb` with a new stopword-v1 tuning section instead of rewriting the notebook;
  - added a self-contained notebook module that:
    - can run independently of the earlier EDA cells,
    - defaults to reusing existing DuckDB tables when present,
    - only rebuilds the stopword-v1 results when explicitly needed;
  - materialized and reused these DuckDB tables:
    - `tfidf_baseline_matches_stopwords_v1`,
    - `tfidf_baseline_domain_summary_stopwords_v1`,
    - `tfidf_baseline_runtime_stopwords_v1`,
    - `tfidf_baseline_comparison_stopwords_v1`,
    - `tfidf_baseline_review_delta_stopwords_v1`;
  - added notebook interpretation cells that compare the tuned baseline against the raw baseline and the reviewed human-in-the-loop sample.
- Result:
  - the new notebook section now supports a much faster workflow: after the tables exist, the user can open a fresh kernel and run only the new tuning section instead of rerunning the full notebook;
  - the first conservative stopword ablation produced an informative negative result:
    - `top1_avg_similarity` stayed unchanged to four decimal places in all three domains,
    - `top1_arxiv_earlier_pct` changed only by `-0.03` to `+0.02` percentage points,
    - only `3/60` reviewed top-1 cases changed at all (`biomed 1`, `cs 2`, `env_energy 0`),
    - none of the raw human-rejected cases were corrected by this stopword-v1 run.
- Conclusion for reuse:
  - do not spend more time refining this same conservative stopword list before testing a more structural intervention;
  - the next baseline-stage improvement should target errors that the human review identified as more binding:
    - repeated review candidates,
    - overly broad grant scope,
    - candidate-pool timing.

### 2026-03-23 - Integrated Human Review Workbook and Locked First Tuning Direction

- Purpose: convert the completed human review from spreadsheet form into a durable project artifact that can directly guide the first controlled baseline-improvement attempt.
- Change:
  - read `review/TF-IDF First baseline Reviewed.xlsx` and normalized the filled review fields;
  - materialized the reviewed rows into DuckDB as `tfidf_baseline_reviewed_top1`;
  - materialized summary statistics into DuckDB as `tfidf_baseline_reviewed_summary`;
  - wrote a persistent interpretation note to `review/TF-IDF First baseline Reviewed Summary.md`;
  - distilled the first conservative stopword-ablation direction from the human labels instead of guessing it only from raw frequency.
- Result:
  - all `60` reviewed top-1 cases are now queryable inside DuckDB rather than existing only in the spreadsheet;
  - the human review confirms that the current raw baseline still captures substantial topical overlap:
    - mean theme relevance is `0.804`,
    - mean granularity fit is `0.708`;
  - the weakest dimension is clearly temporal plausibility at only `0.362`;
  - the dominant non-temporal failure modes are:
    - `duplicate_candidate` (`16`),
    - `scope_mismatch` (`14`);
  - `env_energy` is currently the least reliable domain in the reviewed sample, with only `35.0%` of pairs marked to keep for later evaluation.
- Conclusion for reuse:
  - the next baseline-stage experiment should be a conservative side-specific stopword ablation;
  - do not jump to embeddings yet;
  - compare the stopword-tuned variant against both:
    - the raw baseline tables,
    - the reviewed sample preserved in `tfidf_baseline_reviewed_top1`.

### 2026-03-23 - Generalized the Human-in-the-Loop Mechanism

- Purpose: clarify that the human-in-the-loop rule is a general project mechanism rather than a requirement to always use the current `review/` example format.
- Change:
  - updated `AGENTS.md` and `CLAUDE.md` so the files under `review/` are treated as examples rather than the only valid review style;
  - expanded the guidance to allow multiple review formats, including markdown summaries, CSV tables, notebook sections, targeted examples, comparison tables, and in-turn review instructions;
  - changed the execution rule from surfacing a `review/` packet specifically to surfacing an appropriate review mechanism for the current decision.
- Result:
  - the project now preserves the human-in-the-loop requirement without locking future work into one review format;
  - future review workflows can adapt to the task while still requiring clear review standards, purpose, and expected outputs;
  - the current `review/` artifacts remain reusable examples rather than a hard constraint.

### 2026-03-23 - Added Active Human-in-the-Loop Review Guidance

- Purpose: make human review a standing part of the project workflow so the agent actively surfaces qualitative inspection tasks instead of advancing the research pipeline without decision-critical human judgment.
- Change:
  - updated `AGENTS.md` and `CLAUDE.md` with a dedicated human-in-the-loop review rule;
  - required the agent to proactively offer review material when modeling or interpretation decisions depend on manual judgment;
  - required review requests to include:
    - what to review,
    - the rubric or standard to use,
    - why the review matters,
    - what decision the review will support;
  - instructed the agent to reuse structured artifacts under `review/` when possible instead of creating fragmented review workflows.
- Result:
  - human review is now a formal checkpoint in the operating guidance rather than an optional behavior;
  - future turns should more consistently surface review packets such as `review/top1_highscore_human_review.csv` and `review/top1_highscore_human_review.md` at the right decision points;
  - the project workflow is now better aligned with iterative research practice, where qualitative judgment should guide method selection and analysis interpretation.

### 2026-03-23 - Prepared Human-in-the-Loop Review Pack for Top-1 Error Analysis

- Purpose: support the next baseline-stage decision with direct reading of high-scoring TF-IDF matches before any stopword tuning or stronger matching method is introduced.
- Change:
  - extracted the highest-similarity `match_rank = 1` pairs from `tfidf_baseline_matches_raw`;
  - kept the top `20` top-1 pairs per pilot domain, yielding `60` review cases in total;
  - joined each pair back to `grant_clean.description` and `arxiv_clean.abstract` so the human reviewer can read the actual text rather than only metadata;
  - created reusable review artifacts under `review/`:
    - `top1_highscore_human_review.md`,
    - `top1_highscore_human_review.csv`;
  - added structured review fields for:
    - theme relevance,
    - granularity fit,
    - temporal plausibility,
    - overall label,
    - error type,
    - keep-or-drop decision for later evaluation use.
- Result:
  - the project now has a persistent human-review packet for the most important first-pass baseline error analysis;
  - the selected sample already exposes several likely failure modes worth confirming manually:
    - repeated reuse of the same arXiv paper across multiple grants,
    - strong lexical overlap with temporally inverted pairs,
    - apparent topic drift inside the broad pilot domains;
  - conclusion for reuse:
    - use this review pack before building any custom stopword list;
    - preserve the completed judgments as the seed of a future proxy evaluation set and error taxonomy.

### 2026-03-23 - Added Stopword-Candidate Diagnostics and Raw-Text TF-IDF Baseline

- Purpose: continue the project in the original baseline workflow order by keeping custom stopwords as a later tuning step, while first building and materializing the raw-text domain-wise TF-IDF baseline.
- Change:
  - extended `code.ipynb` instead of rewriting it;
  - added a side-specific stopword-candidate module that identifies terms with high document frequency and high cross-domain entropy within each side;
  - wrote the candidate diagnostics into DuckDB as `side_stopword_candidates`;
  - added a raw-text TF-IDF baseline module over the three pilot domains using:
    - grant-side `demand_text`,
    - arXiv-side `paper_text`,
    - standard English stopwords only,
    - no custom stopword filtering yet;
  - materialized the baseline outputs into DuckDB:
    - `tfidf_baseline_matches_raw`,
    - `tfidf_baseline_domain_summary_raw`,
    - `tfidf_baseline_runtime_raw`;
  - added notebook-level summary and evaluation cells for:
    - top-1 similarity by domain,
    - temporal coherence by domain,
    - high-scoring top-1 example inspection;
  - updated notebook markdown notes to include result interpretation rather than only code-description text;
  - updated project-status files (`AGENTS.md`, `README.md`) to reflect that the raw-text baseline has now been built and the next step is error analysis plus controlled stopword tuning.
- Result:
  - the executed notebook now has `69` cells, `0` execution errors, and every code cell is followed by a markdown explanation cell;
  - side-specific stopword candidates show a meaningful stylistic split:
    - grant-side candidates are dominated by institutional/announcement terms such as `program`, `research`, `funding`, `support`, `announcement`;
    - arXiv-side candidates are dominated by paper-writing terms such as `model`, `results`, `using`, `based`, `data`, `present`;
  - the raw-text TF-IDF baseline produced `1,444,300` top-20 matches across the three pilot domains;
  - baseline summary:
    - `biomed`: top-1 average similarity `0.1818`, top-1 temporal coherence `28.12%`, median top-1 lag `-1280.5` days;
    - `cs`: top-1 average similarity `0.2059`, top-1 temporal coherence `22.97%`, median top-1 lag `-1467.0` days;
    - `env_energy`: top-1 average similarity `0.1698`, top-1 temporal coherence `29.63%`, median top-1 lag `-1242.0` days;
  - conclusion for reuse:
    - keep this baseline table as the locked control version;
    - do not apply custom stopwords before comparing against this raw-text baseline;
    - the next useful work is error analysis on temporally inverted high-score matches, followed by a controlled stopword ablation.

### 2026-03-19 - Matching-Readiness EDA Extension and Chinese Thesis-Ready Notes

- Purpose: test whether the existing EDA was already sufficient for a full matching-study overview, then strengthen the notebook where the data understanding was still thin, especially around retrieval asymmetry, domain-level readiness, and thesis-ready interpretation.
- Change:
  - extended `code.ipynb` again without rewriting the existing Phase-1 flow;
  - added a new "matching readiness" block with additional diagnostics:
    - grant-vs-arXiv retrieval imbalance table within the `2005-2024` window,
    - domain-wise imbalance bar chart,
    - grant agency concentration table,
    - domain-level profile table combining average text length and lexical-overlap Jaccard,
    - compact visualization summarizing domain-level length and overlap differences;
  - revised notebook markdown so every code cell is followed by an explanatory markdown cell written as result interpretation rather than code narration;
  - converted the notebook title and section headers to Chinese so the notebook can be used more directly as thesis-writing material;
  - re-executed the notebook after the changes and fixed a scope bug in the new domain-profile cell caused by reusing a closed DuckDB connection.
- Result:
  - the executed notebook now has `59` cells, `0` execution errors, and every code cell is followed by a markdown explanation cell;
  - the added diagnostics make the matching setup more defensible:
    - overall arXiv-to-grant ratio in `2005-2024` is about `29.56:1`,
    - domain ratios are highly uneven: `biomed 4.18:1`, `env_energy 9.76:1`, `cs 107.77:1`,
    - grant-side concentration is strong, with the top-5 agencies contributing `38.31%` and the top-10 agencies `48.54%` of records;
  - domain-level comparison now makes cross-side modeling risk more explicit:
    - grant `cs` descriptions average `379.35` words versus `166.01` for arXiv `cs` abstracts,
    - lexical-overlap Jaccard remains modest across all domains and is lowest in `env_energy` (`0.2225`);
  - conclusion for future work: the EDA is now sufficient to support a thesis-style data/EDA chapter and to justify why subsequent matching must be domain-aware and candidate-window-constrained rather than global.

### 2026-03-19 - Expanded EDA Notebook With Additional Visual Diagnostics

- Purpose: extend the current EDA beyond the initial pilot checks so the notebook can better support chapter writing, richer interpretation, and safer transition into retrieval modeling.
- Change:
  - extended `code.ipynb` instead of replacing its existing logic, keeping the Phase-1 structure and adding a richer "next phase of EDA" layer on top;
  - added more visual diagnostics:
    - arXiv `version_count` bar chart,
    - grant-vs-arXiv text-length histogram,
    - side-by-side top-term bar charts,
    - retained yearly trend lines and domain-year heatmaps;
  - added more descriptive analysis:
    - critical-field missingness overview across both sides,
    - richer text-style comparison using sampled grant descriptions and arXiv abstracts,
    - explicit lexical-overlap check between the two sides' top terms;
  - inserted explanatory markdown after every code cell so each output is immediately interpreted in-place inside the notebook;
  - executed the notebook end-to-end after the changes and verified that the pilot-domain tables remained consistent in DuckDB.
- Result:
  - the notebook now has `49` cells and every code cell is followed by a markdown explanation cell;
  - the executed notebook currently has `0` error outputs;
  - the expanded EDA makes the main modeling risk more explicit:
    - grant descriptions are longer and more sentence-dense than arXiv abstracts,
    - metadata quality is asymmetric across sides,
    - lexical overlap remains very low even after domain slicing;
  - the current EDA is therefore better positioned to support a thesis-style chapter before moving into temporal-window retrieval experiments.

### 2026-03-14 - Phase 1 EDA and Pilot-Domain Wrangling

- Purpose: start the first-stage exploratory workflow requested for the grant/arXiv pairing, validate text-field quality, define pilot slices, and persist reusable wrangling outputs for later temporal matching experiments.
- Change:
  - rewrote `code.ipynb` around Phase-1 EDA instead of the earlier mixed baseline flow;
  - added grant-side description quality checks using the raw XML plus cleaned retention counts;
  - added arXiv abstract quality checks against `arxiv_clean`;
  - fixed the effective overlap window to `2005-2024` for stable year-level analysis;
  - created `grant_pilot_labeled` and `arxiv_pilot_labeled` in DuckDB using mixed rules:
    - `cs`: technology keywords plus agency hints on the grant side, `cs.* / eess.* / stat.ML` on the arXiv side;
    - `biomed`: health agencies and `HL` activity plus medical keywords, matched with `q-bio` / `physics.bio-ph` plus biomedical keywords;
    - `env_energy`: environment/energy agencies and activity codes plus policy-relevant keywords, matched with `physics.ao-ph` / `physics.geo-ph` / `eess.SY` / `eess.SP` plus environment-energy keywords;
  - executed the notebook and verified that the resulting pilot tables were written into `data/processed/srmatcher.duckdb`;
  - updated `README.md` with the current EDA snapshot and pilot-domain counts.
- Result:
  - `grant` description quality is sufficient for text matching: raw missing rate is only `0.02%`, average non-empty length is `197.86` words, and `16.98%` are shorter than 50 words;
  - `arXiv` abstract quality is also strong: average length is `145.11` words and only `5.38%` are shorter than 50 words;
  - the pilot slices now have usable sizes within the `2005-2024` window:
    - grant: `cs` 6,739, `biomed` 29,966, `env_energy` 35,510;
    - arXiv: `cs` 726,273, `biomed` 125,208, `env_energy` 346,484;
  - the project is now ready for the next step: domain-wise temporal candidate-window construction followed by TF-IDF retrieval baselines.

### 2026-03-14 - Supplemented EDA Toward Chapter-Ready Analysis

- Purpose: strengthen Phase 1 so it can support a full thesis chapter instead of functioning only as a pre-modeling checklist.
- Change:
  - extended `code.ipynb` with a critical-field missingness table across both sides;
  - added `version_count` distribution analysis for arXiv revision behavior;
  - added domain-year heatmaps on top of the line plots for the three pilot slices;
  - added text-style comparison using sampled grant descriptions and arXiv abstracts:
    - top-term tables,
    - sentence-length and document-length summaries,
    - lexical-diversity proxy via type-token ratio,
    - top-term overlap check between the two sides;
  - reviewed the project roadmap HTML and aligned the notebook expansion with its Phase-1 requirements;
  - updated `README.md` to reflect the stronger EDA state and the fact that modeling should not start before the chapter-level interpretation is written down.
- Result:
  - the EDA now supports a more defensible standalone chapter structure: data overview, field quality, pilot slicing logic, temporal distribution, and cross-side text-style comparison;
  - matching-relevant metadata asymmetry is now explicit:
    - grant `cfda_numbers` missing rate is only `0.99%`,
    - arXiv `doi` missing rate is `56.65%`,
    - arXiv `journal_ref` missing rate is `68.79%`;
  - arXiv revision behavior is now characterized: `version_count = 1` dominates with `1,778,489` papers;
  - style comparison shows a real modeling risk:
    - grant descriptions are longer and more sentence-dense,
    - sampled top-term overlap between the two sides is extremely low, with only `data` shared in the top-20 vocabulary lists.

### 2026-03-13 - Added AGENTS.md Workflow Guardrails

- Purpose: add a durable operating guide so development stays aligned with branch scope, project-memory rules, and user-controlled git actions.
- Change:
  - created `AGENTS.md` with branch guardrails for `baseline`, `match`, and `analysis`;
  - added a status board to track the current branch stage and prevent accidental branch drift;
  - added explicit permission rules forbidding `git commit`, `git checkout`, `git switch`, or branch creation without Frankie's approval;
  - added a branch-transition reminder to recommend new branches from the current accepted branch tip instead of switching implicitly.
- Result:
  - the repository now has a local operating guide that can steer future turns and reduce workflow mistakes;
  - branch progression is now explicit and reviewable in-project;
  - git control remains with Frankie unless explicit permission is given.

### 2026-03-13 - Project Initialization and Branch Scope Lock

- Purpose: initialize the project memory files, formalize the branch strategy, and document the current baseline state before further development.
- Change:
  - added a project README with goals, branch boundaries, current pipeline scope, and current dataset snapshot;
  - initialized `REFERENCE.md` as the registry for externally grounded improvement attempts;
  - initialized `NoteOfChange.md` as the durable experiment/change log for substantive future work;
  - locked the branch strategy as `baseline` for EDA and TF-IDF baseline, `match` for matching-method improvement, and `analysis` for all step-3 analysis work.
- Result:
  - the repository now contains persistent project memory for future iterations;
  - the current baseline is explicitly documented as cleaned grant/arXiv tables plus the notebook TF-IDF baseline;
  - the branch boundary for step 3 is fixed to `analysis`, reducing ambiguity before pipeline expansion.
