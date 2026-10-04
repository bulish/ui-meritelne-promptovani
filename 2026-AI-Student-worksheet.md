# AI Student worksheet

Complete this worksheet before full data collection. Submit the initial version with the proposal and the completed version with the final report.

## A. Project identity

**Project title:** Sumarizace odborných článků a porovnání s autorskými abstrakty (Summarization of scientific articles and comparison with author abstracts)

**Team members:** Libuše Babičková, Jakub Procházka (xproch40), Jan Kostrhun

**Roles:**
- Libuše Babičková – dataset coordination, and data collection (Perplexity)
- Jakub Procházka (xproch40) – prompt design, and data collection (Claude, Gemini)
- Jan Kostrhun – metrics and analysis, and data collection (ChatGPT)
- All three members participate in human evaluation and writing the final report

**Primary track:**

- [x] Track B: Source-based research — summarizing a scientific article, grounded in verifiable references to the article's content

**Project scope:**

- [x] The goal is not just to produce a summary — it is to generate an AI summary of a scientific article **and then compare it against the article's own author abstract**, measuring how much they semantically agree or diverge
- [x] Capability under test: producing a continuous English-language summary (150–200 words) of a scientific article's goal, methods, main results, and conclusions, suitable for this comparison
- [x] Faithfulness of the summary to the article itself is checked separately from semantic similarity to the abstract
- [x] Conclusions are scoped to this corpus (MENDELU-linked articles) and to the specific product versions recorded during data collection

**Worksheet version and date:** V1, 3.10.2026

---

## B. Research question

**Primary research question:**

How do ChatGPT, Gemini, Claude, and Perplexity differ in the semantic agreement between their summaries of scientific articles linked to MENDELU and the articles' own author abstracts, measured with BERTScore F1, and to what extent do a structured prompt and an optimized prompt improve on this compared with a common baseline prompt?

**Capability being measured:**

The core measured capability is **how closely an AI-generated summary of a scientific article agrees with the article's own author-written abstract** — i.e., producing the summary is only the first step; the actual object of study is the degree of semantic agreement or divergence between the AI summary and the abstract, compared across systems (ChatGPT, Gemini, Claude, Perplexity) and across prompt conditions (baseline/structured/optimized). Faithfulness of the summary to the underlying article itself is verified separately, since the abstract may not capture every important detail of the article and a close match to the abstract does not by itself guarantee correctness.

**Primary hypothesis:**

- **H1:** Under matched conditions (same input without the abstract, a common protocol for web-based source use, and the same length requirement), the structured prompt will achieve a higher mean BERTScore F1 than the baseline prompt across the systems tested, because it explicitly directs the summary toward goal, methods, results, and conclusions. H1 is considered supported only if the positive paired difference also holds on the 10 held-out test cases, with a 95% bootstrap interval entirely above zero.
- **H2 (secondary):** Under the same conditions, the optimized prompt will achieve a higher mean BERTScore F1 than the structured prompt, because it removes recurring errors identified on the development and validation data. Support is judged by the same rule on the test set.

**Alternative explanation:**

A higher score could arise from greater vocabulary/style overlap with the abstract, or from the model having memorized a publicly available article, without any real improvement in factual correctness. This is why BERTScore changes are cross-checked against human ratings and SummaC.

**What result would challenge our hypothesis?**

A zero or negative difference on the held-out test set would challenge the hypotheses; a bootstrap interval that includes zero is treated as inconclusive. A drop in faithfulness alongside a higher BERTScore would also limit the practical interpretation of a "positive" result.

---

## C. Measurement target

**Operational definition:**

The measured quantity is the degree of semantic agreement between a continuous English-language AI summary of 150–200 words, covering the article's goal, methods, main results, and conclusions, produced without access to the article's own abstract, and that article's actual author-written abstract. The summary itself is an intermediate output; the comparison against the abstract (via BERTScore F1, with ROUGE-L and SummaC-Conv as secondary checks) is the actual measurement target of the study.

**Unit of analysis:**

- [x] Unit of task: one article
- [x] Unit of measurement: the output of a given system, under a given prompt condition, for a given repetition

**Primary metric:** BERTScore F1

**Secondary metrics:**

