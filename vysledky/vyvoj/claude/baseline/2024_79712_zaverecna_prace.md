Summary (about 175 words)

This diploma thesis (Mendel University in Brno, 2024) develops a web-based text annotation application. It uses large language models to semi-automate Named Entity Recognition (NER) and sentiment analysis. The goal is to cut the manual effort and inconsistency of traditional annotation while supporting collaboration. After reviewing existing tools (Brat, Doccano, Prodigy), the author built a system with a Nuxt 3/Vue.js frontend, a Django REST backend and a PostgreSQL database. It offers role-based access for annotators, reviewers and administrators, project and label management, dataset import, and comments. BERT-family models can be fine-tuned through the interface, using CoNLL-2003 for NER and IMDb reviews for sentiment, while GPT-4 supplies zero-shot suggestions. The author and two student annotators tested the tool. They found the interface consistent and easy to use and reported, qualitatively, shorter annotation times with model assistance. In the sample comparisons, GPT-4 and BERT agreed with gold labels on the displayed tweets. On one NER document, TinyBERT scored perfectly, while GPT-4 reached 50% precision and recall. Stated limitations include GPT-4 hallucinations, computational cost, weaker handling of specialised or long texts, and fine-tuning restricted to Hugging Face datasets.

Source sections supporting the main claims

Aim and problem (manual annotation is slow and inconsistent): §1.2 Problem statement; §1.4 Objectives of the study
Review of existing tools: §3.1 Requirements gathering
Technology stack and roles/permissions: §3.4 Choice of technologies (3.4.1–3.4.3); §3.6.1–3.6.4 Implementation
Model choice and GPT-4 zero-shot role: §3.5 Model selection; §3.6.3 LLM integration
Fine-tuning datasets (CoNLL-2003, IMDb): §4.4.9; §4.4.10
Evaluation design (author plus two annotators): §3.7 Evaluation
Usability, collaboration and time-saving findings: §4.5 Testing; §5 Discussion
Sentiment sample comparison (300 tweets): §4.5.1
NER comparison (TinyBERT vs. GPT-4, one document): §4.5.2, Table 5
Limitations: §5.1 Limitations of the application

Notes on the source

I used only the thesis body, per your instructions, and skipped the abstract and the Conclusion (§6).
The thesis gives no aggregate sentiment metrics or measured time savings in its text. The results are one NER document and a table of sample tweets, so the summary reflects only that.
The thesis is inconsistent about which model was fine-tuned for NER. §3.6.3 and §4.5.2 say TinyBERT, while §4.4.9 says BERT. I therefore described them as “BERT-family models.”