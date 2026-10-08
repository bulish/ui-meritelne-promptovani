## Summary

**Goal**
This study aims to compare a fuzzy-logic-based expert system with traditional machine learning methods—specifically a content-based recommender model—for personalized movie recommendations.

**Methods**
The quantitative study utilized a dataset of 722,676 observations with 20 variables sourced from Kaggle, filtering for items with a vote count $\ge 350$. Text preprocessing involved the Porter stemmer from the nltk library, CountVectorizer, and a bag-of-words (BOW) model using the 5000 most repeated words. Performance was evaluated using accuracy, F1 score, precision, recall, and a confusion matrix.

**Main Results**
For the fuzzy logic model, evaluation metrics yielded an accuracy of 0.98, an F1 score of 0.02, a precision of 0.02, and a recall of 0.03, with a confusion matrix showing 7,486 true negatives, 105 false positives, 73 false negatives, and 2 true positives. The content-based machine learning model achieved an accuracy of 0.94, an F1 score of 0.02, a precision of 0.01, and a recall of 0.06, featuring a confusion matrix of 39,536 true negatives, 1,989 false positives, 457 false negatives, and 28 true positives.

**Conclusions**
While the fuzzy logic model outperforms in pure accuracy due to its handling of uncertainty, the authors conclude that the content-based machine learning model is more suitable overall when balancing precision and recall. Ultimately, system selection depends on specific application goals.