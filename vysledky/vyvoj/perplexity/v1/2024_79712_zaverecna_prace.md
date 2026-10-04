Goal
Develop and assess a collaborative, LLM-assisted text-annotation application for Named Entity Recognition (NER) and sentiment analysis, aiming to reduce manual workload while preserving annotation quality.

Methods
The application was implemented using Nuxt 3, Django/Django REST Framework, and PostgreSQL. BERT was fine-tuned for NER using CoNLL-2003, while TinyBERT was fine-tuned for sentiment analysis using the IMDb dataset. Evaluation combined precision, recall, F1, and accuracy measures with application testing by three annotators.

Main results
The fine-tuned BERT NER model achieved training loss 0.106, validation loss 0.0832, precision 0.8868, recall 0.9244, F1 0.9052, and accuracy 0.9788. TinyBERT sentiment-analysis fine-tuning produced training loss 0.3749, validation loss 0.4401, precision 0.8596, recall 0.8594, F1 0.8593, and accuracy 0.8594. For one NER document, TinyBERT achieved 100 for accuracy, precision, recall, and F1-score; GPT-4 achieved 88.89 accuracy and 50 for precision, recall, and F1-score. The sentiment-analysis test dataset comprised 300 samples, with 50 labelled positive and 50 negative. Automation reduced average annotation time; GPT-4 performed well in zero-shot scenarios, and TinyBERT provided precise token-level suggestions for structured datasets.

Conclusions
The system indicates that semi-automated LLM suggestions plus human refinement can improve annotation efficiency and support collaborative workflows. However, practical use remains constrained by GPT-4 hallucinations, substantial computational requirements, contextual and long-text limitations, and fine-tuning restricted to Hugging Face datasets.

Supporting passages
§3.6–3.7, pp. 37–40: System implementation and evaluation design.

§4.4.9, pp. 59–66; Table 2: CoNLL-2003 BERT NER fine-tuning and metrics.

§4.4.10, pp. 66–70; Table 3: IMDb TinyBERT sentiment-analysis fine-tuning and metrics.

§4.5–4.5.2, pp. 78–83; Table 5: Application testing, time reduction, and GPT-4/TinyBERT NER comparison.

§5–5.1, pp. 84–86: Overall interpretation and limitations of LLM-supported annotation.

