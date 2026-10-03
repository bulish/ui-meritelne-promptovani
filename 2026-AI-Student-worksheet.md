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
| v0 | TBD | Baseline prompt established (see section F) | Initial design, not yet data-driven | — | — | — |
| v1 |  |  |  |  |  |  |
| v2 |  |  |  |  |  |  |
| v3 |  |  |  |  |  |  |

*(To be completed as development/validation iterations happen; the optimized prompt in section F is expected to emerge from this log.)*

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

TBD — to be completed after the pilot is run.

**Which cases were rewritten or removed?**

TBD.

**Which metric or rubric changes were made?**

TBD.

**What evidence supports freezing the benchmark?**

TBD.

**What remains uncertain?**

TBD.

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
| Claude Code | Baseline |  |  |  |  |  |  |  |
| Claude Code | Structured |  |  |  |  |  |  |  |
| Claude Code | Optimized |  |  |  |  |  |  |  |
| Grok | Baseline |  |  |  |  |  |  |  |
| Grok | Structured |  |  |  |  |  |  |  |
| Grok | Optimized |  |  |  |  |  |  |  |
| Perplexity | Baseline |  |  |  |  |  |  |  |
| Perplexity | Structured |  |  |  |  |  |  |  |
| Perplexity | Optimized |  |  |  |  |  |  |  |

*(Note: Claude Code and Grok are not part of this project's scope — see section D — and will remain blank unless the design changes.)*

---

### M. Error analysis

*(Not filled in — to be completed after data collection, for the final report.)*

| Error ID | System | Condition | Task ID | Category | Severity | First attempt? | Description | Likely cause | Preventable by prompt? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |

**Most frequent error:**

---

**Most consequential error:**

---

**Did optimization change the error distribution?**

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