- SummaC-Conv: Measures factual consistency via entailment between the generated summary claims and the source article text.

- ROUGE-L F1: Measures exact lexical overlap (longest common subsequence) between the generated summary and the abstract.

- Human evaluation: Manual scoring (1–5 scale) assessing faithfulness to the article, coverage of key information, and correctness of source-based support.

**Why is it valid?**

It compares the summary with the abstract using contextual token embeddings, which captures semantic similarity even when wording differs (unlike purely lexical overlap).

**What important quality dimension does it fail to capture?**

BERTScore does not establish factual truthfulness — a summary can be semantically close to the abstract while still containing factual errors or unsupported claims. Factual consistency is covered separately by SummaC-Conv and by human rating.

---

## D. Systems and conditions

| System | Interface/API | Visible model/version | Tools enabled | Prompt adaptations | Date tested |
| --- | --- | --- | --- | --- | --- |
| ChatGPT | Standard consumer web interface | To be recorded at time of testing | Each system's own standard web/source tools, per the common protocol | Same input (abstract removed) + link to the original article; may verify claims only against this source, not the abstract or other summaries | TBD |
| Gemini | Standard consumer web interface | To be recorded at time of testing | Same as above | Same as above | TBD |
| Claude | Standard consumer web interface | To be recorded at time of testing | Same as above | Same as above | TBD |
| Claude Code | Not used in this study | — | — | — | — |
| Grok | Not used in this study | — | — | — | — |
| Perplexity | Standard consumer web interface | To be recorded at time of testing | Same as above | Same as above | TBD |

**Comparison design:**

- [x] Product-capability design: each system uses its own ordinary web tools under one shared protocol (no attempt to equalize underlying model access); every run starts a fresh conversation with a single user turn, memory disabled where possible

**What cannot be made equal?**

Web search/retrieval capability, prior exposure to the article during training, and exact prompt phrasing (as each interface may require slight instructional tweaks to properly access the linked source) differ across products and cannot be equalized.

**How will this limitation affect interpretation?**

Results are interpreted as a comparison of the overall consumer products (including their search behavior and required product-specific prompting), rather than a strictly controlled comparison of underlying model capability on an identical text string.

---

## E. Data and test-set plan

**Total cases:** 40 articles × 4 systems × 3 prompt conditions = 480 outputs, plus 24 planned repeated-run outputs (2 held-out test articles × 4 systems × 3 prompts, each run twice)

**Development cases:** 20 articles

**Validation cases:** 10 articles

**Held-out test cases:** 10 articles

**Repeated-run cases:** 24 (repeat runs restricted to 2 pre-selected held-out test articles, across all system × prompt combinations)

| Stratum | Planned number | Actual number | How selected |
| --- | --- | --- | --- |
| Ordinary |  |  | Remainder of the 40 articles after edge cases are set aside |
| Difficult |  |  | Included within the "edge or adversarial" stratum below |
| Edge or adversarial | ≥8 articles (20%), split 4/2/2 across dev/validation/test |  | Long context, rare terminology, complex quantitative findings, or ambiguous conclusions |
| Ambiguous or incomplete | (subset of the edge/adversarial stratum above) |  | Articles with ambiguous conclusions |
| Czech | 0 |  | Not used — corpus restricted to English to avoid conflating translation with summarization |
| English | 40 |  | All articles and abstracts are English |
| Mixed language | 0 |  | Not used |
| Other relevant stratum | — |  | Stratified also by field/discipline and article length |

**Data provenance:**

40 scientific articles linked to MENDELU, with verified permission for the intended processing and for sharing with the class; public availability alone is not treated as sufficient license.

**Why is this dataset representative of the intended use?**

It samples across discipline, length, and difficulty within the MENDELU-linked literature, including a stratified ~20% share of realistic edge cases, to reflect the range of articles for which a user would plausibly want an AI summary and would want to know how closely it matches the official abstract.

**What leakage or contamination risks exist?**

A system's web search could surface the article's own abstract (which is otherwise withheld), creating a reference-leakage risk; visible sources and any protocol violations will be logged, though this risk cannot be fully ruled out. Prior memorization of publicly available articles from model training is a related risk.

---

## F. Prompt protocol

