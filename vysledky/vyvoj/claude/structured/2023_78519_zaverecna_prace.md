Goal. This 2024 Mendel University diploma thesis compares a fuzzy-logic expert system with traditional recommender systems (collaborative, content-based, hybrid) for movie recommendation. It asks whether fuzzy logic improves interpretability, adaptability and performance.

Methods. The study uses a quantitative design on a Kaggle movie dataset (722,676 observations, 20 variables), filtered to vote count ≥ 350 with duplicates dropped. A recommendation score combined popularity (0.4), vote_average (0.3) and vote_count (0.3), MinMax-scaled to [0, 1], and genres became binary columns. The fuzzy system (scikit-fuzzy) mapped “User_Preference” to “Recommendation” through three rules (Love, Neutral, Hate). The content-based model used Porter stemming, CountVectorizer (5000 words) and cosine similarity.

Main results. At a 0.5 threshold, fuzzy logic scored accuracy 0.98, F1 0.02, precision 0.02 and recall 0.03. The content-based model scored accuracy 0.94, F1 0.02, precision 0.01 and recall 0.06.

Conclusions. Results are sensitive to the threshold. Fuzzy logic leads on accuracy, but the Discussion judges the content-based model more suitable when precision and recall are considered. The Conclusion nonetheless credits fuzzy expert models with better handling of uncertainty, adaptability and transparency.

Supporting passages

Section 1.2–1.3 (Research Questions, Objectives): the comparison goal and the four research questions
Chapter 3 intro and Section 3.2 (Methodology, fuzzy expert system): quantitative design, variables, rules, inference
Chapter 4 intro and Section 4.1 (Data Preprocessing): dataset size, vote-count filter, weights 0.4/0.3/0.3, MinMax scaling, binary genre columns
Section 4.2 (Fuzzy Logic): scikit-fuzzy components and the three rules
Section 4.3 (Content Based ML Model): stemming, CountVectorizer with 5000 words, cosine similarity
Section 4.4.1 and Figure 7: fuzzy metrics and confusion matrix [[7486, 105], [73, 2]]
Section 4.4.2 and Figure 8: content-based metrics and confusion matrix [[39536, 1989], [457, 28]]
Chapter 5 (Discussion): threshold sensitivity and the accuracy vs. precision/recall trade-off
Chapter 6 (Conclusion): claims about uncertainty handling, adaptability and transparency

Note on a discrepancy in the source: the Discussion says the content-based model has higher precision, but Section 4.4 reports 0.01 for it versus 0.02 for fuzzy logic. Only its recall (0.06 vs. 0.03) is higher. I reported the numbers exactly as given.