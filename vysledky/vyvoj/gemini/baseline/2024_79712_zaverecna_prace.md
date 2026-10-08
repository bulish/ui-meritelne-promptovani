## Summary

This thesis introduces a full-stack web application designed to revolutionize text annotation workflows by integrating Large Language Models (LLMs) like GPT-4, BERT, and TinyBERT. Traditional text annotation processes are typically manual, time-consuming, and prone to bottlenecks. To overcome these challenges, the author developed a collaborative platform using a Nuxt 3 (Vue.js) frontend and a Django REST Framework backend coupled with a PostgreSQL database.

The system supports core Natural Language Processing (NLP) tasks, specifically Named Entity Recognition (NER) and sentiment analysis. It provides features for user role management, secure authentication, file importing, project customization, and interactive threaded comments. Furthermore, the platform implements a dual approach to annotation: fully manual labelling via an intuitive interface and semi-automated suggestions powered by fine-tuned transformer models and prompt engineering. Testing and evaluation against standard benchmarks demonstrate that leveraging LLMs and automated models drastically reduces manual workloads while maintaining high accuracy, although limitations such as model hallucinations and high computational resource requirements remain.

---

## Supporting Source Sections

* **Introduction & Objectives:** Sections 1.1, 1.2, and 1.4.


* **Literature Review & Tool Comparison:** Sections 2.1, 2.2, and 2.6.


* **Methodology & Technology Stack:** Sections 3.2, 3.3, 3.4, and 3.5.


* **System Implementation:** Sections 4.1, 4.4, and 4.4.11.


* **Testing, Results, and Limitations:** Sections 4.5, 5, and 5.1.