#### Common baseline prompt

```
Summarize the following scientific article in English in 150–200 words. Use the supplied article and its linked full text only; do not use its abstract or other summaries. After the summary, list source sections supporting your main claims.
```

#### Structured prompt

```
Role: Act as an expert academic researcher and science communicator.

Context: You are extracting core information from a scientific article to create a precise summary for a research database. Your summary will be evaluated on its strict factual adherence to the provided text.

Task: Summarize the provided scientific article in English in 150–200 words. 

Guidelines:
- Structure the text to explicitly capture the article's Goal, Methods, Main results, and Conclusions.
- Preserve specific numbers, statistics, and technical/domain terms exactly as they appear.
- Use the supplied article and its linked full text strictly. Do not use its abstract or other summaries.
- Do not rely on outside/external knowledge and do not invent information missing from the article.

Output format: 
1. The 150-200 word summary.
2. A bulleted list of specific source sections or passages from the article that support your main claims.
```

#### Optimized prompt

```
[To be finalized: a revision of the structured prompt, adjusting the Role, Context, Task, or Guidelines based only on errors observed in the development and validation sets. Changes will be logged (see section G) and one common optimized version will be frozen before the held-out test set is opened.]
```

**What remains constant?**

The underlying article text (abstract and other summaries removed), the core task (summarization), the 150–200 word length requirement, and the requirement to support claims with a reference to the source.

**What is intentionally different?**

The baseline prompt is a naive, zero-shot instruction. The structured prompt introduces standardized prompt engineering practices: it assigns a specific Role (expert researcher) and Context (database entry evaluated on adherence), defines explicit Guidelines (goal/methods/results/conclusions, preserving numbers/terms, no outside knowledge), and separates the Output format. The optimized prompt will further refine this standardized structure based on observed dev/validation errors.

**When will prompts be frozen?**

The optimized prompt is frozen as a single common version, chosen from at most three candidates on the validation set, before the held-out test set is opened for final evaluation.

**How will held-out cases remain protected?**

The 10 held-out test articles are not used for prompt tuning at any stage; they are reserved for a one-time final evaluation of the frozen protocol, and are kept separate from the development materials in storage.

---

## G. Prompt-change log

| Version | Date | Change | Evidence | Expected effect | Actual validation effect | Retained? |
| --- | --- | --- | --- | --- | --- | --- |
| v0 | TBD (doplň datum zafixování baseline) | Baseline prompt established (see section F) | Initial design, not yet data-driven | — | — | — |
| v1 | 4. 10. 2026 | Minimal revision of the structured prompt (Guidelines only; Role, Context and Output format unchanged): (1) space allocation given as approximate word budgets (Goal 25, Methods 35, Main results 90, Conclusions 30; about 180 in total) with a hard 200-word cap and the source list excluded from the count; (2) Methods limited to the overall approach, no enumeration of individual procedures; (3) Main results prioritise the study's own quantitative findings over background, constraints and recommendations, with exact numbers, units and referents and no invented numbers; (4) Conclusions state the authors' central conclusion or practical implication and carry their recommendations. | Pilot, 3 dev articles, Perplexity. Baseline prompt: E01, E02 (Case 1), E04 (Case 2), E06 (Case 3). Structured prompt, same articles, one run each: E07 and E13 (methodology over-specified / uneven emphasis persist), E10 (constraints and proposals fill 45% of Main results in Case 1), E08, E11, E14 (all three summaries exceed 200 words: 227, 214, 204); quantitative findings retained in all three cases (E09, E12). Limitation: one system, three articles, one run each. | Summaries within 150–200 words; lower share of Methods; recommendations moved from Main results to Conclusions; retained numerical findings not lost; no increase in unsupported claims or numerical errors. | Not yet tested on the validation set. Sanity check on the 3 pilot articles, one run each (not a validation result): Methods share fell (Case 3: 30% to 21%; Case 2: 38% to 23%), recommendations moved to Conclusions (Case 1), Case 2 within the word limit (176 words); Cases 1 and 3 still above 200 words (215 and 211), constraints remained in Main results (Case 1), and word budgets were printed as headings (Case 2).  | TBD (candidate 1 of max. 3) |
| v2 | | | | | | |
| v3 | | | | | | |

