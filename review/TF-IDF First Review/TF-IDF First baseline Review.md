# Top-1 高分配对人工误差分析记录

## 用途

这份文档抽取了 `tfidf_baseline_matches_raw` 中每个 pilot domain 的 top-1 结果里相似度最高的 20 对，共 60 对，用于人工阅读和误差分析。目标不是马上下结论，而是帮助你判断 TF-IDF 当前主要是抓住了主题、文体、机构术语，还是时间上真正可解释的研究需求关联。

## 建议标注口径

- `主题相关性`：1 到 5 分，判断 grant 与 paper 是否确实讨论同一问题域。
- `细粒度匹配度`：1 到 5 分，判断两者是否不只是同一大领域，而是具体问题也接近。
- `时序合理性`：1 到 5 分，判断这对配对在时间上是否能支持后续的需求-供给解释。
- `总体判断`：推荐填 `强相关`、`部分相关`、`弱相关`、`明显错配`。
- `主要误差类型`：可填 `泛词重叠`、`机构/公告腔干扰`、`领域过粗`、`时序反转`、`主题相邻但不一致`、`其他`。
- `是否保留为后续评估样本`：推荐填 `保留` 或 `不保留`。

## 示例填写

下面是建议填写格式，内容只是示范格式，不代表最终判定。

| review_id | 主题相关性 | 细粒度匹配度 | 时序合理性 | 总体判断 | 主要误差类型 | 是否保留为后续评估样本 | 评语 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CS_XX` | 4 | 3 | 1 | 部分相关 | 时序反转；泛词重叠 | 不保留 | 主题上都与可解释性相关，但论文发布时间晚于 grant，且匹配主要依赖通用术语。 |

## 抽样概览

| domain | 配对数 | arXiv 早于或同日的数量 | 平均相似度 | 最低相似度 | 最高相似度 |
| --- | --- | --- | --- | --- | --- |
| `biomed` | 20 | 3 | 0.4598 | 0.4233 | 0.5388 |
| `cs` | 20 | 3 | 0.4024 | 0.3723 | 0.4706 |
| `env_energy` | 20 | 4 | 0.4095 | 0.3989 | 0.4391 |

## 汇总评价表

| review_id | domain | similarity | lag_days | opportunity_id | arxiv_id | grant_title | paper_title | 主题相关性 | 细粒度匹配度 | 时序合理性 | 总体判断 | 主要误差类型 | 是否保留为后续评估样本 | 评语 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BIOMED_01` | `biomed` | 0.5388 | 4807 | `355954` | `1106.2206` | Suivi communautaire des Programmes et Politiques... | Nanomaterials : a review of the definitions,... |  |  |  |  |  |  |  |
| `BIOMED_02` | `biomed` | 0.5259 | -666 | `344521` | `2410.06586` | Supporting the use of Real-World Data to Generate Real-... | Use of Real-World Data and Real-World Evidence in Rare... |  |  |  |  |  |  |  |
| `BIOMED_03` | `biomed` | 0.4965 | -307 | `326652` | `2103.02723` | Emergency Awards: Rapid Investigation of Severe Acute... | Identification and Development of Therapeutics for COVID-19 |  |  |  |  |  |  |  |
| `BIOMED_04` | `biomed` | 0.4955 | -307 | `326664` | `2103.02723` | Emergency Awards: Rapid Investigation of Severe Acute... | Identification and Development of Therapeutics for COVID-19 |  |  |  |  |  |  |  |
| `BIOMED_05` | `biomed` | 0.4896 | -3375 | `257130` | `2309.03033` | Polycystic Kidney Disease (PKD) Research and Translation... | Deep Learning for Polycystic Kidney Disease: Utilizing... |  |  |  |  |  |  |  |
| `BIOMED_06` | `biomed` | 0.4864 | -1233 | `324928` | `2410.06586` | Exploring the use of Real-World Data to Generate Real-... | Use of Real-World Data and Real-World Evidence in Rare... |  |  |  |  |  |  |  |
| `BIOMED_07` | `biomed` | 0.4725 | -1668 | `325478` | `2410.06586` | Exploring the use of Real-World Data to Generate Real-... | Use of Real-World Data and Real-World Evidence in Rare... |  |  |  |  |  |  |  |
| `BIOMED_08` | `biomed` | 0.4578 | 500 | `339641` | `2012.03188` | RFI - HIV Care and Treatment | Representaciones del aprendizaje reutilizando los... |  |  |  |  |  |  |  |
| `BIOMED_09` | `biomed` | 0.4552 | -1821 | `281308` | `2101.12246` | The National Syndromic Surveillance Program: Enhancing... | Revisiting Non-Specific Syndromic Surveillance |  |  |  |  |  |  |  |
| `BIOMED_10` | `biomed` | 0.4511 | -3451 | `271457` | `2406.18625` | Analyze and Evaluate Potential Risk Factors for... | Automatic Prediction of Amyotrophic Lateral Sclerosis... |  |  |  |  |  |  |  |
| `BIOMED_11` | `biomed` | 0.4487 | -3115 | `284301` | `2412.08228` | Coral Reef Assessment at Ritidan Unit, Guam NWR | Hierarchical Classification for Automated Image... |  |  |  |  |  |  |  |
| `BIOMED_12` | `biomed` | 0.4478 | -876 | `308248` | `2103.12808` | Surveillance for Respiratory Syncytial Virus (RSV) and... | Use of mathematical modelling to assess respiratory... |  |  |  |  |  |  |  |
| `BIOMED_13` | `biomed` | 0.4365 | -1021 | `316721` | `2203.11391` | Advancing Novel Research Models to Study Idiopathic... | Survival Analysis for Idiopathic Pulmonary Fibrosis using... |  |  |  |  |  |  |  |
| `BIOMED_14` | `biomed` | 0.4326 | 236 | `332448` | `2008.02547` | Mechanisms of HIV Resistance to Broadly Neutralizing... | Predicting in vivo escape dynamics of HIV-1 from a... |  |  |  |  |  |  |  |
| `BIOMED_15` | `biomed` | 0.4323 | -2350 | `306843` | `2412.08228` | Long Term Monitoring of Selected Coral Reef Sites in Dry... | Hierarchical Classification for Automated Image... |  |  |  |  |  |  |  |
| `BIOMED_16` | `biomed` | 0.4300 | -1582 | `323257` | `2405.02322` | Methods and Measurement in Research with Sexual and... | Towards Causal Interpretation of Sexual Orientation in... |  |  |  |  |  |  |  |
| `BIOMED_17` | `biomed` | 0.4256 | -3141 | `258689` | `2302.00516` | Innovative Assays to Quantify the Latent HIV Reservoir (R01) | Quantifying the HIV reservoir with dilution assays and... |  |  |  |  |  |  |  |
| `BIOMED_18` | `biomed` | 0.4250 | -3502 | `237021` | `2302.00516` | Innovative Assays to Quantify the Latent HIV Reservoir (R21) | Quantifying the HIV reservoir with dilution assays and... |  |  |  |  |  |  |  |
| `BIOMED_19` | `biomed` | 0.4244 | -669 | `286518` | `1805.10150` | IAEA Project Surge Expansion of Sterile Insect Technique... | On the use of the sterile insect technique or the... |  |  |  |  |  |  |  |
| `BIOMED_20` | `biomed` | 0.4233 | -1085 | `328538` | `2307.13708` | Systematic Characterization of Genomic Variation on... | The Impact of Genomic Variation on Function (IGVF)... |  |  |  |  |  |  |  |
| `CS_01` | `cs` | 0.4706 | -700 | `287284` | `1807.04178` | Explainable Artificial Intelligence (XAI) | Explainable Security |  |  |  |  |  |  |  |
| `CS_02` | `cs` | 0.4471 | -3669 | `46271` | `1904.05211` | Gravitational Physics | Applicability study of the PRIMAD model to LIGO... |  |  |  |  |  |  |  |
| `CS_03` | `cs` | 0.4471 | -2889 | `93899` | `1904.05211` | Gravitational Physics | Applicability study of the PRIMAD model to LIGO... |  |  |  |  |  |  |  |
| `CS_04` | `cs` | 0.4348 | -233 | `334291` | `2202.05714` | Cooperative Agreement for CESU-affiliated Partner with... | Modeling Reservoir Release Using Pseudo-Prospective... |  |  |  |  |  |  |  |
| `CS_05` | `cs` | 0.4166 | -3074 | `236600` | `2111.09502` | Drug Docking and Screening Data Resource (U01) | Docking-based Virtual Screening with Multi-Task Learning |  |  |  |  |  |  |  |
| `CS_06` | `cs` | 0.4145 | -543 | `328715` | `2202.05714` | Cooperative Ecosystem Studies Unit, Great Lakes Northern... | Modeling Reservoir Release Using Pseudo-Prospective... |  |  |  |  |  |  |  |
| `CS_07` | `cs` | 0.3985 | -1391 | `227155` | `1702.04652` | Cyber Security (CS) Collaborative Research Alliance (CRA)... | Overview of Cyber Science and Technology Programs at the... |  |  |  |  |  |  |  |
| `CS_08` | `cs` | 0.3956 | -2995 | `46298` | `1706.01540` | Topology | Synthetic Homology in Homotopy Type Theory |  |  |  |  |  |  |  |
| `CS_09` | `cs` | 0.3942 | -2735 | `274934` | `2208.13512` | Research and Development | Labeling of Cultural Heritage Collections on the... |  |  |  |  |  |  |  |
| `CS_10` | `cs` | 0.3942 | -2324 | `283061` | `2208.13512` | Research and Development | Labeling of Cultural Heritage Collections on the... |  |  |  |  |  |  |  |
| `CS_11` | `cs` | 0.3942 | -1981 | `292772` | `2208.13512` | Research and Development | Labeling of Cultural Heritage Collections on the... |  |  |  |  |  |  |  |
| `CS_12` | `cs` | 0.3921 | -24 | `332386` | `2104.11079` | EXPRESS: Randomized Algorithms for Extreme-Scale Science | Randomized Algorithms for Scientific Computing (RASC) |  |  |  |  |  |  |  |
| `CS_13` | `cs` | 0.3915 | 59 | `292214` | `1702.04652` | Internet of Battlefield Things (IoBT) Collaborative... | Overview of Cyber Science and Technology Programs at the... |  |  |  |  |  |  |  |
| `CS_14` | `cs` | 0.3850 | -1841 | `293111` | `2204.11461` | Civic and Tech through English Language (CTEL) | A Review of Research on Civic Technology: Definitions,... |  |  |  |  |  |  |  |
| `CS_15` | `cs` | 0.3836 | -1443 | `40833` | `1202.1782` | Spin Torque Transfer-Random Access Memory (STT-RAM) | Cross-point architecture for spin transfer torque... |  |  |  |  |  |  |  |
| `CS_16` | `cs` | 0.3808 | -4798 | `121133` | `2410.20436` | Coral Reef Conservation Program International Coral Reef... | CoralSCOP-LAT: Labeling and Analyzing Tool for Coral Reef... |  |  |  |  |  |  |  |
| `CS_17` | `cs` | 0.3803 | -3031 | `261268` | `2211.15330` | Unmanned Aircraft System (UAS) Airspace Integration | UAS in the Airspace: A Review on Integration, Simulation,... |  |  |  |  |  |  |  |
| `CS_18` | `cs` | 0.3797 | 1362 | `349929` | `1911.11779` | WINDOWS ON THE UNIVERSE: THE ERA OF MULTI-MESSENGER... | Enabling real-time multi-messenger astrophysics... |  |  |  |  |  |  |  |
| `CS_19` | `cs` | 0.3741 | 360 | `339438` | `2104.11079` | Randomized Algorithms for Combinatorial Scientific Computing | Randomized Algorithms for Scientific Computing (RASC) |  |  |  |  |  |  |  |
| `CS_20` | `cs` | 0.3723 | -5105 | `46296` | `2303.09603` | Algebra, Number Theory, and Combinatorics | Rigorous Analytic Combinatorics in Several Variables in... |  |  |  |  |  |  |  |
| `ENV_ENERGY_01` | `env_energy` | 0.4391 | -24 | `332386` | `2104.11079` | EXPRESS: Randomized Algorithms for Extreme-Scale Science | Randomized Algorithms for Scientific Computing (RASC) |  |  |  |  |  |  |  |
| `ENV_ENERGY_02` | `env_energy` | 0.4293 | -3530 | `233281` | `2301.01756` | FY 2013 Methane Hydrates | Dynamic Viscosity of Methane and Carbon Dioxide Hydrate... |  |  |  |  |  |  |  |
| `ENV_ENERGY_03` | `env_energy` | 0.4271 | -3299 | `44089` | `1705.05025` | Stem Cells and Cancer (R21) | Complexity in cancer stem cells and tumor evolution:... |  |  |  |  |  |  |  |
| `ENV_ENERGY_04` | `env_energy` | 0.4194 | 360 | `339438` | `2104.11079` | Randomized Algorithms for Combinatorial Scientific Computing | Randomized Algorithms for Scientific Computing (RASC) |  |  |  |  |  |  |  |
| `ENV_ENERGY_05` | `env_energy` | 0.4141 | -3159 | `55983` | `1903.05993` | Harmful Algal Bloom Programs | Cooperative decentralized circumnavigation with... |  |  |  |  |  |  |  |
| `ENV_ENERGY_06` | `env_energy` | 0.4126 | -883 | `336125` | `2403.09848` | Staff Support for Regional State Engagement with the U.S.... | Implementation of Parallel Process Execution in the Next... |  |  |  |  |  |  |  |
| `ENV_ENERGY_07` | `env_energy` | 0.4099 | -1149 | `321621` | `2212.04132` | Coral Reef and Natural Resources Program | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_08` | `env_energy` | 0.4059 | 1879 | `291618` | `1112.3991` | Cooperative Ecosystem Studies Unit (CESU), Rocky Mountain... | Short and Long Range Population Dynamics of the Monarch |  |  |  |  |  |  |  |
| `ENV_ENERGY_09` | `env_energy` | 0.4040 | -2209 | `261549` | `2008.12461` | BLM&apos;s Unmanned Aircraft Systems (UAS) Resource... | Counter-Unmanned Aircraft System(s) (C-UAS): State of the... |  |  |  |  |  |  |  |
| `ENV_ENERGY_10` | `env_energy` | 0.4039 | -1648 | `305874` | `2212.04132` | Coral Reef and Natural Resources Program 2018 | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_11` | `env_energy` | 0.4038 | -1371 | `313593` | `2212.04132` | Coral Reef and Natural Resources Program 2019 | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_12` | `env_energy` | 0.4035 | -702 | `330685` | `2212.04132` | Coral Reef and Natural Resources Program 2021 | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_13` | `env_energy` | 0.4034 | -373 | `336758` | `2212.04132` | OIA Coral Reef and Natural Resources Program 2022 | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_14` | `env_energy` | 0.4033 | -2858 | `273729` | `2212.04132` | Coral Reef Initiative Program | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_15` | `env_energy` | 0.4033 | -2547 | `280623` | `2212.04132` | Coral Reef Initiative Program | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_16` | `env_energy` | 0.4030 | -66 | `343884` | `2212.04132` | OIA Coral Reef and Natural Resources Program 2023 | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_17` | `env_energy` | 0.4026 | 2592 | `249237` | `physics/0611083` | Clean Energy Activities- Addendum under APS No.: APS-... | Fractal Dimensionof the El Salvador Earthquake (2001)... |  |  |  |  |  |  |  |
| `ENV_ENERGY_18` | `env_energy` | 0.4023 | 322 | `350746` | `2212.04132` | OIA Coral Reef and Natural Resources Program 2024 | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |
| `ENV_ENERGY_19` | `env_energy` | 0.4015 | -1628 | `300280` | `2207.04914` | DARPA Subterranean (SubT) Challenge | Team CERBERUS Wins the DARPA Subterranean Challenge:... |  |  |  |  |  |  |  |
| `ENV_ENERGY_20` | `env_energy` | 0.3989 | -2170 | `290986` | `2212.04132` | Coral Reef Initiative Program 2017 | Combining Photogrammetric Computer Vision and Semantic... |  |  |  |  |  |  |  |

