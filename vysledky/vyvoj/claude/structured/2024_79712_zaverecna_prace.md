Goal: The thesis develops a user-friendly text annotation application that uses large language models to support collaboration among annotators, ensure high-quality annotations, and reduce manual workload through semi-automation for Named Entity Recognition (NER) and sentiment analysis.

Methods: The author reviewed seven annotation tools (Prodigy scored 15, Label Studio 13, Doccano 12), then built a system with a Nuxt 3/Vue.js frontend, a Django REST Framework backend, and PostgreSQL. BERT was fine-tuned on CoNLL-2003 for NER, and TinyBERT on IMDb for sentiment. GPT-4 was prompted with JSON-parsed templates (temperature 0). Testing involved the author and two student annotators.

Main results: Fine-tuned BERT reached precision 0.8868, recall 0.9244, F1 0.9052, and accuracy 0.9788. TinyBERT reached accuracy 0.8594 and F1 0.8593. On one NER document, TinyBERT scored 100% on all metrics, while GPT-4 scored 88.89% accuracy and 50% precision, recall, and F1. Annotators found the interface easy to navigate, and automation reduced annotation time.

Conclusions: Role-based collaboration, comments, automation, and export reduce manual labour. Limitations include GPT-4 hallucinations, computational demands, weak contextual understanding, token limits, and fine-tuning restricted to Hugging Face datasets.

Supporting passages

1.4 Objectives of the study (goal)
2.6 Review of text annotation applications, Table 1 (tool scores)
3.4 Choice of technologies; 3.5 Model selection (stack and models)
3.7 Evaluation (evaluation design, annotators)
4.4.9 and Table 2 (BERT/CoNLL-2003 metrics)
4.4.10 and Table 3 (TinyBERT/IMDb metrics)
4.4.11.4–4.4.11.5 (GPT-4 prompting for NER and sentiment)
4.5 Testing; Table 5 (NER comparison, usability and time savings)
5 Discussion; 5.1 Limitations; 6 Conclusion