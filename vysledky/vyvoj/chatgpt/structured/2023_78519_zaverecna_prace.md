
1. Summary (190 words)
Goal: The thesis compares fuzzy logic with traditional machine-learning approaches for movie recommender systems, particularly assessing recommendation performance and the suitability of fuzzy logic for handling user preferences. The study uses a dataset containing 7,22,676 observations with 20 variables. 

Methods: Data preprocessing selected movies with a vote count greater than or equal to 350, removed duplicates based on title and released date, calculated a recommendation score from popularity, vote_average, and vote_count, and scaled it to [0, 1] using MinMaxScaler. The fuzzy system used the scikit-fuzzy library, fuzzy sets, membership functions, and three rules mapping “Love,” “Neutral,” and “Hate” preferences to recommendation levels. The content-based ML model used porter stemmer from nltk library, Countvectorizer, BOW (bag of words), and cosine similarity. 
 

Main results: Fuzzy logic achieved Accuracy (0.98), F1 Score (0.02), Precision (0.02), Recall (0.03), while the content-based model achieved Accuracy (0.94), F1 Score (0.02), Precision (0.01), Recall (0.06). 
 

Conclusions: The discussion favors the content-based model when precision and recall are considered, whereas the conclusion emphasizes fuzzy logic’s handling of uncertainty, adaptability, and transparency. 

2. Supporting source sections/passages
Section 4, Results / 4.1 Data Preprocessing: dataset size, selection criteria, recommendation-score calculation, and scaling. 
Section 4.3, Content Based ML Model: stemming, Countvectorizer, BOW, and cosine similarity. 
Section 4.4.1, Fuzzy Logic: Accuracy, F1 Score, Precision, Recall, and confusion matrix results. 
Section 4.4.2, Content-Based ML model: Accuracy, F1 Score, Precision, Recall, and confusion matrix results. 
Section 5, Discussion: comparison of the models and effect of threshold changes. 
Section 6, Conclusion: stated advantages of fuzzy logic expert models regarding uncertainty, adaptability, and transparency. 