---

## H. Evaluation plan

| Metric | Primary/secondary | Automatic/human/judge | Calculation | Calibration or validation | Limitation |
| --- | --- | --- | --- | --- | --- |
| BERTScore F1 | Primary | Automatic | Compares summary to abstract via contextual token embeddings | Checked for correct functioning on the development set; model/library versions, tokenization, segmentation, and scoring settings frozen before testing | Does not establish truthfulness of the summary |
| SummaC-Conv | Secondary | Automatic | Compares summary to the source article; estimates factual consistency via entailment between claims | Same freeze as above | May err on technical/domain-specific statements and numbers |
| ROUGE-L F1 | Secondary | Automatic | Compares summary to abstract via longest common subsequence (lexical overlap) | Same freeze as above | Penalizes valid paraphrasing |
|  |  |  |  |  |  |

**Human raters:** All three team members; all rate every final held-out test output, including planned repeats

**Blinding procedure:** System identity and prompt condition are hidden from raters; raters see the article and its abstract

**Response-order randomization:** Yes, presentation order is randomly shuffled

**Inter-rater agreement measure:** Weighted Cohen's kappa, computed per rubric dimension (at least 20% of outputs double-rated independently; disagreements resolved afterward with a third team member, original scores retained)

**LLM-as-judge used?** No

If yes, state judge model, rubric, calibration sample, and known risks:

---

(Not applicable — human rubric only, scored 1–5 on faithfulness to the article, coverage of key information, and correctness of source-based support; anchors: 1 = major distortion or missing key information, 3 = usable summary with partial shortcomings, 5 = accurate, complete, and correctly supported. Rubric examples developed on the development set; analysis covers at least 8 representative cases including both successes and failures.)

---

## I. Failure and retry policy

**What counts as a failed run?**

A missing/empty summary. Outputs that violate the length requirement but are non-empty are still scored, not treated as failures.

**Are retries allowed?**

Only as a planned, pre-registered second run: for 2 pre-selected held-out test articles, every system × prompt combination is run a second time. Unplanned/ad hoc retries are not allowed.

**Maximum retries:**

1 (a single planned repeat run, limited to the 2 selected test articles)

**How will first-attempt and eventual success be reported?**

Failures are kept (not discarded or replaced with a better response) and their likely cause is distinguished. Alongside the scores from available outputs, the count and success rate of outputs (including the first-attempt vs. eventual outcome where repeats apply) will be reported.

**Which product or infrastructure failures will be excluded, and why?**

None are planned for exclusion — all failures are recorded and reported rather than excluded, so that failure patterns remain visible in the results.

---

### J. Logging checklist

- [x] Product/system name
- [x] Visible model name/version
- [x] Interface/API used
- [x] Date tested
- [x] Prompt version used
- [x] Input version used
- [x] Available system instructions (where visible)
- [x] Tools enabled for the run
- [x] Temperature/output-limit settings (where available)
- [x] Number of rounds / tool calls
- [x] Latency
- [x] Cost
- [x] Failures encountered
- [x] Retries (and whether planned or unplanned)
- [x] Human interventions during the run
- [x] Memory setting (on/off)
- [x] Any visible source/citations used by the system

**Storage location:** Shared team folder with access for the team and the instructor; the reference abstracts and the held-out test set are stored separately from the development materials

**Anonymization and data-protection procedure:** Only articles with a license or explicit permission covering this processing and class-sharing are used (public availability alone is not treated as sufficient); contact details are stripped from supplied article text; no confidential materials, research-participant personal data, or access credentials are used; source, license, and any modifications made to each article are logged

---

## K. Pilot review

**Pilot size:** 3 development articles

**What failed in the pilot?**

**Perplexity:** No technical problems occurred. Each article was run once with the baseline prompt, once with the structured prompt and once with the candidate optimized prompt (v1), and all nine runs produced a summary that could be scored. Under the baseline prompt, the problems were at the content level: in Case 1 almost no specific quantitative findings (E01, E02), in Case 2 uneven emphasis between methodology and the central practical finding (E04), and in Case 3 an over-detailed sequence of econometric procedures (E06). Under the structured prompt, quantitative findings were retained in all three cases (E09, E12), but over-detailed methodology (E07) and uneven emphasis (E13) persisted, constraints and proposals filled 45% of Main results in Case 1 (E10), and all three summaries exceeded the 200-word limit (227, 214 and 204 words; E08, E11, E14). Perplexity's own word counts for two of the summaries (185 and 192) were inaccurate.

