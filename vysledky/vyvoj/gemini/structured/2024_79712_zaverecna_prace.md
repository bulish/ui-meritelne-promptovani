**Goal**


This study aims to develop a user-friendly text annotation application that leverages Large Language Models (LLMs) to facilitate collaboration among annotators, ensure high-quality annotations, and reduce manual workload through semi-automation, specifically focusing on Named Entity Recognition (NER) and sentiment analysis.

**Methods**


The application was built using Nuxt 3 for the frontend framework and Django with the Django REST Framework (DRF) for the backend. PostgreSQL was selected as the database to handle structured and semi-structured data using JSONB fields. For model integration and semi-automation, BERT and TinyBERT were fine-tuned using Hugging Face libraries on datasets such as CoNLL-2003 and IMDb, while GPT-4 was integrated via the OpenAI API using dynamic prompt engineering and Pydantic parsers. The evaluation involved testing user interfaces, multi-user role-based collaboration, and performance metrics like precision, recall, and F1-score against gold standards.

**Main results**


The fine-tuned BERT model achieved a validation loss of 0.0832, precision of 0.8868, recall of 0.9244, F1-score of 0.9052, and accuracy of 0.9788. TinyBERT achieved an evaluation loss of 0.4401, precision of 0.8596, recall of 0.8594, F1-score of 0.8593, and accuracy of 0.8594. Testing demonstrated that semi-automation successfully reduced manual workload, with GPT-4 excelling in zero-shot tasks and TinyBERT providing precise token-level suggestions. Furthermore, role-based access control and real-time commenting successfully supported multi-user collaboration.

**Conclusions**


The developed system successfully integrates modern LLMs like GPT-4, BERT, and TinyBERT into a flexible, customizable text annotation platform that streamlines workflows, minimizes manual labor, and maintains high accuracy. However, challenges such as model hallucinations in GPT-4, high computational demands, context limitations on long texts, and restriction to Hugging Face datasets for fine-tuning remain notable constraints.

---

* **Goal:** "The primary aim of this thesis is to develop a user-friendly text annotation application that leverages LLMs to facilitate collaboration among annotators, ensure high-quality annotations, and reduce manual workload through semi-automation, specifically in tasks like Named Entity Recognition (NER) and sentiment analysis."


* **Methods:** "Nuxt 3, a powerful framework based on Vue.js, was selected for the frontend..." and "Django was chosen as the backend framework..."


* **Methods:** "PostgreSQL, an open-source relational database... was selected to store the application's structured data..."


* **Main results:** "Table 2: Model Training and Evaluation Metrics Across Epochs for BERT... Validation Loss: 0.0832 | Precision: 0.8868 | Recall: 0.9244 | F1: 0.9052 | Accuracy: 0.9788"


* **Main results:** "Table 3: Model Training and Evaluation Metrics Across Epochs for TinyBERT... Validation Loss: 0.4401 | Precision: 0.8596 | Recall: 0.8594 | F1: 0.8593 | Accuracy: 0.8594"


* **Conclusions:** "A unique challenge posed by GPT-4 is the tendency to generate hallucinations—plausible-sounding but incorrect or fabricated information."


* **Conclusions:** "The text annotation system's fine-tuning functionality is restricted to datasets available on Hugging Face."