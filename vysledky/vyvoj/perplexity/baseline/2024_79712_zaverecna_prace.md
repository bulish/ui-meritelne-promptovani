Summary
This thesis develops a collaborative text-annotation application that uses large language models (LLMs) to reduce the manual effort involved in named entity recognition (NER) and sentiment analysis. It addresses limitations of traditional annotation, which the author characterizes as slow, inconsistent, and difficult to scale. The system combines manual annotation with model-generated suggestions that users can review and correct, thereby retaining human oversight. Its implementation uses Nuxt 3 for the frontend, Django and Django REST Framework for backend services, PostgreSQL for data storage, and GPT-4, BERT, and TinyBERT for annotation and fine-tuning. The application supports user roles, project management, dataset import, comments, model fine-tuning, and export in several formats. BERT fine-tuning for NER on CoNLL-2003 produced 88.68% precision, 92.44% recall, 90.52% F1, and 97.88% accuracy, while TinyBERT fine-tuning for sentiment analysis achieved approximately 85.9% across the reported metrics. Testing suggested that semi-automation reduced annotation workload and that GPT-4 was effective for zero-shot sentiment analysis, whereas TinyBERT performed well on structured NER. However, the thesis identifies hallucinations, computational demands, limited contextual understanding, long-text difficulties, and dependence on Hugging Face datasets as important constraints.

Supporting source sections
Introduction, §§1.1–1.4 (pp. 11–14): Motivation, problem statement, and research objectives.

Methodology, §§3.4–3.7 (pp. 34–40): Technology stack, model selection, implementation, and evaluation design.

Results, §§4.4.9–4.4.10 (pp. 59–70): Fine-tuning procedures and reported BERT/TinyBERT metrics.

Results, §§4.4.11 and 4.5 (pp. 70–83): Manual and semi-automated annotation, testing, and model comparisons.

Discussion, §§5–5.1 (pp. 84–86): Usability findings and application limitations.