**Which cases were rewritten or removed?**

**Perplexity:** None. All three pilot articles were kept unchanged.

**Which metric or rubric changes were made?**

**Perplexity:** None. The automatic metrics have not yet been run on the pilot outputs.

**What evidence supports freezing the benchmark?**

**Perplexity:** The common protocol worked for Perplexity on all three articles under both the baseline and the structured prompt without any changes, and the outputs could be scored and their errors assigned to categories (section M). Evidence from the automatic metrics and the human rubric is still pending.

**What remains uncertain?**

**Perplexity:** (1) Each prompt was run only once per article, so differences between the baseline and the structured prompt cannot be separated from run-to-run variation. (2) The evidence comes from one system and three articles. (3) The word count must be computed by the team with a common method (for example, whether section labels are counted), because the model's own counts were inaccurate. (4) The candidate optimized prompt (v1) was run once per article on the same three pilot articles as a sanity check; because these articles were used to design v1, the results are not evidence of its effect, which must be assessed on the development and validation sets. (5) It remains to be confirmed from the run logs whether the visible sources of the pilot runs included the withheld abstract (reference-leakage check).

---

## L. Results table

*(Not filled in — to be completed after data collection, for the final report.)*

| System | Condition | *N* | Primary score | Interval or variation | Secondary score | Median latency | Cost | First-attempt success |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ChatGPT | Baseline |  |  |  |  |  |  |  |
| ChatGPT | Structured |  |  |  |  |  |  |  |
| ChatGPT | Optimized |  |  |  |  |  |  |  |
| Gemini | Baseline |  |  |  |  |  |  |  |
| Gemini | Structured |  |  |  |  |  |  |  |
| Gemini | Optimized |  |  |  |  |  |  |  |
| Claude | Baseline |  |  |  |  |  |  |  |
| Claude | Structured |  |  |  |  |  |  |  |
| Claude | Optimized |  |  |  |  |  |  |  |
| Perplexity | Baseline |  |  |  |  |  |  |  |
| Perplexity | Structured |  |  |  |  |  |  |  |
| Perplexity | Optimized |  |  |  |  |  |  |  |

---

## M. Error analysis

