import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv(
    r"C:\Users\sagar\Desktop\shreyas AIML\ai projects\spam_detection_Dataset.csv"
)

# Convert labels
df["Category"] = df["Category"].map({
    "spam": 1,
    "ham": 0
})

# Convert email text into TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(df["Message"])
y = df["Category"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Parameters to test
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5]
}

# Random Forest
model = RandomForestClassifier(random_state=42)

# Grid Search
grid_cv_model = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

# Train
grid_cv_model.fit(X_train, y_train)

# Predict
y_pred = grid_cv_model.predict(X_test)

# Results
print("Best Parameters:", grid_cv_model.best_params_)
print("Best CV Score:", grid_cv_model.best_score_)

print("Test Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Unseen emails
unseen_df = pd.DataFrame({
    "Message": [
        "Congratulations! You have won a free iPhone. Click here to claim.",
        "Hi, are we still meeting at 5 PM today?",
        "URGENT! You have won $5000. Send your bank details to receive the prize.",
        "Please send me the project report when you get time."
    ]
})

# Convert unseen emails using the existing TF-IDF vectorizer
unseen_X = vectorizer.transform(unseen_df["Message"])

# Predict
unseen_pred = grid_cv_model.predict(unseen_X)

# Add prediction to DataFrame
unseen_df["Prediction"] = unseen_pred

# Convert 1/0 to spam/ham
unseen_df["Prediction"] = unseen_df["Prediction"].map({
    1: "spam",
    0: "ham"
})

print(unseen_df)

"""
================================ Text Vectorization ===================================
The conversion of text data into a numerical representation to make them understandable for ML.

Sparse Matrix :- Mostly values are represented as 0.
Dense Matrix :- Mostly values are non-zeros

One-Hot Encoder  => Sparse matrix

from sklearn.feature_extraction.text import CountVetorizer ==> BoW
from sklearn.feature_extraction.text import TfIdfVectorizer ==> Tf-IDF



=> Bag Of Words(BoW) :- 
=> Tf-IDF :- Count the frequency of terms.


-> spam / ham
-> yes / no
-> resume screening system
    - Python
    - SQL
    - JAVA


document1 => "Hello My name is Ram"
document2 => "We will Talk to you tomorrow"

=> Unique Words (Vocabulary) => [Hello My name is Ram We will Talk to you tomorrow] =>length(11)
!NOTE :- BoW create a random vocabulary of words
                                *COUNT 
            Hello My name is Ram We will Talk to you tomorrow
document1    1     1  1    1  1   0  0    0   0   0    0
document2    0     0  0    0  0   1  1    1   1   1    1
                                        (1,7)

=> [1     1  1    1  1   0  0    0   0   0    0
    0     0  0    0  0   1  1    1   1   1    1]

Dog Bites Man
Man Bites Dog


Riserve Bank Of India
Bank of River


System that unserstands word with their meaning in Sentence

^ Dense matrix 
These are used in Natural Language Processing. ===> Deep learning
* Word2Vec
* BERT encoder
"""