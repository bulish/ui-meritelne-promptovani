### Goal

This study aims to investigate the integration of fuzzy-logic principles with expert systems to develop a novel recommender system and compare its performance against traditional recommender systems, focusing on metrics such as accuracy, relevance, and user satisfaction.

### Methods

The study adopted a quantitative research design utilizing a dataset containing 7,22,676 observations and 20 variables obtained from Kaggle. Data preprocessing involved filtering rows with a vote count greater than or equal to 350, dropping duplicate titles and release dates, and calculating a standardized recommendation score using weights of 0.4 for popularity, 0.3 for vote average, and 0.3 for vote count scaled via a MinMaxScaler. The fuzzy logic expert system utilized Python libraries such as scikit-fuzzy to define antecedents, consequents, fuzzy sets, and membership functions. A content-based machine learning model was developed using text processing via the porter stemmer, CountVectorizer, and a Bag-of-Words (BOW) approach, alongside cosine similarity to evaluate recommendations. Both systems were evaluated using performance metrics including accuracy, F1 score, precision, recall, and confusion matrices.

### Main results

When evaluated, the fuzzy logic model achieved an accuracy of 0.98, an F1 score of 0.02, a precision of 0.02, and a recall of 0.03, with a confusion matrix showing 7486 true negatives, 105 false positives, 73 false negatives, and 2 true positives. In contrast, the content-based machine learning model achieved an accuracy of 0.94, an F1 score of 0.02, a precision of 0.01, and a recall of 0.06, with a confusion matrix consisting of 39536 true negatives, 1989 false positives, 457 false negatives, and 28 true positives.

### Conclusions

While fuzzy logic models excel in handling uncertainty, vagueness, and overall accuracy, evaluating a broader set of metrics like precision and recall demonstrates that the content-based machine learning model is more appropriate for movie recommendations when balancing multiple performance factors.

---

* "This study aims to investigate the amalgamation of fuzzy-logic principles with expert systems to develop a novel recommender system, offering potentially more adaptable and context-aware recommendations."


* "This study adopted the use of quantitative research design, this is because it is well-suited for investigating recommendation systems, especially when comparing traditional recommendation systems with fuzzy logic models."[cite: 33]
* "Data has been selected from [https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies) This dataset contains 7,22,676 observations with 20 variables."


* "Selected data whose vote count is greater than or equal to 350. Drop duplicates from title and released date. Calculated the recommendation score from the data itself."


* "a. weight_popularity with a weight of 0.4. b. weight_vote_average with a weight of 0.3. c. weight_vote_count with a weight of 0.3."


* "Accuracy: 0.98 F1 Score: 0.02 Precision: 0.02 Recall: 0.03 Confusion Matrix: [[7486 105] [ 73 2]]"


* "Accuracy: 0.94 F1 Score: 0.02 Precision: 0.01 Recall: 0.06 Confusion Matrix: [[39536 1989] [ 457 28]]"


* "When evaluating the recommendation systems, fuzzy logic appears to perform better in terms of accuracy. However, if we consider additional evaluation parameters, such as precision and recall, the content-based machine learning model emerges as the more suitable approach for movie recommendations."