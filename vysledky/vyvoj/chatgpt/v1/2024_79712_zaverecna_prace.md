Goal
The thesis aimed to develop a user-friendly text annotation application leveraging large language models (LLMs) to support collaboration, improve annotation quality, and reduce manual workload in Named Entity Recognition (NER) and sentiment analysis.     2024_79712_zaverecna_prace
Methods
The 2024 study developed and evaluated a text-annotation system integrating GPT-4, BERT, and TinyBERT for manual and semi-automated annotation. Testing compared GPT-4 with fine-tuned BERT on a 300-sample sentiment dataset (50% positive, 50% negative) and GPT-4 with TinyBERT for NER, using gold-standard labels and precision, recall, F1-score, and accuracy.     2024_79712_zaverecna_prace     2024_79712_zaverecna_prace
Main results
For NER, one reported document gave TinyBERT 100% accuracy, precision, recall, and F1-score, compared with GPT-4’s 88.89% accuracy and 50% precision, recall, and F1-score. During model fine-tuning, BERT achieved 0.9788 accuracy, while TinyBERT achieved 0.8594 accuracy. The application’s semi-automation reduced annotation time; GPT-4 produced high-quality zero-shot sentiment predictions, whereas TinyBERT performed particularly well on structured NER tasks. Three annotators also successfully tested collaborative functionality.     2024_79712_zaverecna_prace     2024_79712_zaverecna_prace     2024_79712_zaverecna_prace
Conclusions
The authors conclude that integrating GPT-4, BERT, and TinyBERT can reduce manual annotation effort while supporting high-quality annotation. The resulting system is considered adaptable for different datasets and annotation scenarios, although GPT-4 hallucinations, computational requirements, contextual limitations, and restricted fine-tuning datasets remain important constraints.     2024_79712_zaverecna_prace     2024_79712_zaverecna_prace
Source passages supporting the main claims:
- Study objective: Introduction, “Objectives of the study.”     2024_79712_zaverecna_prace
- Overall methodological framework: Methodology, including requirements gathering, system design, model selection, implementation, and evaluation.     2024_79712_zaverecna_prace
- Sentiment-analysis sample and comparison: Results, §4.5.1.     2024_79712_zaverecna_prace
- Model fine-tuning results: BERT and TinyBERT evaluation tables.     2024_79712_zaverecna_prace     2024_79712_zaverecna_prace
- NER quantitative comparison: Results, §4.5.2 and Table 5.     2024_79712_zaverecna_prace
- Application-level findings and collaboration: Discussion, including reduced annotation time and testing with three annotators.     2024_79712_zaverecna_prace
- Limitations: Discussion, §5.1.     2024_79712_zaverecna_prace
- Central conclusion: Conclusion, §6.     2024_79712_zaverecna_prace