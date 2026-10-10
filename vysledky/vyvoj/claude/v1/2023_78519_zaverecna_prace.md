Goal
The thesis compares a fuzzy-logic expert system with a traditional content-based machine learning recommender for movies, asking which performs better on accuracy, precision, and recall.

Methods
Both systems were built on a Kaggle movies dataset of 722,676 observations and 20 variables, filtered to titles with at least 350 votes. A weighted recommendation score (popularity 0.4, vote average 0.3, vote count 0.3) was computed and min-max scaled. The fuzzy system maps user preference (Love, Neutral, Hate) to recommendation levels; the content-based model uses genre features and cosine similarity. Both were evaluated with a 0.5 threshold.

Main results
The fuzzy logic model reached accuracy 0.98, F1 0.02, precision 0.02 and recall 0.03. Its confusion matrix was 7486 true negatives, 105 false positives, 73 false negatives and 2 true positives. The content-based model reached accuracy 0.94, F1 0.02, precision 0.01 and recall 0.06, with 39536 true negatives, 1989 false positives, 457 false negatives and 28 true positives. The authors note that changing the threshold changes the results.

Conclusions
Fuzzy logic scores higher on accuracy, but the Discussion judges the content-based model more suitable when precision and recall are considered. The Conclusion nevertheless argues fuzzy expert models handle uncertainty, adapt to changing preferences, and offer greater transparency.

Source passages supporting the main claims

Chapter 4 intro and 4.1 Data Preprocessing: dataset size, vote filter, score weights, scaling
4.2 Fuzzy Logic: preference categories and rules
4.3 Content Based ML Model and Figure 6: cosine similarity on genre features
4.4.1 Fuzzy Logic and Figure 7: metrics and confusion matrix
4.4.2 Content-Based ML model and Figure 8: metrics and confusion matrix
Chapter 5 Discussion: metric trade-offs and threshold sensitivity
Chapter 6 Conclusion: claimed advantages of fuzzy expert models