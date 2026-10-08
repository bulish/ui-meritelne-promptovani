Here is the precise summary of the scientific article, structured according to your guidelines:

## Goal

The study aims to develop a user-friendly, collaborative text annotation application that leverages Large Language Models (LLMs) to reduce manual workloads and streamline Named Entity Recognition (NER) and sentiment analysis.

## Methods

The research utilized a software engineering and experimental approach, employing the Nuxt 3 frontend framework, Django backend framework, and PostgreSQL database. The system integrated BERT, TinyBERT, and GPT-4 models, evaluating them using benchmark datasets such as CoNLL-2003 and IMDb alongside quantitative metrics like precision, recall, F1-score, and accuracy.

## Main results

Fine-tuning BERT for NER on the CoNLL-2003 dataset achieved a validation loss of $0.0832$, a precision of $88.68\%$, recall of $92.44\%$, F1-score of $90.52\%$, and accuracy of $97.88\%$. Fine-tuning TinyBERT for sentiment analysis on the IMDb dataset yielded a validation loss of $0.4401$, precision of $85.96\%$, recall of $85.94\%$, F1-score of $85.93\%$, and accuracy of $85.94\%$. Furthermore, comparative application testing demonstrated that semi-automation reduced manual annotation times, with GPT-4 performing effectively in zero-shot scenarios and TinyBERT providing precise token-level suggestions.

## Conclusions

The authors conclude that integrating LLMs into a collaborative text annotation framework significantly diminishes manual labor while preserving high accuracy and consistency. They recommend combining automated suggestions with human oversight, while advising caution regarding LLM limitations such as hallucinations, high computational demands, and token length constraints.