## 详细阅读卡片

### biomed

#### BIOMED_01

- 相似度：`0.5388`
- 时间差：`4807` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`355954` / 2024-08-08
- arXiv：`1106.2206` / 2011-06-11
- Grant 标题：Suivi communautaire des Programmes et Politiques li&#233;s au VIH
- Paper 标题：Nanomaterials : a review of the definitions, applications, health effects. How to implement secure development Nanomat\'eriaux : une revue des d\'efinitions, des applications, des effets sanitaires et des moyens \`a mettre en oeuvre pour un d\'eveloppement s\'ecuris\'e

**Grant Description**

Le maintien en vie des personnes vivant avec le VIH (PVVIH) sous traitement antirétroviral (ARV) reste un défi pour atteindre les objectifs 95-95-95 de l'ONUSIDA.L'initiative de Suivi Communautaire/The Community-Led Monitoring (CLM) vise à aider les programmes et les établissements du Plan d'urgence du Président des États-Unis d'Amérique pour la lutte contre le SIDA (U.S. President's Emergency Plan for AIDS Relief PEPFAR) à s'assurer qu'ils fournissent des services de qualité que les bénéficiaires souhaitent utiliser en collaboration avec les organisations communautaires et leurs pairs navigateurs. La collaboration avec les groupes communautaires, les organisations de la société civile et les patients/bénéficiaires peut aider les programmes de lutte contre le VIH et les institutions de santé à identifier les obstacles et les leviers pour faciliter l'accès et l'utilisation des services de lutte contre le VIH et à améliorer la rétention.

**arXiv Abstract**

Nanomaterials are an active area of research but also an economic sector in full expansion which addresses many applications domains. For instance, french production for the most common nanomaterials (such as silica, titanium dioxide, carbon black) is in the hundreds of thousands of tons. As for any innovation, one must consider the risks and, if necessary, establish rules to protect consumer health and that of the worker. This paper addresses in particular difficulties in defining these materials, the state of knowledge on human or environmental toxicity and requirements and agencies in charge of safety.---Les nanomat\'eriaux repr\'esentent un domaine de recherche actif mais aussi un secteur \'economique en pleine expansion en vue de nombreuses applications. Par exemple la production fran\c{c}aise pour les mat\'eriaux les plus courants (comme la silice, le dioxyde de titane, le noir de carbone) se chiffre en centaines de milliers de tonnes. Comme c'est le cas pour toute innovation, il convient de s'interroger sur les risques et, si n\'ecessaire, de fixer des r\`egles pour prot\'eger la sant\'e du consommateur et celle du travailleur. On discute en particulier les difficult\'es pour d\'efinir ces mat\'eriaux, de l'\'etat des connaissances en mati\`ere de toxicit\'e humaine ou environnementale et des prescriptions des agences en mati\`ere de s\'ecurit\'e.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_02

- 相似度：`0.5259`
- 时间差：`-666` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`344521` / 2022-12-13
- arXiv：`2410.06586` / 2024-10-09
- Grant 标题：Supporting the use of Real-World Data to Generate Real-World Evidence in Regulatory Decision-Making (U01) Clinical Trials Optional
- Paper 标题：Use of Real-World Data and Real-World Evidence in Rare Disease Drug Development: A Statistical Perspective

**Grant Description**

The purpose of this Funding Opportunity Announcement (FOA) is to address topics related to FDA's Real-World Evidence (RWE) Program and to enable FDA to assess the potential utility of real-world data (RWD) in generating RWE.

**arXiv Abstract**

Real-world data (RWD) and real-world evidence (RWE) have been increasingly used in medical product development and regulatory decision-making, especially for rare diseases. After outlining the challenges and possible strategies to address the challenges in rare disease drug development (see the accompanying paper), the Real-World Evidence (RWE) Scientific Working Group of the American Statistical Association Biopharmaceutical Section reviews the roles of RWD and RWE in clinical trials for drugs treating rare diseases. This paper summarizes relevant guidance documents and frameworks by selected regulatory agencies and the current practice on the use of RWD and RWE in natural history studies and the design, conduct, and analysis of rare disease clinical trials. A targeted learning roadmap for rare disease trials is described, followed by case studies on the use of RWD and RWE to support a natural history study and marketing applications in various settings.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_03

- 相似度：`0.4965`
- 时间差：`-307` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`326652` / 2020-04-30
- arXiv：`2103.02723` / 2021-03-03
- Grant 标题：Emergency Awards: Rapid Investigation of Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2) and Coronavirus Disease 2019 (COVID-19) (R01 Clinical Trial Not Allowed)
- Paper 标题：Identification and Development of Therapeutics for COVID-19

**Grant Description**

The purpose of this Funding Opportunity Announcement (FOA) is to provide an expedited (rapid) funding mechanism for research on Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2) and Coronavirus Disease 2019 (COVID-19).

**arXiv Abstract**

After emerging in China in late 2019, the novel Severe acute respiratory syndrome-like coronavirus 2 (SARS-CoV-2) spread worldwide and as of early 2021, continues to significantly impact most countries. Only a small number of coronaviruses are known to infect humans, and only two are associated with the severe outcomes associated with SARS-CoV-2: Severe acute respiratory syndrome-related coronavirus, a closely related species of SARS-CoV-2 that emerged in 2002, and Middle East respiratory syndrome-related coronavirus, which emerged in 2012. Both of these previous epidemics were controlled fairly rapidly through public health measures, and no vaccines or robust therapeutic interventions were identified. However, previous insights into the immune response to coronaviruses gained during the outbreaks of severe acute respiratory syndrome (SARS) and Middle East respiratory syndrome (MERS) have proved beneficial to identifying approaches to the treatment and prophylaxis of novel coronavirus disease 2019 (COVID-19). A number of potential therapeutics against SARS-CoV-2 and the resultant COVID-19 illness were rapidly identified, leading to a large number of clinical trials investigating a variety of possible therapeutic approaches being initiated early on in the pandemic. As a result, a small number of therapeutics have already been authorized by regulatory agencies such as the Food and Drug Administration (FDA) in the United States, and many other therapeutics remain under investigation. Here, we describe a range of approaches for the treatment of COVID-19, along with their proposed mechanisms of action and the current status of clinical investigation into each candidate. The status of these investigations will continue to evolve, and this review will be updated as progress is made.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_04

- 相似度：`0.4955`
- 时间差：`-307` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`326664` / 2020-04-30
- arXiv：`2103.02723` / 2021-03-03
- Grant 标题：Emergency Awards: Rapid Investigation of Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2) and Coronavirus Disease 2019 (COVID-19) (R21 Clinical Trial Not Allowed)
- Paper 标题：Identification and Development of Therapeutics for COVID-19

**Grant Description**

The purpose of this Funding Opportunity Announcement (FOA) is to provide an expedited (rapid) funding mechanism for research on Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2) and Coronavirus Disease 2019 (COVID-19).

**arXiv Abstract**

After emerging in China in late 2019, the novel Severe acute respiratory syndrome-like coronavirus 2 (SARS-CoV-2) spread worldwide and as of early 2021, continues to significantly impact most countries. Only a small number of coronaviruses are known to infect humans, and only two are associated with the severe outcomes associated with SARS-CoV-2: Severe acute respiratory syndrome-related coronavirus, a closely related species of SARS-CoV-2 that emerged in 2002, and Middle East respiratory syndrome-related coronavirus, which emerged in 2012. Both of these previous epidemics were controlled fairly rapidly through public health measures, and no vaccines or robust therapeutic interventions were identified. However, previous insights into the immune response to coronaviruses gained during the outbreaks of severe acute respiratory syndrome (SARS) and Middle East respiratory syndrome (MERS) have proved beneficial to identifying approaches to the treatment and prophylaxis of novel coronavirus disease 2019 (COVID-19). A number of potential therapeutics against SARS-CoV-2 and the resultant COVID-19 illness were rapidly identified, leading to a large number of clinical trials investigating a variety of possible therapeutic approaches being initiated early on in the pandemic. As a result, a small number of therapeutics have already been authorized by regulatory agencies such as the Food and Drug Administration (FDA) in the United States, and many other therapeutics remain under investigation. Here, we describe a range of approaches for the treatment of COVID-19, along with their proposed mechanisms of action and the current status of clinical investigation into each candidate. The status of these investigations will continue to evolve, and this review will be updated as progress is made.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_05

- 相似度：`0.4896`
- 时间差：`-3375` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`257130` / 2014-06-10
- arXiv：`2309.03033` / 2023-09-06
- Grant 标题：Polycystic Kidney Disease (PKD) Research and Translation Core Centers (P30)
- Paper 标题：Deep Learning for Polycystic Kidney Disease: Utilizing Neural Networks for Accurate and Early Detection through Gene Expression Analysis

**Grant Description**

This Funding Opportunity Announcement (FOA) invites applications for Polycystic Kidney Disease (PKD) Research and Translation Core Centers to support both basic and clinical research on PKD.

**arXiv Abstract**

With Polycystic Kidney Disease (PKD) potentially leading to fatal complications in patients due to the formation of cysts in kidneys, early detection of PKD is crucial for effective management of the condition. However, the various patient-specific factors that play a role in the diagnosis make it an intricate puzzle for clinicians to solve, leading to possible kidney failure. Therefore, in this study we aim to utilize a deep learning-based approach for early disease detection through gene expression analysis. The devised neural network is able to achieve accurate and robust prediction results for possible PKD in kidneys, thereby improving patient outcomes. Furthermore, by conducting a gene ontology analysis, we were able to predict the top gene processes and functions that PKD may affect.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_06

- 相似度：`0.4864`
- 时间差：`-1233` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`324928` / 2021-05-25
- arXiv：`2410.06586` / 2024-10-09
- Grant 标题：Exploring the use of Real-World Data to Generate Real-World Evidence in Regulatory Decision-Making (U01) Clinical Trials Optional
- Paper 标题：Use of Real-World Data and Real-World Evidence in Rare Disease Drug Development: A Statistical Perspective

**Grant Description**

To support research projects that examine real-world data (RWD), real-world evidence (RWE), and related issues such as data analytics, the use of digital health tools, and innovative trial designs utilizing healthcare settings

**arXiv Abstract**

Real-world data (RWD) and real-world evidence (RWE) have been increasingly used in medical product development and regulatory decision-making, especially for rare diseases. After outlining the challenges and possible strategies to address the challenges in rare disease drug development (see the accompanying paper), the Real-World Evidence (RWE) Scientific Working Group of the American Statistical Association Biopharmaceutical Section reviews the roles of RWD and RWE in clinical trials for drugs treating rare diseases. This paper summarizes relevant guidance documents and frameworks by selected regulatory agencies and the current practice on the use of RWD and RWE in natural history studies and the design, conduct, and analysis of rare disease clinical trials. A targeted learning roadmap for rare disease trials is described, followed by case studies on the use of RWD and RWE to support a natural history study and marketing applications in various settings.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_07

- 相似度：`0.4725`
- 时间差：`-1668` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`325478` / 2020-03-16
- arXiv：`2410.06586` / 2024-10-09
- Grant 标题：Exploring the use of Real-World Data to Generate Real-World Evidence in Regulatory Decision-Making (U01) Clinical Trials Optional
- Paper 标题：Use of Real-World Data and Real-World Evidence in Rare Disease Drug Development: A Statistical Perspective

