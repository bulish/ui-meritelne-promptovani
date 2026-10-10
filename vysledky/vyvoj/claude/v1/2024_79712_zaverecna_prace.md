Summary (about 177 words)

Goal
Develop a user-friendly, collaborative text annotation application that uses large language models (LLMs) to semi-automate named entity recognition (NER) and sentiment analysis.

Methods
The author built a web application (Nuxt/Vue frontend, Django backend, PostgreSQL), fine-tuned BERT on CoNLL-2003 for NER and TinyBERT on IMDb reviews for sentiment, and used GPT-4 zero-shot. Evaluation involved the author and two student annotators, with outputs compared to gold-standard datasets.

Main results

BERT (NER, CoNLL-2003): precision 0.8868, recall 0.9244, F1 0.9052, accuracy 0.9788.
TinyBERT (sentiment, IMDb, 3 epochs): accuracy 0.8594, precision 0.8596, recall 0.8594, F1 0.8593.
One NER test document: TinyBERT scored 100% on all metrics; GPT-4 reached 88.89% accuracy and 50% precision, recall and F1.
A 300-sample tweet comparison of GPT-4 and BERT is shown only as sample predictions, without aggregate scores.
Automation reduced average annotation time (no figure given); GPT-4 hallucinated a nonexistent entity.

Conclusions
The authors conclude the system, combining GPT-4, BERT and TinyBERT, significantly reduces manual labour while ensuring high accuracy and reliability. Limitations noted: GPT-4 hallucinations, computational demands, long-text handling, and fine-tuning restricted to Hugging Face datasets.

Supporting passages
§1.4 Objectives of the study: the aim of building an LLM-based, collaborative, semi-automated annotation tool for NER and sentiment analysis.
§3.6 Implementation (3.6.1–3.6.4): the Nuxt/Vue, Django REST, PostgreSQL stack and the TinyBERT and GPT-4 integration.
§3.7 Evaluation: the author plus two student annotators, and comparison against gold-standard datasets.
§4.4.9 and Table 2: BERT fine-tuned on CoNLL-2003, with precision 0.8868, recall 0.9244, F1 0.9052, accuracy 0.9788.
§4.4.10 and Table 3: TinyBERT on the 50,000-review IMDb dataset, 3 epochs, with accuracy 0.8594 and F1 0.8593.
§4.5 and §4.5.1 (Table 4): the 300-sample sentiment set (50% positive) and the qualitative report that automation reduced annotation time.
§4.5.2 (Table 5): TinyBERT vs GPT-4 on one NER document.
§5 and §5.1: collaboration testing, GPT-4 hallucination example, and the listed limitations.
§6 Conclusion: the central claim about reduced manual labour with high accuracy and reliability.

Two caveats about the source text:

The thesis labels models inconsistently: §3.6.3 says TinyBERT was fine-tuned for NER, but Table 2 and the code describe bert-base-cased. I used the table labels.
No aggregate sentiment scores for the GPT-4 vs BERT comparison appear in the text.