This diploma thesis (Mendel University, 2024) compares a fuzzy-logic expert system with a traditional content-based machine learning recommender for movies. The literature review covers collaborative filtering (memory- and model-based), content-based filtering, hybrid approaches, fuzzy logic (membership functions, IF-THEN rules, defuzzification) and evaluation metrics. The author argues that fuzzy logic better handles the vagueness of user preferences.

Both systems use a Kaggle movie dataset of about 722,000 records. The data was filtered to movies with at least 350 votes, and a weighted recommendation score was built from popularity (0.4), average vote (0.3) and vote count (0.3). Genres were one-hot encoded. The fuzzy system maps a user’s preference (“Love”, “Neutral”, “Hate”) to a recommendation level. The content-based model uses stemming, a 5,000-word bag-of-words and cosine similarity.

Both were evaluated against a 0.5 threshold. Fuzzy logic scored accuracy 0.98, precision 0.02, recall 0.03 and F1 0.02. The content-based model scored accuracy 0.94, precision 0.01, recall 0.06 and F1 0.02. The author concludes that fuzzy logic wins on accuracy, while the content-based model is preferable on recall, and that results depend strongly on the threshold. The thesis claims fuzzy models offer greater interpretability, though this is not tested empirically. The discussion’s claim that the content-based model has higher precision conflicts with the reported figures, and the user-satisfaction research questions are not evaluated.

Source sections supporting the main claims

Overview of recommender approaches: Sections 2.2 (Collaborative Filtering), 2.3 (Content-Based Filtering), 2.4 (Hybrid Approaches)
Fuzzy logic principles: Sections 2.5.1–2.5.4
Evaluation metrics: Section 2.6
Research design and fuzzy system design: Sections 3 and 3.2.2–3.2.7
Dataset, weights and genre encoding: Sections 4 and 4.1
Fuzzy and content-based implementations: Sections 4.2 and 4.3
Reported metrics and confusion matrices: Sections 4.4.1 and 4.4.2 (Figures 7–8)
Threshold sensitivity and comparison: Section 5 (Discussion)
Interpretability and uncertainty-handling claims: Section 6 (Conclusion)
Research questions on user satisfaction, which were not evaluated: Sections 1.2 and 2.6.6

A note on the instructions: the document has no abstract, and no separate linked full text was supplied, so this summary rests solely on the thesis body you attache