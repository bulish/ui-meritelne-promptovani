Goal
The thesis aims to develop a fuzzy-logic-based expert system for personalized movie recommendations and compare it with a traditional content-based machine-learning recommender, focusing on recommendation performance and handling user preferences.     2023_78519_zaverecna_prace
Methods
The study used a quantitative comparative design. A Kaggle movie dataset containing 7,22,676 observations with 20 variables was used. The fuzzy-logic system mapped user preferences to recommendation scores using fuzzy sets and rules, while the content-based model used text preprocessing, CountVectorizer with a 5000-word bag-of-words representation, and cosine similarity. Performance was evaluated using accuracy, F1 score, precision, recall, and confusion matrices.     2023_78519_zaverecna_prace
Main results
The fuzzy-logic model achieved accuracy 0.98, but its F1 Score was 0.02, precision 0.02, and recall 0.03; its confusion matrix contained 7486 true negatives, 105 false positives, 73 false negatives, and 2 true positives. The content-based model achieved accuracy 0.94, F1 Score 0.02, precision 0.01, and recall 0.06, with 39536 true negatives, 1989 false positives, 457 false negatives, and 28 true positives. The discussion therefore identifies fuzzy logic as better on accuracy, but the content-based model as more suitable when precision and recall are considered.     2023_78519_zaverecna_prace
Conclusions
The authors conclude that fuzzy-logic expert models better address uncertainty, imprecision, changing preferences, and transparency, enabling more nuanced and personalized recommendations.     2023_78519_zaverecna_prace
Source sections/passages supporting the main claims:
- Introduction, Objectives (pp. 13–14): research aim and comparison of recommender systems.     2023_78519_zaverecna_prace
- Methodology (pp. 33–45): quantitative design, data collection, and development of the two recommender approaches.     2023_78519_zaverecna_prace
- Results, “Data Preprocessing” (pp. 45–46): dataset size and variables.     2023_78519_zaverecna_prace
- Results, “Evaluation” (pp. 51–54): accuracy, F1, precision, recall, and confusion-matrix results.
- Discussion (p. 55): interpretation of the comparative results and threshold sensitivity.
- Conclusion (pp. 56–57): authors’ central interpretation concerning uncertainty, adaptability, personalization, and transparency.     2023_78519_zaverecna_prace