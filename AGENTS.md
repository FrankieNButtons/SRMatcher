# SRMatcher Agent Operating Guide

## Purpose

This file is the working contract for Codex in the SRMatcher project. It exists to keep development disciplined across branches, preserve project memory, and prevent accidental regressions in workflow.

## Core Rules

1. Treat this project as graduation-paper work and keep decisions professional, explicit, and reproducible.
2. Read `NoteOfChange.md` whenever it is no longer in active context before making substantive changes.
3. Record every substantive improvement attempt in `NoteOfChange.md`, including:
   - the purpose of the attempt;
   - what was changed;
   - the observed result, even if the result is worse or inconclusive;
   - what future work should reuse or avoid.
4. If an improvement attempt depends on papers, benchmarks, datasets, or external methods:
   - add the source and URL to `REFERENCE.md`;
   - cite that source in `NoteOfChange.md`.
5. Do not record tiny bug-fix-only edits in `NoteOfChange.md` unless they materially affect results, interpretation, or pipeline behavior.
6. Treat `srmatcher_baseline_roadmap.svg` as a visual roadmap for the `baseline` branch when its phases are consistent with the written branch rules in this file.
7. Prefer extending `code.ipynb` with new self-contained sections instead of replacing or rewriting the notebook, unless Frankie explicitly asks for a notebook rewrite.

## Branch Guardrails

1. `baseline` is only for EDA, descriptive analysis, data cleaning, and TF-IDF baseline establishment.
2. `match` is only for improved matching-method development and comparison against the baseline.
3. `analysis` is only for step-3 analysis work after the preferred matching method is selected.
4. Do not drift backward into earlier-stage work once a branch has been declared complete without explicitly marking the regression in the status section below.
5. When the current branch task is judged complete, recommend creating the next branch from the current branch tip instead of silently continuing in the wrong branch.
6. Do not switch to `match` until the baseline exit gate defined below is fully satisfied.

## Baseline Ablation Strategy

1. Key principle: every baseline optimization step must become one row in a single ablation table, with an explicit configuration name, top-1 similarity, temporal coherence, and a short note.
2. Layer 1 is candidate-pool quality and must be completed before any Layer 2 text-representation experiment.
3. Do not start stopword, n-gram, or other text-representation tuning before Layer 1 is complete, because stopword-v1 has already shown that representation signals can be drowned out by a noisy candidate pool.
4. Layer 1 has three mandatory sub-experiments, and all three must be implemented in the same notebook section and compared together against the raw baseline:
   - `1a` language filter;
   - `1b` time window with `12`, `24`, and `36` month variants;
   - `1c` duplicate-candidate cap, defined as a global maximum of `K` appearances for the same `arxiv_id`.
5. Do not move to Layer 2 after only one or two of the Layer 1 experiments; Layer 1 is considered complete only when `1a`, `1b`, and `1c` have all been run and compared against the raw baseline.
6. Layer 2 is text-representation quality and must follow this exact order:
   - `2a` field combination;
   - `2b` stopword tuning;
   - `2c` hyperparameter and n-gram tuning.
7. Every Layer 2 step must be recorded in `NoteOfChange.md`, including negative results.
8. Stopword experiments are only meaningful after Layer 1 has cleaned the candidate pool.
9. Any stopword result obtained before Layer 1 completion must be treated only as a negative result under a dirty candidate pool, not as a final conclusion that stopwords are ineffective.
10. The `baseline` branch is complete if and only if all of the following are true:
   - `tfidf_baseline_final` has been written into DuckDB and is clearly distinct from `_raw`;
   - a locked golden set of `100` to `150` pairs exists, combining silver positives, cross-domain negatives, and human three-class labels;
   - `NoteOfChange.md` contains the full two-layer ablation record.
11. Before all three baseline exit conditions are satisfied, do not recommend or attempt a switch to the `match` branch.

## Baseline Temporal-Analysis Rules

The following rules refine the purpose and evaluation focus of the `baseline` branch and should take precedence if they conflict with an earlier interpretation that treats the task as unique-paper retrieval.

### Rule A: Task Framing

The core goal of this project is not to find one best unique paper for each grant. The core goal is to measure the temporal lag `Δt` between the appearance of a research topic on the academic side and the formation of a funding-side hotspot.

Therefore:
- the matching output unit is a set of high-similarity pairs, not only a top-1 hit;
- one grant matching to multiple highly similar papers is normal and expected;
- dup pool means that the same arXiv paper is selected as raw top-1 by `10` or more different grants, showing that this paper occupies an overly strong central position in the TF-IDF lexical space and causes many grants to converge onto it incorrectly.
- the reason `dup` often has negative `Δt` is that these lexically dominant papers are being mismatched to grants that already existed before the paper was published, so the signal is matching noise rather than a real temporal pattern.
- therefore the `dup` pool should:
  - be reported separately in the main `Δt` analysis rather than being mixed into the same mean as `raw` and `tw36`;
  - be treated as a diagnostic signal of TF-IDF candidate-pool quality rather than as an independent research finding;
  - be reduced in the `match` branch by better embedding-based methods that weaken this convergence effect;
- the main evaluation metrics for any ablation experiment should include `Δt` distribution features, including the median and distribution width, not only mean similarity or top-1 precision.

### Rule B: `Δt` Definition Must Be Locked During Baseline

