"""
============================ SVM (Support Vector Machine) ===================================
It is a supervised machine learning algorithm , that uses support vectors with the help of
hyperplane to seperate data , and find the best decision boundry. 

----------------------------------------------------------------------------------------------------------------------
| Supervised Learning Algorithm          | Typical Problems/Tasks      | Example                                     |
| -------------------------------------- | --------------------------- | ------------------------------------------- |
| *Linear Regression*                  | Regression                  | Predict house price, salary, temperature    |
| *Logistic Regression*                | Binary classification       | Spam vs. not spam, disease vs. healthy      |
| *Decision Tree*                      | Classification & regression | Customer churn, loan approval, house price  |
| *Random Forest*                      | Classification & regression | Fraud detection, risk prediction            |
| *K-Nearest Neighbors (KNN)*          | Classification & regression | Classify a customer, predict rating         |
| *Support Vector Machine (SVM)*       | Classification & regression | Image classification, text classification   |
| *Naive Bayes*                        | Mainly classification       | Spam detection, sentiment analysis          |
| *Artificial Neural Network (ANN)*    | Classification & regression | Image recognition, sales prediction         |
| *Gradient Boosting / XGBoost*        | Classification & regression | Credit scoring, fraud detection             |
| *LDA (Linear Discriminant Analysis)* | Classification              | Classifying documents or medical conditions |
----------------------------------------------------------------------------------------------------------------------

=======================================================================================================
| #  | Problem                                                            | Type                      |
| -- | ------------------------------------------------------------------ | ------------------------- |
| 1  | Classify emails as *spam or not spam*                            | Binary classification     |
| 2  | Classify an image as *cat or dog*                                | Binary classification     |
| 3  | Predict whether a tumor is *benign or malignant*                 | Binary classification     |
| 4  | Predict whether a customer will *churn or stay*                  | Binary classification     |
| 5  | Classify handwritten digits *0–9*                                | Multiclass classification |
| 6  | Classify flowers into *Iris Setosa, Versicolor, Virginica*       | Multiclass classification |
| 7  | Classify a transaction as *fraudulent or genuine*                | Binary classification     |
| 8  | Classify reviews as *positive or negative*                       | Binary classification     |
| 9  | Classify news articles into *sports, politics, technology, etc.* | Multiclass classification |
| 10 | Classify a person's health status based on medical measurements    | Classification            |
=======================================================================================================


"""
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score,classification_report

df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\ai projects\churn.csv")
# print(df.head())

# df["Churn"] = df["Churn"].map({1:"churn",0:"stay"})
# print(df.head())


X = df.drop(["CustomerID","Churn"],axis=1)
y = df["Churn"]
# print(X.head())


model = SVC(kernel="linear",random_state=42)

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = 0.3,random_state=42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_pred,y_test)
# print(accuracy)


unseen_df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\ai projects\unseen_churn.csv")

unseen_df = unseen_df.drop(["CustomerID"],axis=1)
# print(unseen_df.head())


result = pd.Series(model.predict(unseen_df))

print(result.map({1:"churn",0:"stay"}))
