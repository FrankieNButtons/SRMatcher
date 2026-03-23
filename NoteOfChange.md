# Note Of Change

This file records substantive project edits, their purpose, and their observed result so future iterations can reuse good directions and avoid repeated mistakes.

## Logging Rule

- Record meaningful improvement attempts, pipeline changes, evaluation changes, and analysis-direction changes.
- Skip tiny bug fixes unless they materially affect results or interpretation.
- When a change is based on external sources, add the source to `REFERENCE.md` and cite it here.

## Entries

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
