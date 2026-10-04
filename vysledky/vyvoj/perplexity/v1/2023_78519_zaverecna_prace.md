Goal
To compare a fuzzy-logic expert system with traditional recommender approaches for movie recommendation, focusing on accuracy, relevance, user satisfaction, interpretability, and adaptability to uncertain user preferences.

Methods
The study used a quantitative design and a Kaggle movie dataset containing 7,22,676 observations and 20 variables. It compared a fuzzy-logic recommender with a content-based ML model. Evaluation used accuracy, F1 Score, precision, recall, and confusion matrices.

Main results
The fuzzy-logic model reported accuracy of 0.98, F1 Score of 0.02, precision of 0.02, and recall of 0.03. Its confusion matrix contained 7486 true negatives, 105 false positives, 73 false negatives, and 2 true positives. The content-based ML model reported accuracy of 0.94, F1 Score of 0.02, precision of 0.01, and recall of 0.06. Its confusion matrix contained 39536 true negatives, 1989 false positives, 457 false negatives, and 28 true positives. The article states that changing the recommendation threshold can substantially alter results.

Conclusions
The thesis concludes that fuzzy-logic expert models are valuable because they handle uncertainty and imprecision in preferences, adapt to changing preferences, and provide transparency through linguistic variables and fuzzy inference. However, it judges the content-based ML model more suitable for movie recommendation when accuracy, precision, and recall are considered together.

Supporting source sections
Section 1.1–1.3, “Background and motivation,” “Research Questions,” and “Objectives of the study”: study purpose and comparison criteria.

Section 3, “Methodology”: quantitative research design.

Section 4, “Results”: dataset size and variables.

Section 4.4.1, “Fuzzy Logic”: fuzzy-model evaluation metrics and confusion matrix.

Section 4.4.2, “Content-Based ML model”: content-based-model evaluation metrics and confusion matrix.

Section 5, “Discussion”: threshold sensitivity and comparative interpretation.

Section 6, “Conclusion”: claimed advantages of fuzzy logic and final practical conclusion.