| Error ID | System     | Condition | Task ID | Category                                    | Severity | First attempt? | Description                                                                                                                                                                                                                                              | Likely cause                                                                                                                              | Preventable by prompt? |
| -------- | ---------- | --------- | ------- | ------------------------------------------- | -------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| E01      | Perplexity | Baseline  | Case 1  | Missing quantitative findings               | Medium   | Yes            | The summary describes the importance, advantages, constraints, and recommendations of Vietnam's wood exports, but provides almost no specific quantitative findings, despite the task concerning export performance and market development.              | The baseline prompt does not explicitly require preservation of numerical findings or prioritization of quantitative results.             | Yes                    |
| E02      | Perplexity | Baseline  | Case 1  | Weak results specificity                    | Medium   | Yes            | The Main results content is largely qualitative (advantages, opportunities, constraints, EU requirements) rather than identifying specific measurable findings from the study.                                                                           | The baseline prompt does not explicitly distinguish key results from general background information.                                      | Yes                    |
| E03      | Perplexity | Baseline  | Case 2  | No clear error; positive example            | Low      | Yes            | The summary successfully preserves important quantitative information, including 14 pilot tests and 65 certified operators by March 2022.                                                                                                                | The relevant information was sufficiently salient in the source and was retained despite the baseline prompt.                             | No                     |
| E04      | Perplexity | Baseline  | Case 2  | Uneven emphasis                             | Medium   | Yes            | The summary contains detailed methodology and framework information, while the central practical finding from the abstract (harmonised Pan-European qualifications as a solution to qualification barriers) receives comparatively less direct emphasis. | The baseline prompt does not specify how space should be allocated among goal, methods, results, and conclusions.                         | Yes                    |
| E05      | Perplexity | Baseline  | Case 3  | No clear quantitative omission              | Low      | Yes            | The summary successfully retains important numerical information, including the 1990–2022 study period and the approximately 4.3% annual error-correction adjustment.                                                                                    | The quantitative findings were prominent and/or salient enough to be preserved by the baseline prompt.                                    | No                     |
| E06      | Perplexity | Baseline  | Case 3  | Potential over-specification of methodology | Medium   | Yes            | The summary gives substantial space to the sequence of econometric procedures (VAR lag selection, ADF, Johansen, VECM, and Granger causality), potentially reducing space available for the main substantive findings.                                   | The baseline prompt does not instruct the model to balance methodological detail against substantive results within the fixed word limit. | Yes                    |
| E07 | Perplexity | Structured | Case 3 | Over-specification of methodology (persists from baseline, see E06) | Medium | Yes | The Methods section (69 of 227 words, 30%) lists VAR lag selection, ADF, Johansen, VECM and Granger causality tests plus a Doornik-Hansen normality test, as in the baseline run (E06). Main results open with the outcomes of the unit-root and cointegration tests before the coefficient estimates. | The structured prompt asks for Methods but does not limit procedural detail or balance methods against results within the word limit. | Yes |
| E08 | Perplexity | Structured | Case 3 | Length violation | Medium | Yes | The summary has 227 words (232 including section labels; source list excluded), 27 above the 150–200 limit. | The limit is stated once and nothing asks the model to control length; detailed Methods (69 words) and Main results (96 words) take most of the space. | Yes |
| E09 | Perplexity | Structured | Case 1 | No clear error; positive example (quantitative findings retained) | Low | Yes | Main results contain specific figures (USD 8.52 billion in 2019, USD 12.37 billion in 2020 with +16.2%, exports to more than 120 countries, EU demand of up to USD 85 billion versus Vietnamese exports of about USD 700–800 million). The omission of quantitative findings seen under the baseline prompt (E01) did not recur in this run. | The structured prompt's instruction to preserve specific numbers and statistics. | No |
| E10 | Perplexity | Structured | Case 1 | Weak results specificity (persists in reduced form, see E02) | Medium | Yes | About 45% of Main results (54 of 119 words) lists general constraints (raw materials, certification, scale, finance, technology, EU requirements) and the thesis's proposed solutions rather than measured findings. The proposals appear under Main results instead of Conclusions, and Conclusions is a single sentence of 22 words. | The structured prompt separates the four parts but does not say that recommendations belong to Conclusions or that constraints and background should not fill Main results. | Yes |
| E11 | Perplexity | Structured | Case 1 | Length violation | Medium | Yes | The summary has 214 words (219 including section labels; source list excluded), 14 above the limit. Perplexity labelled it "185 words". Main results take 119 words (56%). | The limit is stated once and nothing asks the model to control length; the model's own word count is inaccurate. | Yes |
| E12 | Perplexity | Structured | Case 2 | No clear error; positive example | Low | Yes | Key numerical information is preserved: over 50 documents reviewed, 30 stakeholder meetings, 14 pilot tests, 65 live candidate tests, 65 operators certified by March 2022, EQF level 4. | The instruction to preserve specific numbers; the figures are salient in the source. | No |
| E13 | Perplexity | Structured | Case 2 | Uneven emphasis (persists from baseline, see E04) | Medium | Yes | Methods take 77 of 204 words (38%), as many as Main results (78 words), while Conclusions take 17 words (8%): one sentence stating that the objectives were achieved and that the qualifications support safety, recognition and worker mobility. Methods also include process steps (contributions of stakeholders, the expert group and training providers to standard setting, pilot testing and qualification development). | The structured prompt does not specify how space should be allocated among the four parts. | Yes |
| E14 | Perplexity | Structured | Case 2 | Length violation | Low | Yes | The summary has 204 words (209 including section labels; source list excluded), 4 above the limit. Perplexity labelled it "192 words". | The limit is stated once and nothing asks the model to control length; the model's own word count is inaccurate. | Yes |
| E15 | Perplexity | Optimized (v1) | Case 3 | No clear error; positive example (methodology no longer enumerated) | Low | Yes | Methods take 45 of 211 words (21%) compared with 69 of 227 (30%) under the structured prompt, and no longer list the individual tests (ADF, Johansen, Granger, Doornik-Hansen); the over-specification seen in E06 and E07 did not recur in this run. | The Methods guideline limiting the description to the overall approach. | No |
| E16 | Perplexity | Optimized (v1) | Case 3 | Length violation (reduced) | Medium | Yes | The summary has 211 words (216 including section labels; source list excluded), 11 above the limit, down from 227 under the structured prompt. Main results take 111 words (53%) against a budget of 90 and add detail not present in the structured run (VAR lag length, the long-run equation with its constant, p-values of the non-significant coefficients). | The instruction to prioritise exact quantitative results competes with the section word budget; the budgets were not respected. | Partly |
| E17 | Perplexity | Optimized (v1) | Case 1 | No clear error; positive example (recommendations moved to Conclusions) | Low | Yes | The proposed solutions now appear in Conclusions (43 words, 20%) instead of Main results, and the share of Main results fell from 56% to 47% of the summary. The two figure series are stated separately with their own growth rates (USD 8.52 billion in 2019, +17.8%; USD 12.37 billion in 2020, +16.2%). | The Conclusions guideline to carry the recommendations; the guideline to state what each figure refers to. | No |
| E18 | Perplexity | Optimized (v1) | Case 1 | Weak results specificity (persists in reduced form, see E02, E10) | Low | Yes | A sentence of general constraints (raw materials, certification, scale, finance, technology, EU requirements; 33 of 101 words, 33%) remains in Main results although the guideline asks to prioritise quantitative results over constraints. | The guideline gives priority to quantitative results but does not prohibit constraints in Main results. | Yes |
| E19 | Perplexity | Optimized (v1) | Case 1 | Length violation | Medium | Yes | The summary has 215 words (220 including section labels; source list excluded), 15 above the limit, unchanged from the structured run (214). All four sections exceed their budget (Goal 32 vs 25, Methods 39 vs 35, Main results 101 vs 90, Conclusions 43 vs 30). | The word budgets and the 200-word cap were not respected. | Partly |
| E20 | Perplexity | Optimized (v1) | Case 2 | No clear error; positive example (within the word limit, better balance) | Low | Yes | The summary has 176 words (189 including the labels as printed), within the limit. Methods take 40 words (23%) compared with 77 (38%) under the structured prompt, Conclusions 32 words (18%) compared with 17 (8%); E13 and E14 did not recur. Key numerical findings are retained. | The allocation and Methods guidelines. | No |
| E21 | Perplexity | Optimized (v1) | Case 2 | Output artefact (word budgets printed as headings) | Low | Yes | The section headings repeat the prompt's budgets ("Goal (25 words)", "Methods (35 words)", "Main results (90 words)", "Conclusions (30 words)"), which do not match the actual counts (26, 40, 78 and 32 words). | The budgets are given in the Guidelines and the model reproduces them as labels. | Yes |