**Grant Description**

The purpose of this Funding Opportunity Announcement (FOA) is to support research projects that examine real-world data (RWD), real-world evidence (RWE), and related issues such as data analytics, the use of digital health tools, and innovative trial designs utilizing healthcare settings.

**arXiv Abstract**

Real-world data (RWD) and real-world evidence (RWE) have been increasingly used in medical product development and regulatory decision-making, especially for rare diseases. After outlining the challenges and possible strategies to address the challenges in rare disease drug development (see the accompanying paper), the Real-World Evidence (RWE) Scientific Working Group of the American Statistical Association Biopharmaceutical Section reviews the roles of RWD and RWE in clinical trials for drugs treating rare diseases. This paper summarizes relevant guidance documents and frameworks by selected regulatory agencies and the current practice on the use of RWD and RWE in natural history studies and the design, conduct, and analysis of rare disease clinical trials. A targeted learning roadmap for rare disease trials is described, followed by case studies on the use of RWD and RWE to support a natural history study and marketing applications in various settings.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_08

- 相似度：`0.4578`
- 时间差：`500` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`339641` / 2022-04-20
- arXiv：`2012.03188` / 2020-12-06
- Grant 标题：RFI - HIV Care and Treatment
- Paper 标题：Representaciones del aprendizaje reutilizando los gradientes de la retropropagacion

**Grant Description**

The United States Government, represented by the Agency for International Development (USAID) in Guatemala is conducting this Request for Information (RFI) to identify local organizations in the Central America Region who possess the capabilities to implement the HIV Care and Treatment Project. El Gobierno de los Estados Unidos, representado por la Agencia para el Desarrollo Internacional (USAID) en Guatemala, está realizando esta Solicitud de Información (RFI) para identificar organizaciones locales en la Región de América Central que posean las capacidades para implementar el Proyecto de Atención y Tratamiento del VIH.

**arXiv Abstract**

This work proposes an algorithm for taking advantage of backpropagation gradients to determine feature importance at different stages of training. Additionally, we propose a way to represent the learning process qualitatively. Experiments were performed over the Wisconsin cancer dataset provided by sklearn, and results showed an interesting convergence of the so called "learning gradients" towards the most important features. --- Este trabajo propone el algoritmo de gradientes de aprendizaje para encontrar significado en las entradas de una red neuronal. Ademas, se propone una manera de evaluarlas por orden de importancia y representar el proceso de aprendizaje a traves de las etapas de entrenamiento. Los resultados obtenidos utilizan como referencia el conjunto de datos acerca de tumores malignos y benignos en Wisconsin. Esta referencia sirvio para detectar un patron en las variables mas importantes del modelo gracias, asi como su evolucion temporal.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_09

- 相似度：`0.4552`
- 时间差：`-1821` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`281308` / 2016-02-03
- arXiv：`2101.12246` / 2021-01-28
- Grant 标题：The National Syndromic Surveillance Program: Enhancing Syndromic Surveillance Capacity and Practice
- Paper 标题：Revisiting Non-Specific Syndromic Surveillance

**Grant Description**

The National Syndromic Surveillance Program: Enhancing Syndromic Surveillance Capacity and Practice

**arXiv Abstract**

Infectious disease surveillance is of great importance for the prevention of major outbreaks. Syndromic surveillance aims at developing algorithms which can detect outbreaks as early as possible by monitoring data sources which allow to capture the occurrences of a certain disease. Recent research mainly focuses on the surveillance of specific, known diseases, putting the focus on the definition of the disease pattern under surveillance. Until now, only little effort has been devoted to what we call non-specific syndromic surveillance, i.e., the use of all available data for detecting any kind of outbreaks, including infectious diseases which are unknown beforehand. In this work, we revisit published approaches for non-specific syndromic surveillance and present a set of simple statistical modeling techniques which can serve as benchmarks for more elaborate machine learning approaches. Our experimental comparison on established synthetic data and real data in which we injected synthetic outbreaks shows that these benchmarks already achieve very competitive results and often outperform more elaborate algorithms.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_10

- 相似度：`0.4511`
- 时间差：`-3451` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`271457` / 2015-01-14
- arXiv：`2406.18625` / 2024-06-26
- Grant 标题：Analyze and Evaluate Potential Risk Factors for Amyotrophic Lateral Sclerosis (ALS)
- Paper 标题：Automatic Prediction of Amyotrophic Lateral Sclerosis Progression using Longitudinal Speech Transformer

**Grant Description**

The purpose of this funding opportunity announcement (FOA) is to allow for investigator-initiated research that will further the understanding of potential risk factors for amyotrophic lateral sclerosis (ALS), while supporting the goals of the National ALS Registry.

**arXiv Abstract**

Automatic prediction of amyotrophic lateral sclerosis (ALS) disease progression provides a more efficient and objective alternative than manual approaches. We propose ALS longitudinal speech transformer (ALST), a neural network-based automatic predictor of ALS disease progression from longitudinal speech recordings of ALS patients. By taking advantage of high-quality pretrained speech features and longitudinal information in the recordings, our best model achieves 91.0\% AUC, improving upon the previous best model by 5.6\% relative on the ALS TDI dataset. Careful analysis reveals that ALST is capable of fine-grained and interpretable predictions of ALS progression, especially for distinguishing between rarer and more severe cases. Code is publicly available.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_11

- 相似度：`0.4487`
- 时间差：`-3115` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`284301` / 2016-06-01
- arXiv：`2412.08228` / 2024-12-11
- Grant 标题：Coral Reef Assessment at Ritidan Unit, Guam NWR
- Paper 标题：Hierarchical Classification for Automated Image Annotation of Coral Reef Benthic Structures

**Grant Description**

1. Characterize benthic structure and coral assemblages within the Refugeâ¿¿s boundaries. 2. Provide an inventory of all coral species found in the fore reef (lower spur and groove and upper terrace) and reef flats (i.e., back reef & reef crest) to include presence/absence of ESA listed corals. 3. Determine the presence/absence of coral disease, coral bleaching, or predation upon corals. 4. Produce a final product report that includes photos of coral species and assemblage, benthic GIS maps showing benthic structure and coral species locations, and provide measures of coral diversity, and abundance. A comparison of data collected from the transects surveyed in the previous study will be made.

**arXiv Abstract**

Automated benthic image annotation is crucial to efficiently monitor and protect coral reefs against climate change. Current machine learning approaches fail to capture the hierarchical nature of benthic organisms covering reef substrata, i.e., coral taxonomic levels and health condition. To address this limitation, we propose to annotate benthic images using hierarchical classification. Experiments on a custom dataset from a Northeast Brazilian coral reef show that our approach outperforms flat classifiers, improving both F1 and hierarchical F1 scores by approximately 2\% across varying amounts of training data. In addition, this hierarchical method aligns more closely with ecological objectives.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_12

- 相似度：`0.4478`
- 时间差：`-876` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`308248` / 2018-10-29
- arXiv：`2103.12808` / 2021-03-23
- Grant 标题：Surveillance for Respiratory Syncytial Virus (RSV) and Other Viral Respiratory Infections Among Native Americans/Alaska Natives
- Paper 标题：Use of mathematical modelling to assess respiratory syncytial virus epidemiology and interventions: A literature review

**Grant Description**

Respiratory syncytial virus (RSV) is the leading viral cause of lower respiratory tract infection including bronchiolitis and pneumonia in infants and children worldwide. The annual rate of RSV hospitalizations for children less than 2 years of age in the US is 5.2 per 1,000, but substantially higher among Native Americans. There are currently approximately 40 vaccines or antibody products in development designed to prevent RSV infections. With potential licensure of these products on the horizon, it will be important to establish baseline estimates of the burden of RSV infections in high-risk populations, like Native Americans, and to maintain surveillance post-licensure in order to evaluate impact. Native Americans are also at higher risk for severe respiratory infections associated with human metapneumovirus (HMPV) and other viruses, which will also be monitored through this system.

**arXiv Abstract**

Respiratory syncytial virus (RSV) is a leading cause of acute lower respiratory tract infection worldwide, resulting in approximately sixty thousand annual hospitalizations of <5-year-olds in the United States alone and three million annual hospitalizations globally. The development of over 40 vaccines and immunoprophylactic interventions targeting RSV has the potential to significantly reduce the disease burden from RSV infection in the near future. In the context of RSV, a highly contagious pathogen, dynamic transmission models (DTMs) are valuable tools in the evaluation and comparison of the effectiveness of different interventions. This review, the first of its kind for RSV DTMs, provides a valuable foundation for future modelling efforts and highlights important gaps in our understanding of RSV epidemics. Specifically, we have searched the literature using Web of Science, Scopus, Embase, and PubMed to identify all published manuscripts reporting the development of DTMs focused on the population transmission of RSV. We reviewed the resulting studies and summarized the structure, parameterization, and results of the models developed therein. We anticipate that future RSV DTMs, combined with cost-effectiveness evaluations, will play a significant role in shaping decision making in the development and implementation of intervention programs.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_13

- 相似度：`0.4365`
- 时间差：`-1021` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`316721` / 2019-06-04
- arXiv：`2203.11391` / 2022-03-21
- Grant 标题：Advancing Novel Research Models to Study Idiopathic Pulmonary Fibrosis (U01 Clinical Trial Not Allowed)
- Paper 标题：Survival Analysis for Idiopathic Pulmonary Fibrosis using CT Images and Incomplete Clinical Data

**Grant Description**

To establish a set of complementary model systems that reproduce essential disease-defining features of human idiopathic pulmonary fibrosis (IPF). This collection of models will advance our understanding of the pathogenesis of IPF from its onset through disease progression and serve as a resource for the broader research community, including investigators developing and testing novel therapies to treat this fatal disease.

**arXiv Abstract**

Idiopathic Pulmonary Fibrosis (IPF) is an inexorably progressive fibrotic lung disease with a variable and unpredictable rate of progression. CT scans of the lungs inform clinical assessment of IPF patients and contain pertinent information related to disease progression. In this work, we propose a multi-modal method that uses neural networks and memory banks to predict the survival of IPF patients using clinical and imaging data. The majority of clinical IPF patient records have missing data (e.g. missing lung function tests). To this end, we propose a probabilistic model that captures the dependencies between the observed clinical variables and imputes missing ones. This principled approach to missing data imputation can be naturally combined with a deep survival analysis model. We show that the proposed framework yields significantly better survival analysis results than baselines in terms of concordance index and integrated Brier score. Our work also provides insights into novel image-based biomarkers that are linked to mortality.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_14

- 相似度：`0.4326`
- 时间差：`236` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`332448` / 2021-03-30
- arXiv：`2008.02547` / 2020-08-06
- Grant 标题：Mechanisms of HIV Resistance to Broadly Neutralizing Antibodies (bNAbs) (U01 Clinical Trial Not Allowed)
- Paper 标题：Predicting in vivo escape dynamics of HIV-1 from a broadly neutralizing antibody

**Grant Description**

To encourage multidisciplinary teams to characterize mechanisms that impact resistance to HIV broadly neutralizing antibodies (bNAbs) and develop strategies to prevent and overcome HIV resistance to bNAbs.

**arXiv Abstract**

Broadly neutralizing antibodies are promising candidates for treatment and prevention of HIV-1 infections. Such antibodies can temporarily suppress viral load in infected individuals; however, the virus often rebounds by escape mutants that have evolved resistance. In this paper, we map an in vivo fitness landscape of HIV-1 interacting with broadly neutralizing antibodies, using data from a recent clinical trial. We identify two fitness factors, antibody dosage and viral load, that determine viral reproduction rates reproducibly across different hosts. The model successfully predicts the escape dynamics of HIV-1 in the course of an antibody treatment, including a characteristic frequency turnover between sensitive and resistant strains. This turnover is governed by a dosage-dependent fitness ranking, resulting from an evolutionary tradeoff between antibody resistance and its collateral cost in drug-free growth. Our analysis suggests resistance-cost tradeoff curves as a measure of antibody performance in the presence of resistance evolution.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_15

- 相似度：`0.4323`
- 时间差：`-2350` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`306843` / 2018-07-06
- arXiv：`2412.08228` / 2024-12-11
- Grant 标题：Long Term Monitoring of Selected Coral Reef Sites in Dry Tortugas
- Paper 标题：Hierarchical Classification for Automated Image Annotation of Coral Reef Benthic Structures

**Grant Description**

The primary project goal is to evaluate long term status and trends of common and rare coral reef types and benthic communities in Dry Tortugas National Park. The objectives are to collect benthic data which provides a quantitative assessment of stony coral species richness density, abundance, and spatial cover, benthic cover values for major taxonomic groups (e.g., stony corals, macroalgae, octocorals, sponges, and zoanthids) and an evaluation of stony coral and octocoral condition including the prevalence of disease and bleaching and causes of mortality. Targeted surveys also focus on the abundance of Diadema antillarum within the park. In addition, in situ water temperature data is collected at many sites to determine its influence on benthic community structure. Lastly, surveys to assess the effects of diving activities on coral communities within the Research Natural Area dive sites are performed.

**arXiv Abstract**

Automated benthic image annotation is crucial to efficiently monitor and protect coral reefs against climate change. Current machine learning approaches fail to capture the hierarchical nature of benthic organisms covering reef substrata, i.e., coral taxonomic levels and health condition. To address this limitation, we propose to annotate benthic images using hierarchical classification. Experiments on a custom dataset from a Northeast Brazilian coral reef show that our approach outperforms flat classifiers, improving both F1 and hierarchical F1 scores by approximately 2\% across varying amounts of training data. In addition, this hierarchical method aligns more closely with ecological objectives.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_16

