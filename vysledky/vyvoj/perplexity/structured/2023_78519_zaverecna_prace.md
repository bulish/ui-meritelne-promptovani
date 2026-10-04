Summary
Goal: This thesis compares a fuzzy-logic expert system with a traditional content-based machine-learning (ML) model for movie recommendation, examining accuracy, relevance, interpretability, and adaptability to user preferences. Methods: Using a dataset of 7,22,676 observations and 20 variables, the study retained movies with vote counts ≥350, removed title/release-date duplicates, and created a MinMax-scaled recommendation score weighted by popularity (0.4), vote_average (0.3), and vote_count (0.3). Genre data were binary encoded. The fuzzy system used scikit-fuzzy antecedent/consequent variables, membership functions, and three rules mapping “Love,” “Neutral,” and “Hate” preferences to recommendation levels. The content-based model applied Porter stemming, CountVectorizer, a bag-of-words representation of 5000 frequent words, and cosine similarity. Main results: Fuzzy logic achieved accuracy 0.98, F1 0.02, precision 0.02, and recall 0.03; the content-based model achieved accuracy 0.94, F1 0.02, precision 0.01, and recall 0.06. Conclusions: The thesis states that threshold changes substantially affect outcomes. It concludes that fuzzy logic better handles uncertainty, supports transparent linguistic reasoning, and provides personalization, whereas the content-based model is considered more suitable when precision and recall are jointly considered.

Supporting sections
Section 1.1–1.3, Introduction: States the motivation to integrate fuzzy logic into expert systems and the comparative objectives.

Section 3.2.2–3.2.7, Development of the fuzzy logic expert system: Describes inputs, membership functions, fuzzy rules, inference, and defuzzification.

Section 4.1, Data Preprocessing: Reports dataset size, vote-count filter, feature weights, scaling, and genre encoding.

Section 4.2, Fuzzy Logic: Specifies scikit-fuzzy components, preference categories, rules, and recommendation procedure.

Section 4.3, Content Based ML Model: Specifies Porter stemming, CountVectorizer, bag-of-words, and cosine similarity.

Sections 4.4.1–4.4.2, Evaluation: Provides the reported accuracy, F1, precision, recall, and confusion-matrix results.

Sections 5–6, Discussion and Conclusion: Interprets threshold sensitivity and states the comparative conclusions.