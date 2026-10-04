Summary
This thesis compares a fuzzy-logic expert system with a content-based machine-learning recommender for personalized movie suggestions. It first reviews collaborative, content-based, and hybrid recommendation methods, emphasizing the difficulty of representing uncertain and subjective user preferences. The proposed fuzzy system models preferences through linguistic categories and membership functions, applies “IF–THEN” rules, and converts the resulting fuzzy output into recommendation scores. Using a large movie dataset, the study preprocesses records by filtering vote counts, removing duplicates, weighting popularity and rating variables, scaling scores, and encoding genres as binary features. The content-based model uses stemming, CountVectorizer, a bag-of-words representation, and cosine similarity to identify similar films.

The fuzzy system achieved higher reported accuracy (0.98 versus 0.94), but both systems had very low F1 scores. The fuzzy model reported precision of 0.02 and recall of 0.03, while the content-based model reported precision of 0.01 and recall of 0.06. The thesis therefore concludes that accuracy alone is misleading, especially under class imbalance and threshold sensitivity. Although fuzzy logic offers interpretability and better handling of vague preferences, the content-based model is judged more suitable when precision and recall are prioritized.

Supporting sections
Introduction, Sections 1.1–1.3: motivation, research questions, and objectives.

Literature Review, Sections 2.3–2.5: content-based filtering and fuzzy-logic principles.

Methodology, Sections 3.2–3.3: development of the fuzzy and traditional recommender systems.

Results, Sections 4.1–4.4: dataset, preprocessing, model construction, and evaluation.

Discussion, Section 5: interpretation of accuracy, precision, recall, and threshold sensitivity.

Conclusion, Section 6: stated advantages of fuzzy logic, including interpretability and handling uncertainty.