- 相似度：`0.4300`
- 时间差：`-1582` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`323257` / 2019-12-23
- arXiv：`2405.02322` / 2024-04-22
- Grant 标题：Methods and Measurement in Research with Sexual and Gender Minority (SGM) Populations (R21- Clinical Trials Not Allowed)
- Paper 标题：Towards Causal Interpretation of Sexual Orientation in Regression Analysis: Applications and Challenges

**Grant Description**

The purpose of this initiative is to support projects to advance the measurement of constructs relevant to health research with sexual and gender minority (SGM) populations.

**arXiv Abstract**

This study presents an approach to analyze health disparities in Sexual and Gender Minority (SGM) populations, with a focus on the role of social support levels as an example to allow causal interpretations of regression models. We advocate for precisely defining the exposure variable and incorporating mediators into analyses, to address the limitations of comparing counterfactual outcomes solely between SGM and heterosexual populations. We define sexual orientation into domains (attraction, behavior, and identity), and emphasize a consideration of these elements either separately or together, depending on the research question. We also introduce social support measured before and after the disclosure of sexual orientation to facilitate inference. We illustrate this approach by examining the association between SGM status and depression diagnosis with data from the 2020 and 2021 National Health Interview Survey. We find a direct effect of SGM status on depression (OR: 3.07, 95% CI: 2.64 - 3.58) and no indirect effect through social support (OR: 1.07, 95% CI: 0.87-1.31). Our research emphasizes the necessity of the comprehensive measurement of sexual orientation and a focus on intervenable variables like social support in order to empower SGM communities and address SGM related health inequalities.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_17

- 相似度：`0.4256`
- 时间差：`-3141` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`258689` / 2014-06-27
- arXiv：`2302.00516` / 2023-02-01
- Grant 标题：Innovative Assays to Quantify the Latent HIV Reservoir (R01)
- Paper 标题：Quantifying the HIV reservoir with dilution assays and deep viral sequencing

**Grant Description**

The purpose of this Funding Opportunity Announcement (FOA) is to support research on new or improved methods for quantifying latently infected cells in HIV-positive individuals on effective antiretroviral therapy. Quantifying latent HIV reservoirs is critical to evaluating strategies to cure HIV infection in vivo. The current gold-standard method involves a limiting dilution viral outgrowth assay that is slow, resource-intensive, and relatively imprecise. A molecular assay to accurately detect replication-competent provirus, or a viral outgrowth assay with improved efficiency, would facilitate proof-of-concept studies for curing HIV infection.

**arXiv Abstract**

People living with HIV on antiretroviral therapy often have undetectable virus levels by standard assays, but "latent" HIV still persists in viral reservoirs. Eliminating these reservoirs is the goal of HIV cure research. The quantitative viral outgrowth assay (QVOA) is commonly used to estimate the reservoir size, i.e., the infectious units per million (IUPM) of HIV-persistent resting CD4+ T cells. A new variation of the QVOA, the Ultra Deep Sequencing Assay of the outgrowth virus (UDSA), was recently developed that further quantifies the number of viral lineages within a subset of infected wells. Performing the UDSA on a subset of wells provides additional information that can improve IUPM estimation. This paper considers statistical inference about the IUPM from combined dilution assay (QVOA) and deep viral sequencing (UDSA) data, even when some deep sequencing data are missing. Methods are proposed to accommodate assays with wells sequenced at multiple dilution levels and with imperfect sensitivity and specificity, and a novel bias-corrected estimator is included for small samples. The proposed methods are evaluated in a simulation study, applied to data from the University of North Carolina HIV Cure Center, and implemented in the open-source R package SLDeepAssay.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_18

- 相似度：`0.4250`
- 时间差：`-3502` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`237021` / 2013-07-01
- arXiv：`2302.00516` / 2023-02-01
- Grant 标题：Innovative Assays to Quantify the Latent HIV Reservoir (R21)
- Paper 标题：Quantifying the HIV reservoir with dilution assays and deep viral sequencing

**Grant Description**

The purpose of this Funding Opportunity Announcement (FOA) is to support research on new or improved methods for quantifying latently infected cells in HIV-positive individuals on effective antiretroviral therapy. Quantifying latent HIV reservoirs is critical to evaluating strategies to cure HIV infection in vivo. The current gold-standard method involves a limiting dilution viral outgrowth assay that is slow, resource-intensive, and relatively imprecise. A molecular assay to accurately detect replication-competent provirus, or a viral outgrowth assay with improved efficiency, would facilitate proof-of-concept studies for curing HIV infection.

**arXiv Abstract**

People living with HIV on antiretroviral therapy often have undetectable virus levels by standard assays, but "latent" HIV still persists in viral reservoirs. Eliminating these reservoirs is the goal of HIV cure research. The quantitative viral outgrowth assay (QVOA) is commonly used to estimate the reservoir size, i.e., the infectious units per million (IUPM) of HIV-persistent resting CD4+ T cells. A new variation of the QVOA, the Ultra Deep Sequencing Assay of the outgrowth virus (UDSA), was recently developed that further quantifies the number of viral lineages within a subset of infected wells. Performing the UDSA on a subset of wells provides additional information that can improve IUPM estimation. This paper considers statistical inference about the IUPM from combined dilution assay (QVOA) and deep viral sequencing (UDSA) data, even when some deep sequencing data are missing. Methods are proposed to accommodate assays with wells sequenced at multiple dilution levels and with imperfect sensitivity and specificity, and a novel bias-corrected estimator is included for small samples. The proposed methods are evaluated in a simulation study, applied to data from the University of North Carolina HIV Cure Center, and implemented in the open-source R package SLDeepAssay.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_19

- 相似度：`0.4244`
- 时间差：`-669` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`286518` / 2016-07-25
- arXiv：`1805.10150` / 2018-05-25
- Grant 标题：IAEA Project Surge Expansion of Sterile Insect Technique (SIT) to Control Mosquito Populations
- Paper 标题：On the use of the sterile insect technique or the incompatible insect technique to reduce or eliminate mosquito populations

**Grant Description**

IAEA Project Surge Expansion of Sterile Insect Technique (SIT) to Control Mosquito Populations that Transmit the Zika Virus

**arXiv Abstract**

Vector control is critical to limit the circulation of vector-borne diseases like chikungunya, dengue or zika which have become important issues around the world. Among them the Sterile Insect Technique (SIT) and the Incompatible Insect Technique (IIT) recently aroused a renewed interest. In this paper we derive and study a minimalistic mathematical model designed for Aedes mosquito population elimination by SIT/IIT. Contrary to most of the previous models, it is bistable in general, allowing simultaneously for elimination of the population and for its survival. We consider dierent types of releases (constant, periodic or impulsive) and show necessary conditions to reach elimination in each case. We also estimate both sucient and minimal treatment times. Biological parameters are estimated from a case study of an Aedes polynesiensis population, for which extensive numerical investigations illustrate the analytical results. The applications of this work are twofold: to help identifying some key parameters that may need further eld investigations, and to help designing release protocols.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### BIOMED_20

- 相似度：`0.4233`
- 时间差：`-1085` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`328538` / 2020-08-03
- arXiv：`2307.13708` / 2023-07-24
- Grant 标题：Systematic Characterization of Genomic Variation on Genomic Function and Phenotype (UM1 Clinical Trial Not Allowed)
- Paper 标题：The Impact of Genomic Variation on Function (IGVF) Consortium

**Grant Description**

FOA seeks applications to experimentally correlate variants with effects on genomic function. This will be accomplished by performing systematic perturbation; collecting data on the effects of non-coding and protein-coding genomic variation on molecular, cellular, and organismal phenotypes; generating a catalog of these variant effects; and assisting in a group predictive modeling effort using the data. Centers funded through this initiative will become part of the Impact of Genomic Variation on Function Consortium. As members of this Consortium, mapping centers will be expected to work closely with one another and other Consortium components to accelerate understanding of how genomic variation impacts human health and disease through the coordination of data collection strategies and analyses.

**arXiv Abstract**

Our genomes influence nearly every aspect of human biology from molecular and cellular functions to phenotypes in health and disease. Human genetics studies have now associated hundreds of thousands of differences in our DNA sequence ("genomic variation") with disease risk and other phenotypes, many of which could reveal novel mechanisms of human biology and uncover the basis of genetic predispositions to diseases, thereby guiding the development of new diagnostics and therapeutics. Yet, understanding how genomic variation alters genome function to influence phenotype has proven challenging. To unlock these insights, we need a systematic and comprehensive catalog of genome function and the molecular and cellular effects of genomic variants. Toward this goal, the Impact of Genomic Variation on Function (IGVF) Consortium will combine approaches in single-cell mapping, genomic perturbations, and predictive modeling to investigate the relationships among genomic variation, genome function, and phenotypes. Through systematic comparisons and benchmarking of experimental and computational methods, we aim to create maps across hundreds of cell types and states describing how coding variants alter protein activity, how noncoding variants change the regulation of gene expression, and how both coding and noncoding variants may connect through gene regulatory and protein interaction networks. These experimental data, computational predictions, and accompanying standards and pipelines will be integrated into an open resource that will catalyze community efforts to explore genome function and the impact of genetic variation on human biology and disease across populations.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

### cs

#### CS_01

- 相似度：`0.4706`
- 时间差：`-700` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`287284` / 2016-08-10
- arXiv：`1807.04178` / 2018-07-11
- Grant 标题：Explainable Artificial Intelligence (XAI)
- Paper 标题：Explainable Security

**Grant Description**

DARPA is soliciting innovative research proposals in the areas of machine learning and human-computer interaction. The goal of Explainable Artificial Intelligence (XAI) is to create a suite of new or modified machine learning techniques that produce explainable models that, when combined with effective explanation techniques, enable end users to understand, appropriately trust, and effectively manage the emerging generation of Artificial Intelligence (AI) systems. Proposed research should investigate innovative approaches that enable revolutionary advances in science, or systems. Specifically excluded is research that primarily results in evolutionary improvements to the existing state of practice.

**arXiv Abstract**

The Defense Advanced Research Projects Agency (DARPA) recently launched the Explainable Artificial Intelligence (XAI) program that aims to create a suite of new AI techniques that enable end users to understand, appropriately trust, and effectively manage the emerging generation of AI systems. In this paper, inspired by DARPA's XAI program, we propose a new paradigm in security research: Explainable Security (XSec). We discuss the ``Six Ws'' of XSec (Who? What? Where? When? Why? and How?) and argue that XSec has unique and complex characteristics: XSec involves several different stakeholders (i.e., the system's developers, analysts, users and attackers) and is multi-faceted by nature (as it requires reasoning about system model, threat model and properties of security, privacy and trust as well as about concrete attacks, vulnerabilities and countermeasures). We define a roadmap for XSec that identifies several possible research directions.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_02

- 相似度：`0.4471`
- 时间差：`-3669` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`46271` / 2009-03-24
- arXiv：`1904.05211` / 2019-04-10
- Grant 标题：Gravitational Physics
- Paper 标题：Applicability study of the PRIMAD model to LIGO gravitational wave search workflows

**Grant Description**

Emphasizes the theory of strong gravitational fields and their application to astrophysics and cosmology, computer simulations of strong and gravitational fields, and gravitational radiation; and construction of a quantum theory of gravity. The program oversees the management of the construction, commissioning, and operation of the Laser Interferometer Gravity Wave Observatory (LIGO), and provides support for LIGO users and other experimental investigations in gravitational physics and related areas.

**arXiv Abstract**

The PRIMAD model with its six components (i.e., Platform, Research Objective, Implementation, Methods, Actors, and Data), provides an abstract taxonomy to represent computational experiments and enforce reproducibility by design. In this paper, we assess the model applicability to a set of Laser Interferometer Gravitational-Wave Observatory (LIGO) workflows from literature sources (i.e., published papers). Our work outlines potentials and limits of the model in terms of its abstraction levels and application process.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_03

- 相似度：`0.4471`
- 时间差：`-2889` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`93899` / 2011-05-13
- arXiv：`1904.05211` / 2019-04-10
- Grant 标题：Gravitational Physics
- Paper 标题：Applicability study of the PRIMAD model to LIGO gravitational wave search workflows

**Grant Description**

Emphasizes the theory of strong gravitational fields and their application to astrophysics and cosmology, computer simulations of strong and gravitational fields, and gravitational radiation; and construction of a quantum theory of gravity. The program oversees the management of the construction, commissioning, and operation of the Laser Interferometer Gravity Wave Observatory (LIGO), and provides support for LIGO users and other experimental investigations in gravitational physics and related areas.

**arXiv Abstract**

The PRIMAD model with its six components (i.e., Platform, Research Objective, Implementation, Methods, Actors, and Data), provides an abstract taxonomy to represent computational experiments and enforce reproducibility by design. In this paper, we assess the model applicability to a set of Laser Interferometer Gravitational-Wave Observatory (LIGO) workflows from literature sources (i.e., published papers). Our work outlines potentials and limits of the model in terms of its abstraction levels and application process.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_04

- 相似度：`0.4348`
- 时间差：`-233` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`334291` / 2021-06-23
- arXiv：`2202.05714` / 2022-02-11
- Grant 标题：Cooperative Agreement for CESU-affiliated Partner with Great Lakes Cooperative Ecosystem Studies Unit
- Paper 标题：Modeling Reservoir Release Using Pseudo-Prospective Learning and Physical Simulations to Predict Water Temperature

**Grant Description**

