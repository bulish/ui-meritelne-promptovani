Goal: This thesis develops and evaluates a user-friendly, collaborative text-annotation application that uses large language models (LLMs) to support Named Entity Recognition (NER) and sentiment analysis while reducing manual annotation work. The system combines manual review with semi-automated suggestions from GPT-4, BERT, and TinyBERT.

Methods: The application was implemented with Nuxt 3, Django/Django REST Framework, and PostgreSQL. It includes role-based access, project and label management, dataset import/export, comments, manual annotation, and model fine-tuning. BERT was fine-tuned for NER on CoNLL-2003; TinyBERT was fine-tuned for sentiment analysis on the IMDb dataset. Evaluation used precision, recall, F1, and accuracy, alongside usability and collaboration testing with three annotators.

Main results: Fine-tuned BERT achieved precision 0.8868, recall 0.9244, F1 0.9052, and accuracy 0.9788 for NER. TinyBERT achieved precision 0.8596, recall 0.8594, F1 0.8593, and accuracy 0.8594 for sentiment analysis. In a reported NER document, TinyBERT scored 100 for accuracy, precision, recall, and F1-score, versus GPT-4’s 88.89 accuracy and 50 for the other metrics.

Conclusions: Semi-automation reduced annotation time and supported collaboration, but GPT-4 hallucinations, computational requirements, difficulties with specialised and long texts, and Hugging Face-only fine-tuning limited applicability.

Source passages supporting claims
§1.2–1.4, pp. 12–14: Problem statement and objective to build a collaborative LLM-supported annotation application for NER and sentiment analysis.

§3.4–3.7, pp. 34–40: Architecture, model selection, implementation plan, and evaluation criteria.

§4.4.9, pp. 59–66, especially Table 2: CoNLL-2003 BERT fine-tuning and NER metrics.

§4.4.10, pp. 66–70, especially Table 3: IMDb TinyBERT fine-tuning and sentiment-analysis metrics.

§4.5, pp. 78–83, especially Table 5: Testing outcomes and TinyBERT/GPT-4 NER comparison.

§5–5.1, pp. 84–86: Discussion of semi-automation, usability, collaboration, hallucinations, resource constraints, long-text issues, and Hugging Face dataset limitation.