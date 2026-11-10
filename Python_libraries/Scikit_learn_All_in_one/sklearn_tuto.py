"""
Machine Learning :-
-------------------
AI => Artificial Intelligence
=> Machine Learning :- Past Records ===> Patterns  ===> Predict
Algorithms => Mathematical Rules (Formulas)
=> Deep Learning
=> Neural Networks  => Structure Human Brain


ML :-
------
Supervised learning => Labeled Data
Unsupervised learning => Un-labeled
Semi-Supervised
Reinforcement Learning => Agent => reward and Penelties


scikit learn => supervised and Unsupervised learning
Deep learning :- Pytorch , Tensorflow, etc

==================================================================
1950 => Allan Turing  => Turing Test ===> Artificial Intelligence

1956 => John Mc Harty => Artificial Intelligence


1997 => IBM Deep Blue => Chess Champion

AlphaGo (google) => Go => 2016

Transformers => Self-Attention  => 2017

Generative AI => 2020
chatGPT => 2022


============================
Algorithm => A mathmatical representation of Problem
==========================================================================
1. Business Problem
2. Data Clean => fill (numerical => mean , mode | categorical => median) , remove
3. Features Extract => columns 
4. train(80%) and testing(20%)
5. Model Selection 
6. Predict
7. Report
8. Deploy

-------------------------------------------------------------
House Price Prediction 
~~~~~~~~~~~~~~~~~~~~~~~
length
width
location
nearBy

Predict :-
-----------
Price 

X => Input Features 
y => Target/output/label


====================================

supervised learning => Regression(Numerical) and Classification(categorical)


*=> To install scikit learn :- pip install scikit-learn

"""
'''
# import sklearn.datasets

# from sklearn.datasets import load_iris
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


dataset = sklearn.datasets.load_iris()
# print(type(dataset)) # <class 'sklearn.utils._bunch.Bunch'>
# data
# feature_names

# for i in dataset:
#     print(i)
    
data = dataset["data"]
target = dataset["target"]
features = dataset["feature_names"]

# print(data.shape) # (150, 4)
"""
data
target
frame
feature_names
target_names
images
DESCR
"""

# print(dataset.feature_names) # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# print(dataset.target_names) # ['setosa' 'versicolor' 'virginica']


X = dataset.data
y = dataset.target

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    train_size=.8,
    test_size=.2,
    random_state=45
)
# print(X_test)
# # [5.1 3.5 1.4 0.2]
# print(X_train.shape)
# print(X_test.shape)


model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# print(y_pred)


accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy) # Accuracy: 0.9666666666666667

new_flower = [[0.1, 0.5, 0.4, 0.2]]

prediction = model.predict(new_flower)

print("Predicted class:", dataset.target_names[prediction[0]])
'''

# ============================================= Heart Disease ==========================================
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

dataset = load_breast_cancer()

# print(dataset.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])

X = dataset["data"]
y = dataset["target"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2 , random_state=42)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train,y_train)
testing_prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, testing_prediction)
# print(accuracy)
"""
X = 30 tumor-related features

y = target/class

0 = malignant

1 = benign
"""
new_tumor = [X_test[0]]

prediction = model.predict(new_tumor)

if prediction[0] == 0:
    print("Malignant")
else:
    print("Benign")

# print(X.shape) # (569, 30)
# print(y.shape) # (569,)

# print(dataset["target_names"])



"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

^# 1. Dataset load
iris = load_iris()

X = iris.data
y = iris.target

^# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

^# 3. Model create
model = KNeighborsClassifier(n_neighbors=3)

^# 4. Training
model.fit(X_train, y_train)

^# 5. Prediction
y_pred = model.predict(X_test)

^# 6. Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

"""