The USGS is offering a funding opportunity to a CESU partner for research in stream and reservoir water quality modeling, with a focus on temperature. Water temperature is a “master variable” for many important aquatic outcomes, including the suitability of habitat, evaporation rates, greenhouse gas exchange, and efficiency of thermoelectric energy production. Stream temperature is one of the most widely measured water characteristics by the USGS, though monitoring gaps in time and space requires modeling efforts to understand broad-scale temperature dynamics and supply decision-ready data to our stakeholders. Currently, stream and lake temperature are modeled separately, despite our knowledge that water flowing into a reservoir affects its temperature, and that reservoirs greatly impact the temperature of downstream river reaches. Further, in some places, water managers can affect downstream temperatures via reservoir releases, and understanding when to release, how much to release, and the expected water temperature changes from the release can support better decision making. The USGS and collaborators are developing process-guided machine learning models for streams and lakes that leverage the benefits of both process and machine learning models; the models are grounded in physical realism and perform well in data sparse and data rich conditions (e.g., Read et al., 2019). But key processes related to stream temperature remain unexplored or not accurately predicted or represented in the process-guided deep learning framework. These include but are not limited to: the impact of reservoir releases on downstream temperature, sub-daily prediction to accurately predict extremes, inclusion of different data types that may have lower accuracy (e.g., satellite estimated surface temperature), translation to finer resolution stream segments, prediction beneath reservoirs with varying amounts of data, and representation of certain processes that might be critical to evaluate long term change like groundwater contribution to stream temperature dynamics.

**arXiv Abstract**

This paper proposes a new data-driven method for predicting water temperature in stream networks with reservoirs. The water flows released from reservoirs greatly affect the water temperature of downstream river segments. However, the information of released water flow is often not available for many reservoirs, which makes it difficult for data-driven models to capture the impact to downstream river segments. In this paper, we first build a state-aware graph model to represent the interactions amongst streams and reservoirs, and then propose a parallel learning structure to extract the reservoir release information and use it to improve the prediction. In particular, for reservoirs with no available release information, we mimic the water managers' release decision process through a pseudo-prospective learning method, which infers the release information from anticipated water temperature dynamics. For reservoirs with the release information, we leverage a physics-based model to simulate the water release temperature and transfer such information to guide the learning process for other reservoirs. The evaluation for the Delaware River Basin shows that the proposed method brings over 10\% accuracy improvement over existing data-driven models for stream temperature prediction when the release data is not available for any reservoirs. The performance is further improved after we incorporate the release data and physical simulations for a subset of reservoirs.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_05

- 相似度：`0.4166`
- 时间差：`-3074` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`236600` / 2013-06-19
- arXiv：`2111.09502` / 2021-11-18
- Grant 标题：Drug Docking and Screening Data Resource (U01)
- Paper 标题：Docking-based Virtual Screening with Multi-Task Learning

**Grant Description**

The purpose of this Funding Opportunity Announcement (FOA) is to continue to increase the amount of publicly available, high-quality data describing structures and affinities of protein-drug ligand complexes -data vital for development, validation, and benchmarking of drug docking and screening software. Accurate and robust methods for in silico drug screening are expected to speed drug discovery and reduce drug development cost by focusing experimental efforts on the most promising candidate compounds. The ability to predict side effects resulting from off-target binding and to increase repurposing of existing pharmaceuticals is an additional expected benefit.

**arXiv Abstract**

Machine learning shows great potential in virtual screening for drug discovery. Current efforts on accelerating docking-based virtual screening do not consider using existing data of other previously developed targets. To make use of the knowledge of the other targets and take advantage of the existing data, in this work, we apply multi-task learning to the problem of docking-based virtual screening. With two large docking datasets, the results of extensive experiments show that multi-task learning can achieve better performances on docking score prediction. By learning knowledge across multiple targets, the model trained by multi-task learning shows a better ability to adapt to a new target. Additional empirical study shows that other problems in drug discovery, such as the experimental drug-target affinity prediction, may also benefit from multi-task learning. Our results demonstrate that multi-task learning is a promising machine learning approach for docking-based virtual screening and accelerating the process of drug discovery.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_06

- 相似度：`0.4145`
- 时间差：`-543` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`328715` / 2020-08-17
- arXiv：`2202.05714` / 2022-02-11
- Grant 标题：Cooperative Ecosystem Studies Unit, Great Lakes Northern Forests CESU
- Paper 标题：Modeling Reservoir Release Using Pseudo-Prospective Learning and Physical Simulations to Predict Water Temperature

**Grant Description**

The USGS is offering a funding opportunity to a CESU partner for research in stream and reservoir temperature modeling. Water temperature is a ¿master variable¿ for many important aquatic outcomes, including the suitability of habitat, evaporation rates, greenhouse gas exchange, and efficiency of thermoelectric energy production. Stream temperature is one of the most widely measured water characteristics by the USGS, though monitoring gaps in time and space requires modeling efforts to understand broad-scale temperature dynamics and supply decision-ready data to our stakeholders. Currently, stream and lake temperature are modeled separately, despite our knowledge that water flowing into a reservoir affects its temperature, and that reservoirs greatly impact the temperature of downstream river reaches. Further, in some places, water managers can affect downstream temperatures via reservoir releases, and understanding when to release, how much to release, and the expected water temperature changes from the release can support better decision making. The USGS and collaborators are developing process-guided machine learning models for streams and lakes that leverage the benefits of both process and machine learning models; the models are grounded in physical realism and perform well in data sparse and data rich conditions (e.g., Read et al., 2019). However, we have yet to model a stream network that reflects both lake and stream temperature dynamics.

**arXiv Abstract**

This paper proposes a new data-driven method for predicting water temperature in stream networks with reservoirs. The water flows released from reservoirs greatly affect the water temperature of downstream river segments. However, the information of released water flow is often not available for many reservoirs, which makes it difficult for data-driven models to capture the impact to downstream river segments. In this paper, we first build a state-aware graph model to represent the interactions amongst streams and reservoirs, and then propose a parallel learning structure to extract the reservoir release information and use it to improve the prediction. In particular, for reservoirs with no available release information, we mimic the water managers' release decision process through a pseudo-prospective learning method, which infers the release information from anticipated water temperature dynamics. For reservoirs with the release information, we leverage a physics-based model to simulate the water release temperature and transfer such information to guide the learning process for other reservoirs. The evaluation for the Delaware River Basin shows that the proposed method brings over 10\% accuracy improvement over existing data-driven models for stream temperature prediction when the release data is not available for any reservoirs. The performance is further improved after we incorporate the release data and physical simulations for a subset of reservoirs.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_07

- 相似度：`0.3985`
- 时间差：`-1391` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`227155` / 2013-03-14
- arXiv：`1702.04652` / 2017-01-03
- Grant 标题：Cyber Security (CS) Collaborative Research Alliance (CRA) Program Announcement (PA)
- Paper 标题：Overview of Cyber Science and Technology Programs at the U.S. Army Research Laboratory

**Grant Description**

The U.S. Army Contracting Command – Aberdeen Proving Ground RTP Division, on behalf of the U.S. Army Research Laboratory (ARL), is issuing a Program Announcement (PA), W911NF-13-R-0004, for the establishment of a Collaborative Research Alliance (CRA) for Cyber Security (CS).Cyber security is critical to the Army due to the growing number and sophistication of attacks on military cyber networks coupled with the ever increasing reliance on cyber systems to conduct the Army’s mission. The Army Research Laboratory (ARL) has established an Enterprise approach to Cyber Security that couples multi-disciplinary internal research, analysis, and operations with extramural research and collaborative ventures. ARL intends to establish a new collaborative venture – The Cyber Security Collaborative Research Alliance (CRA) – that seeks to advance the theoretical foundations of cyber science in the context of Army networks. This Collaborative Research Alliance will consist of academia, industry and government researchers working jointly to solve complex problems. The overall objective of the Cyber Security CRA is to develop a fundamental understanding of cyber phenomena, including aspects of human attackers, cyber defenders, and end users, so that fundamental laws, theories, and theoretically grounded and empirically validated models can be applied to a broad range of Army domains, applications, and environments. The ARL strongly believes that a joint collaborative approach by a multidisciplinary researcher team is required to make fundamental advances towards meeting the CRA goal to develop a fundamental understanding of cyber phenomena. ARL has identified three interrelated aspects or Research Areas of cyber security that when jointly studied will advance the theoretical foundations of cyber science in the context of Army networks. In addition to these three Research Areas (RAs), advancing the theoretical foundations requires a trans-disciplinary approach that takes into account the human element of the network. This Cross-Cutting Research Issue (CCRI) addressing Psychosocial Effects must be jointly studied in the context and the constraints of the three Research Areas. The Research Areas and CCRI for this CRA are as follows: (1) Risk; (2) Detection; (3) Agility; (4) Psychosocial Effects.The CS CRA PA can be found at www.arl.army.mil/cracyber.This PA is expected to result in the award of a cooperative agreement (CA) as defined at 31 U.S.C. 6305 for the execution of the program. The CA will be awarded to a Consortium of organizations that may include academic, industrial and non-profit organizations. To assure the creation of a well-focused research program, the number of partners should balance the need for expertise in all three Research Areas and the crosscutting research initiative with the need to maintain a focused, cohesive, well-integrated research program. The Consortium must be led by an academic institution charged with spearheading the focused basic research program. Additionally, it is a goal that “covered educational institutions” (to include Historically Black Colleges and Universities and Minority-Serving Institutions) will receive 5% of the annual CA funding.The Consortium under this PA, will be selected via a two stage process involving Whitepapers and full proposals. Full details regarding the application process are found in section D of the CS CRA PA. Planned funding levels for the CA are set forth in the CS CRA PA. Contingent upon available funding, the Army expects to support the CS CRA for five years with an option for an additional five years.Whitepapers for the Cyber Security (CS) Collaborative Research Alliance (CRA) are due 26 April 2013. Full proposals from invited Offerors are due 19 July 2013, with an award expected in September 2013.Contracting Office Address:ACC-APG RTP, ATTN: AMSSB-ACR, Research Triangle Park Division, P.O. 1221, Research Triangle Park, NC 27709-2211Additional InformationArmy Research Laboratory (ARL) Broad Agency Announcements (BAA)Cyber Security Research AlliancePoints of Contact(s):William A. Creech, 919-549-4212

**arXiv Abstract**

This paper provides an overview of research programs in cyber security performed by the U.S Army Research Laboratory. Although ARL is the U.S. Army's corporate laboratory that focuses on fundamental and early applied research, the fundamental science endeavors are closely integrated with extensive operationally-oriented programs. One example is the Cyber Collaborative Research Alliance (CRA) that brings together ARL scientists with academic researchers from dozens of U.S. universities. ARL cyber scientists are largely driven by challenges unique to the ground operations of the Army; this paper outlines a few of these challenges and the ways in which they are addressed by ARL research efforts. The long-term campaign of cyber research is guided by the vision of the future Army battlefield. In the year 2040, it will be a highly converged virtual-physical space, where cyber operations will be an integral part of the battle.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_08

- 相似度：`0.3956`
- 时间差：`-2995` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`46298` / 2009-03-24
- arXiv：`1706.01540` / 2017-06-05
- Grant 标题：Topology
- Paper 标题：Synthetic Homology in Homotopy Type Theory

**Grant Description**

Supports research on algebraic topology, including homotopy theory, ordinary and extraordinary homology and cohomology, cobordism theory, and K-theory; topological manifolds and cell complexes, fiberings, knots, and links; differential topology and actions of groups of transformations; geometric group theory; and general topology and continua theory.

**arXiv Abstract**

This paper defines homology in homotopy type theory, in the process stable homotopy groups are also defined. Previous research in synthetic homotopy theory is relied on, in particular the definition of cohomology. This work lays the foundation for a computer checked construction of homology.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_09

- 相似度：`0.3942`
- 时间差：`-2735` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`274934` / 2015-03-04
- arXiv：`2208.13512` / 2022-08-29
- Grant 标题：Research and Development
- Paper 标题：Labeling of Cultural Heritage Collections on the Intersection of Visual Analytics and Digital Humanities

**Grant Description**

The Research and Development program supports projects that address major challenges in preserving or providing access to humanities collections and resources. These challenges include the need to find better ways to preserve materials of critical importance to the nation’s cultural heritage—from fragile artifacts and manuscripts to analog recordings and digital assets subject to technological obsolescence—and to develop advanced modes of organizing, searching, discovering, and using such materials. This program recognizes that finding solutions to complex problems often requires forming interdisciplinary project teams, bringing together participants with expertise in the humanities; in preservation; and in information, computer, and natural science. All projects must demonstrate how advances in preservation and access would benefit the cultural heritage community in supporting humanities research, teaching, or public programming.

**arXiv Abstract**

Engaging in interdisciplinary projects on the intersection between visualization and humanities research can be a challenging endeavor. Challenges can be finding valuable outcomes for both domains, or how to apply state-of-the-art visual analytics methods like supervised machine learning algorithms. We discuss these challenges when working with cultural heritage data. Further, there is a gap in applying these methods to intangible heritage. To give a reflection on some interdisciplinary projects, we present three case studies focusing on the labeling of cultural heritage collections, the problems and challenges with the data, the participatory design process, and takeaways for the visualization scholars from these collaborations.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_10

- 相似度：`0.3942`
- 时间差：`-2324` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`283061` / 2016-04-18
- arXiv：`2208.13512` / 2022-08-29
- Grant 标题：Research and Development
- Paper 标题：Labeling of Cultural Heritage Collections on the Intersection of Visual Analytics and Digital Humanities

**Grant Description**

The Research and Development program supports projects that address major challenges in preserving or providing access to humanities collections and resources. These challenges include the need to find better ways to preserve materials of critical importance to the nation’s cultural heritage—from fragile artifacts and manuscripts to analog recordings and digital assets subject to technological obsolescence—and to develop advanced modes of organizing, searching, discovering, and using such materials. This program recognizes that finding solutions to complex problems often requires forming interdisciplinary project teams, bringing together participants with expertise in the humanities; in preservation; and in information, computer, and natural science. All projects must demonstrate how advances in preservation and access would benefit the cultural heritage community in supporting humanities research, teaching, or public programming.