Before entering the `match` branch, the following work must be completed inside the `baseline` branch and recorded in `NoteOfChange.md`:
- lock the `Δt` formula as `Δt = grant posted_date - arXiv submitted_date`;
- lock the method used to determine the similarity threshold for selecting valid pairs;
- run at least one full three-domain `Δt` distribution and report its median and percentiles;
- treat that distribution as the baseline comparison target for all later matching-method improvements.
- the `Δt` baseline must be locked and reported as two subgroups:
  - main distribution: `pool_used IN ('raw', 'tw36')`, representing valid temporal matching signal;
  - `dup` subgroup: reported separately as a candidate-pool quality diagnostic and not included in the main conclusion;
  mixed averages across the two subgroups must not be used as the primary basis for conclusions.

Before the work above is complete, do not recommend or attempt a switch to the `match` branch.

### Rule C: Golden-Set Positioning

The role of the golden set is to validate matching directionality, including temporal coherence and topic relevance, rather than to serve as an exact-retrieval ground truth.

Therefore:
- it is not required to be fully locked before Phase 3;
- its scale may be relaxed from `30` to `50` pairs per domain to `20` to `30` topic windows per domain;
- its annotation dimensions may be simplified to two binary judgments:
  - whether the temporal direction is correct,
  - whether the topic is relevant;
- its construction may proceed in parallel with the initial `Δt` analysis and should not be treated as the gating item for progress by itself.

## Permission Rules

1. Never run `git commit` without Frankie's explicit permission.
2. Never run `git checkout`, `git switch`, or create a new branch without Frankie's explicit permission.
3. Always leave commit execution to Frankie unless Frankie explicitly asks otherwise.
4. If a branch transition is the correct next step, state it clearly and stop short of executing it.

## Human-in-the-Loop Review Rule

1. Keep the project actively human-in-the-loop whenever a modeling, matching, labeling, or interpretation decision would benefit from human judgment.
2. Proactively offer review material instead of waiting for the user to ask if:
   - a baseline or new method has produced examples worth manual inspection;
   - the next decision depends on error taxonomy, relevance judgment, temporal plausibility, or qualitative interpretation;
   - a result could be misleading without direct reading of matched text.
3. Treat the current files under `review/` as examples of the mechanism, not the only allowed format.
4. Provide review material in the format that best fits the task, such as:
   - structured files under `review/`,
   - markdown summaries,
   - CSV tables,
   - notebook sections,
   - targeted example lists,
   - comparison tables,
   - concise review instructions embedded in the turn response.
5. Reuse an existing review artifact when it fits the current decision; otherwise create a new review format that better matches the task.
6. When asking for review, always tell the user:
   - what to review;
   - the review standard or rubric to use;
   - why the review matters for the next research decision;
   - what output or conclusion is expected from the review.
7. After producing review material, explicitly invite the user to complete the review before the next major modeling or analysis step when that review is decision-critical.

## Status Board

- Current expected branch: `match`
- Current stage: All baseline branch exit conditions have been satisfied and
  verified with statistical tests. The match branch has not yet been opened.
  Waiting for Frankie's explicit authorization to create the branch from the
  baseline tip.
  First task after branch creation: Section 19, embedding baseline.
  Inherit the tfidf_baseline_layer1_final candidate pool rules.
  Compare directly against TF-IDF baseline. Primary observations:
  whether dup % decreases and whether the main Δt distribution improves.
  Next notebook section number is 19.
- `baseline` status: complete
- `match` status: not yet opened — waiting for Frankie to create branch
  from baseline tip
- `analysis` status: not started
- Branch transition rule: open match branch from baseline tip, not from main;
  open analysis branch from match tip after match is complete.
- Backtracking rule: if regression is needed, record the reason in
  NoteOfChange.md before doing anything.

## Current Project Context

1. The repository already contains raw data, cleaned DuckDB outputs, and a baseline notebook.
2. The current cleaned snapshot is:
   - `grant_clean`: 80,748 rows, 2004-03-22 to 2026-03-11;
   - `arxiv_clean`: 2,954,910 rows, 1995-01-01 to 2026-03-05.
3. `main.py` currently builds cleaned `grant_clean` and `arxiv_clean` tables.
4. `code.ipynb` currently covers Phase-1 EDA, pilot-domain review, side-specific stopword-candidate diagnosis, the raw-text domain-wise TF-IDF baseline, and the full Layer 1 candidate-pool ablation.
5. `srmatcher_baseline_roadmap.svg` is an available visual roadmap for baseline-stage sequencing and exit criteria.
6. `srmatcher_match_roadmap.svg` is the visual roadmap for the match branch.
   It covers five phases: Phase A (embedding baseline, Section 19),
   Phase B (ablation experiments, Section 20), Phase C (golden set expansion,
   Section 21), Phase D (skill-aware hybrid, Section 22), and Phase E
   (handoff to analysis branch). If this SVG and the written rules in this
   file disagree, always follow the written rules and note the mismatch
   explicitly.

## Execution Preference

1. Before major work, restate the current branch scope and confirm the task fits it.
2. Before edits, check whether the change is:
   - a baseline/EDA task for `baseline`;
   - a matching-method task for `match`;
   - an analysis task for `analysis`.
3. After major work, state:
   - what changed;
   - whether `NoteOfChange.md` was updated;
   - whether the current branch should continue or a new branch should be created next.
4. When human judgment is the bottleneck, stop pushing the pipeline forward blindly and instead surface a concrete review mechanism with a scoring standard and a short explanation of the decision it will support.
5. On `baseline`, always frame the next experiment as the next row of the ablation table rather than as an isolated tweak.
6. On notebook work, prefer adding a new section that reuses existing tables and earlier notebook context rather than replacing existing notebook structure.
7. If the SVG roadmap and the written rules disagree, follow the written rules and note the mismatch explicitly.
8. The next notebook section number is 19. Do not use any other number for
   the first match-branch section unless you have first read code.ipynb and
   confirmed that Section 19 already exists.
