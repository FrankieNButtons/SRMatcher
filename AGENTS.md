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

## Branch Guardrails

1. `baseline` is only for EDA, descriptive analysis, data cleaning, and TF-IDF baseline establishment.
2. `match` is only for improved matching-method development and comparison against the baseline.
3. `analysis` is only for step-3 analysis work after the preferred matching method is selected.
4. Do not drift backward into earlier-stage work once a branch has been declared complete without explicitly marking the regression in the status section below.
5. When the current branch task is judged complete, recommend creating the next branch from the current branch tip instead of silently continuing in the wrong branch.

## Permission Rules

1. Never run `git commit` without Frankie's explicit permission.
2. Never run `git checkout`, `git switch`, or create a new branch without Frankie's explicit permission.
3. Always leave commit execution to Frankie unless Frankie explicitly asks otherwise.
4. If a branch transition is the correct next step, state it clearly and stop short of executing it.

## Status Board

Update this section when branch scope changes or when a major stage is completed.

- Current expected branch: `baseline`
- Current stage: raw-text TF-IDF baseline built, evaluation and tuning preparation
- `baseline` status: in progress
- `match` status: not started
- `analysis` status: not started
- Branch transition rule: when `baseline` work is accepted, recommend branching `match` from the current `baseline` state; when matching work is accepted, recommend branching `analysis` from the accepted `match` state.
- Backtracking rule: if work needs to return to an earlier branch after completion, log the reason in `NoteOfChange.md` before proceeding.

## Current Project Context

1. The repository already contains raw data, cleaned DuckDB outputs, and a baseline notebook.
2. The current cleaned snapshot is:
   - `grant_clean`: 80,748 rows, 2004-03-22 to 2026-03-11;
   - `arxiv_clean`: 2,954,910 rows, 1995-01-01 to 2026-03-05.
3. `main.py` currently builds cleaned `grant_clean` and `arxiv_clean` tables.
4. `code.ipynb` currently covers Phase-1 EDA, pilot-domain review, side-specific stopword-candidate diagnosis, and the raw-text domain-wise TF-IDF baseline.

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