**arXiv Abstract**

Engaging in interdisciplinary projects on the intersection between visualization and humanities research can be a challenging endeavor. Challenges can be finding valuable outcomes for both domains, or how to apply state-of-the-art visual analytics methods like supervised machine learning algorithms. We discuss these challenges when working with cultural heritage data. Further, there is a gap in applying these methods to intangible heritage. To give a reflection on some interdisciplinary projects, we present three case studies focusing on the labeling of cultural heritage collections, the problems and challenges with the data, the participatory design process, and takeaways for the visualization scholars from these collaborations.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_11

- 相似度：`0.3942`
- 时间差：`-1981` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`292772` / 2017-03-27
- arXiv：`2208.13512` / 2022-08-29
- Grant 标题：Research and Development
- Paper 标题：Labeling of Cultural Heritage Collections on the Intersection of Visual Analytics and Digital Humanities

**Grant Description**

The Research and Development program supports projects that address major challenges in preserving or providing access to humanities collections and resources. These challenges include the need to find better ways to preserve materials of critical importance to the nation’s cultural heritage—from fragile artifacts and manuscripts to analog recordings and digital assets subject to technological obsolescence—and to develop advanced modes of organizing, searching, discovering, and using such materials. This program recognizes that finding solutions to complex problems often requires forming interdisciplinary project teams, bringing together participants with expertise in the humanities; in preservation; and in information, computer, and natural science. All projects must demonstrate how advances in preservation and access would benefit the cultural heritage community in supporting humanities research, teaching, or public programming.

**arXiv Abstract**

Engaging in interdisciplinary projects on the intersection between visualization and humanities research can be a challenging endeavor. Challenges can be finding valuable outcomes for both domains, or how to apply state-of-the-art visual analytics methods like supervised machine learning algorithms. We discuss these challenges when working with cultural heritage data. Further, there is a gap in applying these methods to intangible heritage. To give a reflection on some interdisciplinary projects, we present three case studies focusing on the labeling of cultural heritage collections, the problems and challenges with the data, the participatory design process, and takeaways for the visualization scholars from these collaborations.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_12

- 相似度：`0.3921`
- 时间差：`-24` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`332386` / 2021-03-26
- arXiv：`2104.11079` / 2021-04-19
- Grant 标题：EXPRESS: Randomized Algorithms for Extreme-Scale Science
- Paper 标题：Randomized Algorithms for Scientific Computing (RASC)

**Grant Description**

The DOE SC program in Advanced Scientific Computing Research (ASCR) hereby announces its interest in research applications to explore potentially high-impact approaches in the development and use of randomized algorithms for scientific computing and extreme-scale science

**arXiv Abstract**

Randomized algorithms have propelled advances in artificial intelligence and represent a foundational research area in advancing AI for Science. Future advancements in DOE Office of Science priority areas such as climate science, astrophysics, fusion, advanced materials, combustion, and quantum computing all require randomized algorithms for surmounting challenges of complexity, robustness, and scalability. This report summarizes the outcomes of that workshop, "Randomized Algorithms for Scientific Computing (RASC)," held virtually across four days in December 2020 and January 2021.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_13

- 相似度：`0.3915`
- 时间差：`59` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`292214` / 2017-03-03
- arXiv：`1702.04652` / 2017-01-03
- Grant 标题：Internet of Battlefield Things (IoBT) Collaborative Research Alliance (CRA)
- Paper 标题：Overview of Cyber Science and Technology Programs at the U.S. Army Research Laboratory

**Grant Description**

The ability of the Army to understand, predict, adapt, and exploit the vast array of internetworked things that will be present of the future battlefield is critical to maintaining and increasing its competitive advantage. The explosive growth of technologies in the commercial sector that exploits the convergence of cloud computing, ubiquitous mobile communications, networks of data-gathering sensors, and artificial intelligence presents an imposing challenge for the Army. These Internet of Things (IoT) technologies will give our enemies ever increasing capabilities that must be countered, but commercial developments do not address the unique challenges that the Army will face in using them. The U.S. Army Research Laboratory (ARL) has established an Enterprise approach to address the challenges resulting from the Internet of Battlefield Things (IoBT) that couples multi-disciplinary internal research with extramural research and collaborative ventures. ARL intends to establish a new collaborative venture (the IoBT CRA) that seeks to develop the foundations of IoBT in the context of future Army operations. The Collaborative Research Alliance (CRA) will consist of private sector and government researchers working jointly to solve complex problems. The overall objective is to develop the fundamental understanding of dynamically-composable, adaptive, goal-driven IoBTs to enable predictive analytics for intelligent command and control and battlefield services.The Future Army will operate in a highly complex and rapidly changing environment, thus the U.S. Army’s Operating Concept is to “Win in a Complex World”. The Army must tackle wicked problems wherein objectives and constraints evolve in unpredictable ways. Complexity arises from the increasing heterogeneity, connectivity, scale, dynamics, functionality and interdependence of networked elements, and from the increasing velocity and momentum of human interactions and information. Events now unfold in internet time, as noted by the Defense Science Board (DSB) 2014 Study on Decisive Army Strategic and Expeditionary Maneuver. In this context, future IoBTs will be significantly more complex that today’s networked systems, and novel mathematical approaches and techniques will be needed to represent them, reason about them, understand their behaviors, and to provide predictive analytics in diverse and dynamic environments.The Army will use IoTs for diverse and dynamic missions and will require rapid deployment and adaptation in environments with high mobility, resource constraints, and extreme heterogeneity in both very dense and sparse environments. In addition to Things and IoTs that the Army owns and controls, it may also need to make use of IoTs that it does not own or fully control. A foundational problem to be addressed by the CRA is the fundamental understanding of how to learn and devise complex models of IoBT goals, networks, information, and analytics to enable intelligent command and control, and battlefield services. A critical issue embedded throughout all aspects of IoBTs is cyber physical security as the Army will need to use things it does not control (military (blue), adversary (red), civilian (gray)), accommodate deceptive data, and counter advanced persistent threats. ARL strongly believes that a joint collaborative approach by multidisciplinary researchers is required to make fundamental advances towards meeting the CRA goal to develop a fundamental understanding of IoBTs. ARL has identified three interrelated Research Areas (RAs) that when jointly studied will advance the theoretical foundations of IoBTs in the context of future Army operations.• Discovery, Composition and Adaptation of Goal-Driven Heterogeneous IoBTs• Autonomic IoBTs to Enable Intelligent Services• Distributed Asynchronous Processing and Analytics of ThingsIn addition to these three RAs, Cyber-Physical Security has been identified as a Cross-Cutting Research Issue (CCRI) that is inherent in each of the RAs and that must be jointly studied with the RAs to make fundamental advances in IoBTs.The CRA is intended to create a collaborative environment that enables the Alliance to advance the state-of-the-art and to take advantage of the diverse scientific capabilities and viewpoints of both the private sector and government researchers. The CRA will work collaboratively with ARLs Enterprise research programs to identify areas where joint, multi-disciplinary, collaborative research is advantageous. Continuous collaboration, technical exchanges, site visits, and staff rotations will strengthen and improve the CRA research and its Army relevance.

**arXiv Abstract**

This paper provides an overview of research programs in cyber security performed by the U.S Army Research Laboratory. Although ARL is the U.S. Army's corporate laboratory that focuses on fundamental and early applied research, the fundamental science endeavors are closely integrated with extensive operationally-oriented programs. One example is the Cyber Collaborative Research Alliance (CRA) that brings together ARL scientists with academic researchers from dozens of U.S. universities. ARL cyber scientists are largely driven by challenges unique to the ground operations of the Army; this paper outlines a few of these challenges and the ways in which they are addressed by ARL research efforts. The long-term campaign of cyber research is guided by the vision of the future Army battlefield. In the year 2040, it will be a highly converged virtual-physical space, where cyber operations will be an integral part of the battle.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_14

- 相似度：`0.3850`
- 时间差：`-1841` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`293111` / 2017-04-10
- arXiv：`2204.11461` / 2022-04-25
- Grant 标题：Civic and Tech through English Language (CTEL)
- Paper 标题：A Review of Research on Civic Technology: Definitions, Theories, History and Insights

**Grant Description**

Civic and Tech through English Language II (CTEL II) program will provide English language training courses aimed at improving English language command among Civic Education and Internet and Computer Technologies (ICT) teachers and promoting as well as advancing integrated teaching and learning in the following three disciplines: English language, Civic Education and ICT in the public schools of Samtskhe-Javakheti and Shida Kartli regions.

**arXiv Abstract**

There have been initiatives that take advantage of information and communication technologies to serve civic purposes, referred to as civic technologies (Civic Tech). In this paper, we present a review of 224 papers from the ACM Digital Library focusing on Computer Supported Cooperative Work and Human-Computer Interaction, the key fields supporting the building of Civic Tech. Through this review, we discuss the concepts, theories and history of civic tech research and provide insights on the technological tools, social processes and participation mechanisms involved. Our work seeks to direct future civic tech efforts to the phase of by the citizens.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_15

- 相似度：`0.3836`
- 时间差：`-1443` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`40833` / 2008-02-26
- arXiv：`1202.1782` / 2012-02-08
- Grant 标题：Spin Torque Transfer-Random Access Memory (STT-RAM)
- Paper 标题：Cross-point architecture for spin transfer torque magnetic random access memory

**Grant Description**

DARPA is soliciting innovative research and development (R&D) proposals in the area of Spin-Torque Transfer Random Access Memory technologies. The goal of this program is to develop materials and processes to fully exploit the spin-torque transfer (STT) phenomenon for creating “universal” memory elements. A universal memory element is one that exhibits scalability for high capacity of storage per unit volume, as well as high read/write speed, compatibility with CMOS processes, and non-volatility. Proposed research should investigate innovative approaches that enable revolutionary advances in science, devices, or systems. Specifically excluded is research that primarily results in evolutionary improvements to the existing state of practice. Prior research in micro-magnetics and spintronics has led to the exploitation of giant magnetoresistance (GMR) effects for rotating magnetic disk drive memories, as well as magnetic tunneling junctions (MTJ) for magnetic random access memory (MRAM). The spin-torque transfer (STT) effect is a recent discovery that exploits magnetic spin states to electrically change the magnetic orientation of a material (Science 285, 867 (1999)). Components based on the STT effect can have the properties of a universal memory, high density, high speed, non-volatility, high endurance, and can also be well suited for harsh environments such as those with exposure to ionizing radiation. In addition, they can operate from a single power supply voltage level greatly simplifying associated circuitry.This program is aimed at developing the core technology for exploiting spin-torque transfer and related phenomena for producing large-scale memories. Compatibility and stability with expected mainstream processes for semiconductor electronics and patterned media is an important attribute that should enable significant leverage for these new technologies in delivering early demonstrations and in gaining wider acceptance.All administrative correspondence and questions on this solicitation, including requests for information on how to submit a proposal abstract or full proposal to this BAA, should be directed to BAA08-16@darpa.mil.Full BAA attached.

**arXiv Abstract**

Spin transfer torque magnetic random access memory (STT-MRAM) is considered as one of the most promising candidates to build up a true universal memory thanks to its fast write/read speed, infinite endurance and non-volatility. However the conventional access architecture based on 1 transistor + 1 memory cell limits its storage density as the selection transistor should be large enough to ensure the write current higher than the critical current for the STT operation. This paper describes a design of cross-point architecture for STT-MRAM. The mean area per word corresponds to only two transistors, which are shared by a number of bits (e.g. 64). This leads to significant improvement of data density (e.g. 1.75 F2/bit). Special techniques are also presented to address the sneak currents and low speed issues of conventional cross-point architecture, which are difficult to surmount and few efficient design solutions have been reported in the literature. By using a STT-MRAM SPICE model including precise experimental parameters and STMicroelectronics 65 nm technology, some chip characteristic results such as cell area, data access speed and power have been calculated or simulated to demonstrate the expected performances of this new memory architecture.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_16

- 相似度：`0.3808`
- 时间差：`-4798` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`121133` / 2011-09-08
- arXiv：`2410.20436` / 2024-10-27
- Grant 标题：Coral Reef Conservation Program International Coral Reef Conservation Cooperative Agreements
- Paper 标题：CoralSCOP-LAT: Labeling and Analyzing Tool for Coral Reef Images with Dense Mask

**Grant Description**

The NOAA Coral Reef Conservation Grant Program (Grant Program), as authorized under the Coral Reef Conservation Act of 2000, provides matching grants of financial assistance for international coral reef conservation cooperative agreements. The Grant Program solicits proposals that will support the NOAA Coral Reef Conservation Program International Strategy 2010-2015 (International Strategy). The International Strategy focuses on supporting existing regional efforts in four priority regions based on their interconnections with U.S. reef ecosystems and existing initiatives and partnerships. Two of these four priority regions will be considered under this Federal Funding Opportunity: the Wider Caribbean and Samoa and the Southwest Pacific.

**arXiv Abstract**

Coral reef imagery offers critical data for monitoring ecosystem health, in particular as the ease of image datasets continues to rapidly expand. Whilst semi-automated analytical platforms for reef imagery are becoming more available, the dominant approaches face fundamental limitations. To address these challenges, we propose CoralSCOP-LAT, a coral reef image analysis and labeling tool that automatically segments and analyzes coral regions. By leveraging advanced machine learning models tailored for coral reef segmentation, CoralSCOP-LAT enables users to generate dense segmentation masks with minimal manual effort, significantly enhancing both the labeling efficiency and precision of coral reef analysis. Our extensive evaluations demonstrate that CoralSCOP-LAT surpasses existing coral reef analysis tools in terms of time efficiency, accuracy, precision, and flexibility. CoralSCOP-LAT, therefore, not only accelerates the coral reef annotation process but also assists users in obtaining high-quality coral reef segmentation and analysis outcomes. Github Page: https://github.com/ykwongaq/CoralSCOP-LAT.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_17