**Most frequent error:**

**Perplexity**

*Baseline:* The most recurrent issue observed in the pilot is **insufficiently specific presentation of the main findings**, particularly the tendency to summarize results qualitatively rather than consistently preserving the most important quantitative findings. However, this pattern is not present in every case: Cases 2 and 3 demonstrate that Perplexity can preserve important numerical findings when they are sufficiently salient.

*Structured:* The most frequent issue was exceeding the 150–200 word limit (3 of 3 runs: 227, 214 and 204 words; the two word counts Perplexity stated itself, 185 and 192, were inaccurate). The second most frequent was an unbalanced distribution of space: Methods took 30% (Case 3) to 38% (Case 2) of the summary, and in Case 1 constraints and proposals filled 45% of Main results. The omission of quantitative findings seen under the baseline prompt did not recur; key numerical findings were retained in all three cases.

*Optimized (v1):* Exceeding the word limit remained the most frequent issue (2 of 3 runs: 215 and 211 words), although Case 2 came within the limit (176 words). The section budgets were exceeded in most sections (for example Main results with 111 and 101 words against 90 in Cases 3 and 1, and Conclusions with 43 words against 30 in Case 1).

**ChatGPT / Gemini / Claude:** TBD (to be added from their pilots).

**Most consequential error:**

