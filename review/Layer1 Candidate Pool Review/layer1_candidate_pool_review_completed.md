# Layer 1 candidate-pool review — completed

## What was added

- `layer1_preferred_pool`: manual choice among `raw`, `lang`, `tw36`, `dup`, or `none`.
- `layer1_manual_decision_note`: row-level hand-check note explaining the decision.
- `layer1_preferred_*`: the selected top-1 paper/id/similarity/lag copied out for downstream use.

## Aggregate counts

- `none`: 4
- `raw`: 32
- `tw36`: 14
- `dup`: 10

## Row-by-row decisions

- `BIOMED_01` → `none`: language filter removes the French-spanish noise path, but no alternative candidate is actually on-topic; keep this row out rather than promote tw36.
- `BIOMED_02` → `raw`: Raw/lang are the strongest semantic fit on RWD→RWE; tw36 is more generic and weaker.
- `BIOMED_03` → `tw36`: tw36 is still COVID-focused and has much better temporal plausibility than the later review-style raw hit.
- `BIOMED_04` → `tw36`: Same reasoning as BIOMED_03; tw36 is the better Layer-1 top-1 once time direction matters.
- `BIOMED_05` → `raw`: tw36 drifts off PKD entirely; raw is weak but still the only disease-specific candidate.
- `BIOMED_06` → `tw36`: tw36 stays on RWD/RWE and avoids the over-used rare-disease review, so it is the better candidate-pool control.
- `BIOMED_07` → `tw36`: tw36 is on-topic and less duplicate-prone than the recurring raw review paper.
- `BIOMED_08` → `none`: All variants are off-topic ML-in-Spanish; this row should be excluded from downstream evaluation.
- `BIOMED_09` → `raw`: Raw/lang are exactly about syndromic surveillance; tw36 is a false friend based on 'syndromic'.
- `BIOMED_10` → `raw`: Raw is not perfect but clearly closer than the broader neurodegenerative time-series tw36 candidate.
- `BIOMED_11` → `raw`: Raw remains the only coral-reef assessment/annotation bridge; tw36 is generic ecology drift.
- `BIOMED_12` → `raw`: Raw fits RSV surveillance/epidemiology better; tw36 is narrower and more indirect.
- `BIOMED_13` → `raw`: Raw keeps the disease match; tw36 is clearly off-topic.
- `BIOMED_14` → `raw`: All variants collapse to the same excellent HIV-bNAb escape paper; keep raw.
- `BIOMED_15` → `raw`: Raw is still the most usable reef-monitoring method proxy; tw36 is looser on site monitoring.
- `BIOMED_16` → `raw`: Raw is a real SGM-methods match; tw36 is unrelated biology wording.
- `BIOMED_17` → `raw`: Raw directly addresses quantifying the latent HIV reservoir and is better than the older dynamic-model tw36 option.
- `BIOMED_18` → `dup`: Semantically the same as raw, but for the duplicated R01/R21 pair the duplicate-cap path is preferable for downstream uniqueness.
- `BIOMED_19` → `raw`: Raw is almost exact on SIT for mosquito control; tw36 shifts toward Zika rather than SIT.
- `BIOMED_20` → `raw`: Raw is the intended genomic-variation/function agenda match; tw36 is only one technical subproblem.
- `CS_01` → `raw`: Explainable Security is imperfect but still much closer to XAI than the awkward tw36 alternative.
- `CS_02` → `tw36`: Both are relevant, but tw36 is more directly about LIGO search capability than the PRIMAD workflow-reproducibility angle.
- `CS_03` → `dup`: To avoid repeating the same LIGO paper across duplicate grant rows, prefer the duplicate-controlled pool for this row.
- `CS_04` → `tw36`: tw36 is a cleaner lake/water-temperature ecosystem modeling match than the reservoir-release operations paper.
- `CS_05` → `raw`: Raw is directly about docking-based virtual screening, which is nearer to the FOA than the broad review tw36.
- `CS_06` → `tw36`: For the broad CESU ecosystem call, tw36 is a slightly better thematic fit on monitoring water temperature and quality in lakes.
- `CS_07` → `raw`: Raw stays inside ARL cyber programs and is more defensible than the generic military decision-support tw36 hit.
- `CS_08` → `raw`: Synthetic homology in HoTT is a legitimate topology-family match; tw36 is farther away.
- `CS_09` → `raw`: Raw is a more concrete humanities-collections R&D match than the linked-data infrastructure tw36 item.
- `CS_10` → `dup`: Content is good either way, but this grant line is a near-repeat; prefer duplicate control for downstream de-redundancy.
- `CS_11` → `dup`: Same as CS_10: use duplicate-controlled pool to avoid another identical cultural-heritage repeat.
- `CS_12` → `raw`: Raw is almost exact on randomized algorithms for scientific computing; tw36 is clearly off-topic.
- `CS_13` → `raw`: All variants are the same broad ARL cyber overview; keep raw.
- `CS_14` → `none`: Neither raw nor tw36 is really about English-language teaching; better to mark as no acceptable Layer-1 candidate.
- `CS_15` → `raw`: Raw is an exact STT-RAM technical match; tw36 is generic RAM testing.
- `CS_16` → `raw`: Raw at least keeps coral-reef image-analysis alignment; tw36 is nonsense here.
- `CS_17` → `raw`: Raw directly names UAS airspace integration and is clearly the right choice.
- `CS_18` → `tw36`: Both are on-topic, but tw36 improves temporal plausibility while staying within multi-messenger astrophysics.
- `CS_19` → `raw`: All variants are the same RASC paper; keep raw despite the temporal awkwardness.
- `CS_20` → `raw`: Raw is the better combinatorics match; tw36 drops algebra/number-theory breadth.
- `ENV_ENERGY_01` → `dup`: This is a duplicate of the RASC theme elsewhere, so the duplicate-controlled pool is preferable.
- `ENV_ENERGY_02` → `raw`: Raw is strongly about methane hydrates; tw36 is also relevant but less complete.
- `ENV_ENERGY_03` → `raw`: Raw is the stronger stem-cells-and-cancer match; tw36 narrows to a specific brain-tumor simulation.
- `ENV_ENERGY_04` → `dup`: Another repeated RASC hit; prefer duplicate control for uniqueness.
- `ENV_ENERGY_05` → `tw36`: tw36 is more directly about harmful algal blooms themselves, whereas raw is a specialized tracking-control method.
- `ENV_ENERGY_06` → `raw`: Raw is tightly tied to the named system-analysis context; tw36 is only loosely adjacent nuclear-waste instrumentation.
- `ENV_ENERGY_07` → `tw36`: For an older reef-program row, tw36 keeps coral-reef science while moving away from the over-repeated computer-vision paper.
- `ENV_ENERGY_08` → `raw`: Raw is at least about monarch population dynamics; tw36 is too generic.
- `ENV_ENERGY_09` → `tw36`: tw36 finally gets the UAS operational side, while raw is about counter-UAS defense and is a scope miss.
- `ENV_ENERGY_10` → `tw36`: Given the heavy repetition of the reef CV paper, tw36 is the more acceptable 2018-specific candidate.
- `ENV_ENERGY_11` → `tw36`: Same reef-family logic: tw36 gives a distinct coral-reef-science paper and reduces repetition.
- `ENV_ENERGY_12` → `tw36`: tw36 is both coral-specific and temporally reasonable for the 2021 row, so it beats the repeated raw paper.
- `ENV_ENERGY_13` → `raw`: tw36 drifts into statistical clustering; raw remains the better 2022 coral-program match.
- `ENV_ENERGY_14` → `dup`: Among the alternatives, dup at least stays on coral-reef recovery science; raw is an over-repeated and temporally stretched reef CV hit.
- `ENV_ENERGY_15` → `dup`: Same as ENV_ENERGY_14: duplicate-controlled pool yields a more distinct reef-science candidate.
- `ENV_ENERGY_16` → `raw`: For the 2023 reef row, raw is one of the best and most timely matches in the family.
- `ENV_ENERGY_17` → `none`: Both raw and tw36 are unrelated to clean energy activities; exclude this row.
- `ENV_ENERGY_18` → `dup`: For the 2024 reef call, dup improves temporal plausibility relative to the older raw paper while staying reef-specific.
- `ENV_ENERGY_19` → `raw`: Raw is delightfully exact on the DARPA SubT Challenge; tw36 is unrelated.
- `ENV_ENERGY_20` → `dup`: For the older 2017 reef program, dup is the more distinct reef-science choice versus the repeated raw CV paper.