- 相似度：`0.3803`
- 时间差：`-3031` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`261268` / 2014-08-07
- arXiv：`2211.15330` / 2022-11-24
- Grant 标题：Unmanned Aircraft System (UAS) Airspace Integration
- Paper 标题：UAS in the Airspace: A Review on Integration, Simulation, Optimization, and Open Challenges

**Grant Description**

• The objective of this effort is to conduct basic, applied, advanced and demonstration/validation research to develop, demonstrate, integrate and transition new UAS airspace integration technologies to the warfighter.• Tasks may include the following: – Modeling, simulation and analysis of UAS – Trade studies and research of UAS systems, subsystems and interfaces– Verification, validation and safety analysis– Concept and component research and development, including software and/or hardware – Human-machine interface research and development– Develop, conduct and/or support ground or flight tests• Calls under this BAA will fall under six research areas in AFRL/RQQ: Airspace Integration; State Awareness and Real Time Response; Verification & Validation; Cooperative Intelligence; Surveillance and Reconnaissance; Automated Strike Integration and Safety Technologies • Calls under this BAA may be standalone efforts in one or multiple research areas, or in support of a larger effort. Each individual call will specify its own goals, objectives and deliverables.

**arXiv Abstract**

Air transportation is essential for society, and it is increasing gradually due to its importance. To improve the airspace operation, new technologies are under development, such as Unmanned Aircraft Systems (UAS). In fact, in the past few years, there has been a growth in UAS numbers in segregated airspace. However, there is an interest in integrating these aircraft into the National Airspace System (NAS). The UAS is vital to different industries due to its advantages brought to the airspace (e.g., efficiency). Conversely, the relationship between UAS and Air Traffic Control (ATC) needs to be well-defined due to the impacts on ATC capacity these aircraft may present. Throughout the years, this impact may be lower than it is nowadays because the current lack of familiarity in this relationship contributes to higher workload levels. Thereupon, the primary goal of this research is to present a comprehensive review of the advancements in the integration of UAS in the National Airspace System (NAS) from different perspectives. We consider the challenges regarding simulation, final approach, and optimization of problems related to the interoperability of such systems in the airspace. Finally, we identify several open challenges in the field based on the existing state-of-the-art proposals.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_18

- 相似度：`0.3797`
- 时间差：`1362` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`349929` / 2023-08-19
- arXiv：`1911.11779` / 2019-11-26
- Grant 标题：WINDOWS ON THE UNIVERSE: THE ERA OF MULTI-MESSENGER ASTROPHYSICS
- Paper 标题：Enabling real-time multi-messenger astrophysics discoveries with deep learning

**Grant Description**

The Universe is the ultimate laboratory, and we can now probe it as never before through several powerful and diverse windows – electromagnetic waves, high-energy particles, and gravitational waves. Each of these windows provides a different view. Together they reveal a detailed picture of the Universe that will allow us to study matter, energy, and the cosmos in fundamentally new ways. The “Windows on the Universe” Multi-Messenger Astrophysics (WoU-MMA) program identifies three categories of messengers - electromagnetic waves, high-energy particles including neutrinos and cosmic rays, and gravitational waves. The goals of WoU-MMA are to build the capabilities and accelerate the synergy between observations and theory to realize integrated, multi-messenger astrophysical explorations of the Universe. The WoU-MMA program welcomes proposals in any area of research supported through the participating divisions that address at least one of the following criteria: Coordination: Activities to coordinate observations involving more than one messenger. Observations: Observations of astrophysical objects or phenomena that are potentially sources of more than one messenger. Interpretation: Theory, experiment, simulations and other activities to understand or interpret observations of astrophysical objects that are sources of more than onemessenger. Competitive proposals will accelerate the progress in multi-messenger astrophysics and advance the community activities that have been developed during the initial five-year period of the WoU-MMA program. These build on observational and analysis capabilities at the intersection of the explorations enabled by each of the three windows. Efforts to integrate research communities to develop full interoperability between the three windows, and to develop a skilled new workforce in this field, are also encouraged. Proposals should be submitted to the relevant programs listed below (see Related Programs). The WoU-MMA program is not intended to replace existing programs that make awards that involve experimental or theoretical efforts related to each of the three messengers. Rather, the WoU-MMA program is meant to fund awards that have significant components of multi-messenger astrophysics. Priority will be given to proposals for dedicated efforts that significantly advance the WoU-MMA goals. A proposal that is requesting consideration within the context of WoU-MMA should begin the title with the identifying acronym "WoU-MMA:". PIs should ask for consideration and review as a WoU-MMA proposal only if the proposal addresses at least one of the criteria listed above. Proposals marked for consideration by the WoU-MMA program that do not address at least one of these criteria will be reviewed solely within the participating program(s) to which they were submitted. Supplement requests to existing awards within a program that address one of the above criteria will also be considered.

**arXiv Abstract**

Multi-messenger astrophysics is a fast-growing, interdisciplinary field that combines data, which vary in volume and speed of data processing, from many different instruments that probe the Universe using different cosmic messengers: electromagnetic waves, cosmic rays, gravitational waves and neutrinos. In this Expert Recommendation, we review the key challenges of real-time observations of gravitational wave sources and their electromagnetic and astroparticle counterparts, and make a number of recommendations to maximize their potential for scientific discovery. These recommendations refer to the design of scalable and computationally efficient machine learning algorithms; the cyber-infrastructure to numerically simulate astrophysical sources, and to process and interpret multi-messenger astrophysics data; the management of gravitational wave detections to trigger real-time alerts for electromagnetic and astroparticle follow-ups; a vision to harness future developments of machine learning and cyber-infrastructure resources to cope with the big-data requirements; and the need to build a community of experts to realize the goals of multi-messenger astrophysics.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_19

- 相似度：`0.3741`
- 时间差：`360` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`339438` / 2022-04-14
- arXiv：`2104.11079` / 2021-04-19
- Grant 标题：Randomized Algorithms for Combinatorial Scientific Computing
- Paper 标题：Randomized Algorithms for Scientific Computing (RASC)

**Grant Description**

The DOE SC program in Advanced Scientific Computing Research (ASCR) hereby announces its interest in basic research in the design, development, analysis, and scalability of randomized algorithms for the challenging discrete and combinatorial problems that arise in the Department’s energy, environmental, and national security mission areas.

**arXiv Abstract**

Randomized algorithms have propelled advances in artificial intelligence and represent a foundational research area in advancing AI for Science. Future advancements in DOE Office of Science priority areas such as climate science, astrophysics, fusion, advanced materials, combustion, and quantum computing all require randomized algorithms for surmounting challenges of complexity, robustness, and scalability. This report summarizes the outcomes of that workshop, "Randomized Algorithms for Scientific Computing (RASC)," held virtually across four days in December 2020 and January 2021.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### CS_20

- 相似度：`0.3723`
- 时间差：`-5105` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`46296` / 2009-03-24
- arXiv：`2303.09603` / 2023-03-16
- Grant 标题：Algebra, Number Theory, and Combinatorics
- Paper 标题：Rigorous Analytic Combinatorics in Several Variables in SageMath

**Grant Description**

Supports research in algebra, including algebraic structures, general algebra, and linear algebra; number theory, including algebraic, analytic number theory, arithmetic geometry, quadratic forms, and automorphic forms; combinatorics, including graph theory; and algebraic geometry.

**arXiv Abstract**

We introduce the new sage_acsv package for the SageMath computer algebra system, allowing users to rigorously compute asymptotics for a large variety of multivariate sequences with rational generating functions. Using Sage's support for exact computations over the algebraic number field, this package provides the first rigorous implementation of algorithms from the theory of analytic combinatorics in several variables.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

### env_energy

#### ENV_ENERGY_01

- 相似度：`0.4391`
- 时间差：`-24` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`332386` / 2021-03-26
- arXiv：`2104.11079` / 2021-04-19
- Grant 标题：EXPRESS: Randomized Algorithms for Extreme-Scale Science
- Paper 标题：Randomized Algorithms for Scientific Computing (RASC)

**Grant Description**

The DOE SC program in Advanced Scientific Computing Research (ASCR) hereby announces its interest in research applications to explore potentially high-impact approaches in the development and use of randomized algorithms for scientific computing and extreme-scale science

**arXiv Abstract**

Randomized algorithms have propelled advances in artificial intelligence and represent a foundational research area in advancing AI for Science. Future advancements in DOE Office of Science priority areas such as climate science, astrophysics, fusion, advanced materials, combustion, and quantum computing all require randomized algorithms for surmounting challenges of complexity, robustness, and scalability. This report summarizes the outcomes of that workshop, "Randomized Algorithms for Scientific Computing (RASC)," held virtually across four days in December 2020 and January 2021.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_02

- 相似度：`0.4293`
- 时间差：`-3530` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`233281` / 2013-05-06
- arXiv：`2301.01756` / 2023-01-04
- Grant 标题：FY 2013 Methane Hydrates
- Paper 标题：Dynamic Viscosity of Methane and Carbon Dioxide Hydrate Systems from Pure Water at High-Pressure Driving Forces

**Grant Description**

The objective of this Funding Opportunity Announcement is to fund research that advances the current state of knowledge or technology with respect to methane hydrate science focusing on characterization of gas hydrate deposits, response of methane hydrate systems to natural environmental change, and response of gas hydrate reservoirs to induced environmental change to determine the potential of methane hydrates as a potential energy resource and their role in the natural environment.

**arXiv Abstract**

The viscosity of methane and carbon dioxide hydrate systems were measured using a high-pressure rheometer up to 30 MPag. Where hydrate formation was not detected, the effect of temperature on the viscosity was one order of magnitude higher than the pressure effect on viscosity in most of the experimental pressure range (-0.048 mPa s/C at 1 MPag and 0.009 mPa s/MPag at 2C). The pressure effect on the viscosity of carbon dioxide systems where no hydrate formation was observed was up to one order of magnitude higher than that of the methane systems, due to carbon dioxide's higher solubility in water. Novel rheological phases diagrams were developed to further characterize the gas hydrate systems. Several systems with high driving forces for hydrate formation (2.07 MPag to 4.1 MPag) did not form gas hydrates. System limitations to the formation of hydrates were categorized as kinetic, mass diffusion, and/or heat of crystallization effects.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_03

- 相似度：`0.4271`
- 时间差：`-3299` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`44089` / 2008-05-02
- arXiv：`1705.05025` / 2017-05-14
- Grant 标题：Stem Cells and Cancer (R21)
- Paper 标题：Complexity in cancer stem cells and tumor evolution: towards precision medicine

**Grant Description**

Purpose. This funding opportunity announcement (FOA), issued by the National Cancer Institute (NCI), and the National Institute on Aging (NIA), encourages research in all aspects of tumor stem cell biology, including the molecular and biochemical regulation of embryonic and adult stem cell behavior relevant to tumor formation. Tumor stem cells are a rare population of cells that can recapitulate all the cell types represented in the original tumor. Tumor stem cells are capable of self-renewal and asymmetric cell division. These cells are putatively responsible for the transplantability and metastatic properties of tumors. This FOA intends to stimulate efforts on isolation and characterization of tumor stem cells from a large spectrum of tumors. Such studies are important in order to understand the progression of malignant diseases. They may also inspire the development of new therapeutic strategies based on specific targeting of tumor stem cells. In addition, more research is encouraged to understand the genetic and biochemical regulatory mechanisms that control the self-renewal phenotype, asymmetric cell division, and the stem cell microenvironment (or niche ). It is anticipated that the results of such research will ultimately improve the specificity and long-term effectiveness of cancer therapy.

**arXiv Abstract**

In this review, we discuss recent advances on the plasticity of cancer stem cells and highlight their relevance to understand the metastatic process and to guide therapeutic interventions. Recent results suggest that the strict hierarchical structure of cancer cell populations advocated by the cancer stem cell model must be reconsidered since the depletion of cancer stem cells leads the other tumor cells to switch back into the cancer stem cell phenotype. This plasticity has important implications for metastasis since migrating cells do not need to be cancer stem cells in order to seed a metastasis. We also discuss the important role of the immune system and the microenvironment in modulating phenotypic switching and suggest possible avenues to exploit our understanding of this process to develop an effective strategy for precision medicine.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_04

- 相似度：`0.4194`
- 时间差：`360` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`339438` / 2022-04-14
- arXiv：`2104.11079` / 2021-04-19
- Grant 标题：Randomized Algorithms for Combinatorial Scientific Computing
- Paper 标题：Randomized Algorithms for Scientific Computing (RASC)

**Grant Description**

The DOE SC program in Advanced Scientific Computing Research (ASCR) hereby announces its interest in basic research in the design, development, analysis, and scalability of randomized algorithms for the challenging discrete and combinatorial problems that arise in the Department’s energy, environmental, and national security mission areas.

**arXiv Abstract**

Randomized algorithms have propelled advances in artificial intelligence and represent a foundational research area in advancing AI for Science. Future advancements in DOE Office of Science priority areas such as climate science, astrophysics, fusion, advanced materials, combustion, and quantum computing all require randomized algorithms for surmounting challenges of complexity, robustness, and scalability. This report summarizes the outcomes of that workshop, "Randomized Algorithms for Scientific Computing (RASC)," held virtually across four days in December 2020 and January 2021.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_05

- 相似度：`0.4141`
- 时间差：`-3159` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`55983` / 2010-07-20
- arXiv：`1903.05993` / 2019-03-14
- Grant 标题：Harmful Algal Bloom Programs
- Paper 标题：Cooperative decentralized circumnavigation with application to algal bloom tracking