**Perplexity**

*Baseline:* The most consequential potential error is **omission of key quantitative findings from the Results section**, because this can substantially reduce the informational value of a research-database summary and make a scientifically specific finding appear only as a general qualitative statement.

*Structured:* The imbalance between methods and results/conclusions (Cases 2 and 3), because it displaces the content that forms the core of the intended summary.

*Optimized (v1):* The instruction to prioritise exact quantitative results, combined with the word budgets, produced additional numerical detail (for example VAR lag length, the long-run equation and p-values in Case 3) that pushed the summary beyond the word limit. Whether the figures and wording that appear only in the v1 runs are supported by the articles was checked separately.

**ChatGPT / Gemini / Claude:** TBD.

**Did optimization change the error distribution?**

**Perplexity**

*Baseline:* Reference condition; no change to report.

*Structured (compared with baseline):* Not yet established. The structured prompt was piloted on the same three articles as the baseline (one run per article). In these runs it did not repeat the omission of quantitative findings in Case 1 (E01), but over-detailed methodology (E06, E07) and uneven emphasis (E04, E13) persisted, and all three runs exceeded the word limit.

*Optimized (v1):* Partly, in these single runs. Compared with the structured prompt, v1 reduced the share of Methods (30% to 21% in Case 3, 38% to 23% in Case 2), did not repeat the enumeration of statistical tests (E06, E07), moved the recommendations from Main results to Conclusions in Case 1 (E10, E18) and brought Case 2 within the word limit. It did not eliminate length violations (Cases 1 and 3), did not remove the constraints from Main results in Case 1 (E19), and in Case 2 it printed the word budgets as headings (E22). Quantitative findings were retained in all three cases. These observations come from one run per article on the pilot articles used to design v1; they are not evidence of a validation effect and must be confirmed on the development and validation sets.

**ChatGPT / Gemini / Claude:** TBD.

---

---

## N. Practical recommendation

*(Not filled in — depends on results; to be completed for the final report.)*

**Best system for the defined capability:**

---

**Best prompt condition:**

---

**Conditions under which this recommendation holds:**

---

**Important cost, latency, or human-effort trade-off:**

---

**What should a practitioner not infer from this study?**

---

---

## O. Validity and limitations

**Construct validity: are we measuring the intended capability?**

Largely addressed by design: the intended capability is the degree of semantic agreement/divergence between an AI summary and the article's author abstract, and BERTScore F1 directly targets that semantic comparison. The remaining gap is that BERTScore alone cannot confirm the summary is factually faithful to the article itself (a summary can match the abstract closely while still containing errors), which is why faithfulness is checked separately via SummaC-Conv and human rating.

**Internal validity: could another factor explain the result?**

Confounds anticipated: article length and field, abstract quality, text-extraction quality, output length, whether the article was known from training data, generation randomness, web search behavior, full-text availability, context limits, and product changes over the data-collection window. These are partly controlled via a uniform input, fixed length requirement, stratification, a short collection window, and alternating system order; residual limitations remain and will be described.

**External validity: where might the result fail to generalize?**

Conclusions are scoped to this MENDELU-linked corpus of English-language articles and to the specific product versions recorded during testing; results are a comparison of products (including their web/search behavior), not of isolated model capability.

**Statistical uncertainty or sample-size limitation:**

Only 10 held-out test articles; uncertainty will be estimated via paired bootstrap over articles (preserving the pairing of related outputs), and results from the development/validation sets will not be merged into the final test score.

**Product or model-version drift:**

Mitigated by a short, defined data-collection window and by logging the visible model/version and date tested for every run (section D/J); full elimination of drift across the collection period cannot be guaranteed.

**Evaluation bias or judge bias:**

No LLM-as-judge is used. Human-rating bias is mitigated via blinding of system identity/prompt condition, randomized presentation order, and weighted Cohen's kappa to quantify inter-rater agreement; a risk of reference leakage exists if a system's web search surfaces the withheld abstract (see section E).

**Most important follow-up experiment:**

TBD — to be identified after reviewing the pilot and final results.