**Grant Description**

National Centers for Coastal Ocean Centers (NCCOS)/Center for Sponsored Coastal Ocean Research (CSCOR) is soliciting proposals for the Ecology and Oceanography of Harmful Algal Blooms Program, the Monitoring and Event Response for Harmful Algal Blooms Program and the Prevention, Control and Mitigation of Harmful Algal Blooms Program. Background information about the NCCOS/CSCOR efforts can be found at http://www.cop.noaa.gov. Proposals should be submitted through Grants.gov http://www.grants.gov/.

**arXiv Abstract**

Harmful algal blooms occur frequently and deteriorate water quality. A reliable method is proposed in this paper to track algal blooms using a set of autonomous surface robots. A satellite image indicates the existence and initial location of the algal bloom for the deployment of the robot system. The algal bloom area is approximated by a circle with time varying location and size. This circle is estimated and circumnavigated by the robots which are able to locally sense its boundary. A multi-agent control algorithm is proposed for the continuous monitoring of the dynamic evolution of the algal bloom. Such algorithm comprises of a decentralized least squares estimation of the target and a controller for circumnavigation. We prove the convergence of the robots to the circle and in equally spaced positions around it. Simulation results with data provided by the SINMOD ocean model are used to illustrate the theoretical results.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_06

- 相似度：`0.4126`
- 时间差：`-883` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`336125` / 2021-10-13
- arXiv：`2403.09848` / 2024-03-14
- Grant 标题：Staff Support for Regional State Engagement with the U.S. Department of Energy - Office of Integrated Waste Management on Radioactive Materials Transportation Planning
- Paper 标题：Implementation of Parallel Process Execution in the Next Generation System Analysis Model

**Grant Description**

The purpose of this Cooperative Agreement between the U.S. Department of Energy (DOE), Office of Nuclear Energy (NE), Office of Integrated Waste Management (DOE-IWM) and [TBD] hereinafter referred to as the “Recipient” is to facilitate engagement between State government officials in one of the four (4) specific regions: Eastern Region, Western Region, Midwestern Region or Southern Region of the United States and DOE-IWM in planning for future large-scale DOE transportation of commercial spent nuclear fuel (SNF) and high-level radioactive waste (HLW) to storage and disposal facilities, when such facilities become available, and related DOE program issues that may impact a State or region. This facilitation is an essential component of developing and implementing a successful large-scale SNF transportation program that is safe, secure, and that merits public trust and confidence.

**arXiv Abstract**

The United States DOE Office of Integrated Waste Management program is planning for the transportation, storage, and eventual disposal of spent nuclear fuel and high-level radioactive waste from nuclear power plant sites across the United States. The Next Generation System Analysis Model is an agent-based simulation toolkit that is used for system level simulation and analysis of the SNF inventory in the United States. This tool was developed as part of a collaborative effort between Argonne National Laboratory and Oak Ridge National Laboratory. The analyst using NGSAM has the ability to define several factors like the number of storage facilities, capacity at each facility, transportation schedules, shipment rates, and other conditions. The primary purpose of NGSAM is to provide the system analyst with the tools to model the integrated waste management system and gain insights on waste management alternatives, impact of storage choices, generating cost estimates, and developing an integrated approach with emphasis on flexibility.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_07

- 相似度：`0.4099`
- 时间差：`-1149` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`321621` / 2019-10-16
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：Coral Reef and Natural Resources Program
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

The Coral Reef and Natural Resources Initiative provides grant funding for management and protection of coral reefs and combat invasive species in the U.S. insular areas.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_08

- 相似度：`0.4059`
- 时间差：`1879` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`291618` / 2017-02-06
- arXiv：`1112.3991` / 2011-12-16
- Grant 标题：Cooperative Ecosystem Studies Unit (CESU), Rocky Mountain CESU
- Paper 标题：Short and Long Range Population Dynamics of the Monarch

**Grant Description**

The USGS is offering a funding opportunity to a CESU partner for research on refining our understanding of the amounts and types of land cover change in monarch butterfly migratory habitat in Mexico. The Eastern population of monarch butterflies has experienced declines over the last two decades. A leading hypothesis for the decline is the loss of breeding habitats in the central US. However, others have suggested declines in habitat that supports both northward and southward migration in Mexico and Texas may be impacting the population. Analysis of land cover change in the central US exist, and USGS is currently working on a change analysis for Texas. However, a similar analysis in Mexico does not exist and is needed to understand the rates and types of land change taking place across the entire migratory range of the eastern monarch butterfly population. Remotely sensed data products for Mexico differ from those available in the US and an assessment of what data are available and how they can be used to address a change analysis of monarch migratory habitat in Mexico may be required.

**arXiv Abstract**

The monarch butterfly annually migrates from central Mexico to southern Canada. During recent decades, its population has been reduced due to human interaction with their habitat. We examine the effect of herbicide usage on the monarch butterfly's population by creating a system of linear and non-linear ordinary differential equations that describe the interaction between the monarch's population and its environment at various stages of migration: spring migration, summer loitering, and fall migration. The model has various stages that are used to describe the dynamics of the monarch butterfly population over multiple generations. In Stage 1, we propose a system of coupled ordinary differential equations that model the populations of the monarch butterflies and larvae during spring migration. In Stage 2, we propose a predator-prey model with age structure to model the population dynamics at the summer breeding site. In Stages 3 and 4, we propose exponential decay functions to model the monarch butterfly's fall migration to central Mexico and their time at the overwintering site. The model is used to analyze the long-term behavior of the monarch butterflies through numerical analysis, given data available in the research literature.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_09

- 相似度：`0.4040`
- 时间差：`-2209` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`261549` / 2014-08-11
- arXiv：`2008.12461` / 2020-08-28
- Grant 标题：BLM&apos;s Unmanned Aircraft Systems (UAS) Resource Management Operations
- Paper 标题：Counter-Unmanned Aircraft System(s) (C-UAS): State of the Art, Challenges and Future Trends

**Grant Description**

BLM's Unmanned Aircraft Systems (UAS) Resource Management Operations

**arXiv Abstract**

Unmanned aircraft systems (UAS), or unmanned aerial vehicles (UAVs), often referred to as drones, have been experiencing healthy growth in the United States and around the world. The positive uses of UAS have the potential to save lives, increase safety and efficiency, and enable more effective science and engineering research. However, UAS are subject to threats stemming from increasing reliance on computer and communication technologies, which place public safety, national security, and individual privacy at risk. To promote safe, secure and privacy-respecting UAS operations, there is an urgent need for innovative technologies for detecting, tracking, identifying and mitigating UAS. A Counter-UAS (C-UAS) system is defined as a system or device capable of lawfully and safely disabling, disrupting, or seizing control of an unmanned aircraft or unmanned aircraft system. Over the past 5 years, significant research efforts have been made to detect, and mitigate UAS: detection technologies are based on acoustic, vision, passive radio frequency, radar, and data fusion; and mitigation technologies include physical capture or jamming. In this paper, we provide a comprehensive survey of existing literature in the area of C-UAS, identify the challenges in countering unauthorized or unsafe UAS, and evaluate the trends of detection and mitigation for protecting against UAS-based threats. The objective of this survey paper is to present a systematic introduction of C-UAS technologies, thus fostering a research community committed to the safe integration of UAS into the airspace system.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_10

- 相似度：`0.4039`
- 时间差：`-1648` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`305874` / 2018-06-04
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：Coral Reef and Natural Resources Program 2018
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

The Coral Reef and Natural Resources Initiative provides grant funding for management and protection of coral reefs and combat invasive species in the U.S. insular areas.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_11

- 相似度：`0.4038`
- 时间差：`-1371` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`313593` / 2019-03-08
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：Coral Reef and Natural Resources Program 2019
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

The Coral Reef and Natural Resources Initiative provides grant funding for management and protection of coral reefs and combat invasive species in the U.S. insular areas.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_12

- 相似度：`0.4035`
- 时间差：`-702` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`330685` / 2021-01-05
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：Coral Reef and Natural Resources Program 2021
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

The Coral Reef and Natural Resources Initiative provides grant funding for management and protection of coral reefs and to combat invasive species in the U.S. insular areas.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_13

- 相似度：`0.4034`
- 时间差：`-373` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`336758` / 2021-11-30
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：OIA Coral Reef and Natural Resources Program 2022
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

The Coral Reef and Natural Resources Initiative provides grant funding for management and protection of coral reefs and to combat invasive species in the U.S. insular areas.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_14

- 相似度：`0.4033`
- 时间差：`-2858` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`273729` / 2015-02-10
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：Coral Reef Initiative Program
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

Coral Reef Initiative Program provides grant funding for management and protection of coral reef in the insular areas. Highest priority will be given to proposals that support local and regional priorities for protection and sustainable use of coral reefs.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_15

- 相似度：`0.4033`
- 时间差：`-2547` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`280623` / 2015-12-18
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：Coral Reef Initiative Program
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

Coral Reef Initiative Program provides grant funding for management and protection of coral reef in the insular areas. Highest priority will be given to proposals that support local and regional priorities for protection and sustainable use of coral reefs.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_16

- 相似度：`0.4030`
- 时间差：`-66` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`343884` / 2022-10-03
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：OIA Coral Reef and Natural Resources Program 2023
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

The Coral Reef and Natural Resources Initiative provides grant funding for management and protection of coral reefs and to combat invasive species in the U.S. insular areas.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_17

- 相似度：`0.4026`
- 时间差：`2592` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`249237` / 2013-12-13
- arXiv：`physics/0611083` / 2006-11-08
- Grant 标题：Clean Energy Activities- Addendum under APS No.: APS-OAA-13-00003
- Paper 标题：Fractal Dimensionof the El Salvador Earthquake (2001) time Series

**Grant Description**

USAID/El Salvador is seeking concept papers for clean energy initiatives in the Central American region.

**arXiv Abstract**

We have estimated multifractal spectrum of the El Salvador earthquake signal recorded at different locations.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_18

- 相似度：`0.4023`
- 时间差：`322` 天
- arXiv 是否更早：`是`（arXiv更早或同日）
- grant：`350746` / 2023-10-26
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：OIA Coral Reef and Natural Resources Program 2024
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

The Coral Reef and Natural Resources Initiative provides grant funding for management and protection of coral reefs and to combat invasive species in the U.S. insular areas.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_19

- 相似度：`0.4015`
- 时间差：`-1628` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`300280` / 2018-01-25
- arXiv：`2207.04914` / 2022-07-11
- Grant 标题：DARPA Subterranean (SubT) Challenge
- Paper 标题：Team CERBERUS Wins the DARPA Subterranean Challenge: Technical Overview and Lessons Learned

**Grant Description**

The goal of the DARPA Subterranean Challenge is to discover innovations that enable integrated and rapid mapping, navigation, and search of complex environments.

**arXiv Abstract**

This article presents the CERBERUS robotic system-of-systems, which won the DARPA Subterranean Challenge Final Event in 2021. The Subterranean Challenge was organized by DARPA with the vision to facilitate the novel technologies necessary to reliably explore diverse underground environments despite the grueling challenges they present for robotic autonomy. Due to their geometric complexity, degraded perceptual conditions combined with lack of GPS support, austere navigation conditions, and denied communications, subterranean settings render autonomous operations particularly demanding. In response to this challenge, we developed the CERBERUS system which exploits the synergy of legged and flying robots, coupled with robust control especially for overcoming perilous terrain, multi-modal and multi-robot perception for localization and mapping in conditions of sensor degradation, and resilient autonomy through unified exploration path planning and local motion planning that reflects robot-specific limitations. Based on its ability to explore diverse underground environments and its high-level command and control by a single human supervisor, CERBERUS demonstrated efficient exploration, reliable detection of objects of interest, and accurate mapping. In this article, we report results from both the preliminary runs and the final Prize Round of the DARPA Subterranean Challenge, and discuss highlights and challenges faced, alongside lessons learned for the benefit of the community.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

#### ENV_ENERGY_20

- 相似度：`0.3989`
- 时间差：`-2170` 天
- arXiv 是否更早：`否`（arXiv更晚）
- grant：`290986` / 2016-12-29
- arXiv：`2212.04132` / 2022-12-08
- Grant 标题：Coral Reef Initiative Program 2017
- Paper 标题：Combining Photogrammetric Computer Vision and Semantic Segmentation for Fine-grained Understanding of Coral Reef Growth under Climate Change

**Grant Description**

Coral Reef Initiative Program provides grant funding for management and protection of coral reef in the insular areas. Highest priority will be given to proposals that support local and regional priorities for protection and sustainable use of coral reefs.

**arXiv Abstract**

Corals are the primary habitat-building life-form on reefs that support a quarter of the species in the ocean. A coral reef ecosystem usually consists of reefs, each of which is like a tall building in any city. These reef-building corals secrete hard calcareous exoskeletons that give them structural rigidity, and are also a prerequisite for our accurate 3D modeling and semantic mapping using advanced photogrammetric computer vision and machine learning. Underwater videography as a modern underwater remote sensing tool is a high-resolution coral habitat survey and mapping technique. In this paper, detailed 3D mesh models, digital surface models and orthophotos of the coral habitat are generated from the collected coral images and underwater control points. Meanwhile, a novel pixel-wise semantic segmentation approach of orthophotos is performed by advanced deep learning. Finally, the semantic map is mapped into 3D space. For the first time, 3D fine-grained semantic modeling and rugosity evaluation of coral reefs have been completed at millimeter (mm) accuracy. This provides a new and powerful method for understanding the processes and characteristics of coral reef change at high spatial and temporal resolution under climate change.

**你的评价**

- 主题相关性：
- 细粒度匹配度：
- 时序合理性：
- 总体判断：
- 主要误差类型：
- 是否保留为后续评估样本：
- 评语：

