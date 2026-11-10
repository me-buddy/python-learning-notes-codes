"""
Metrices  => sklearn.metrics
-----------------------------
Supervised
(classfication and Regression)
 => Accuracy-score , Precision , Recall , F1 Score , Rou-Auc , etc...

and 

unsupervised
(clustring and Dimensionality Reductions)
 => MSE 


"""
"""
Algorithms :-
--------------
Supervised learning => labeled => input + outputs
=> Classification ===> Predict Categorical Data
    -> Logistic Regression
    -> Decision Tree Classifier
    -> Random Forest Classifier
    -> SVM
    -> Naive Byes
    
=> Regression =======> Predict Numeric Data 
    -> Linear Regression
    -> Decision Tree Regressor
    -> Random Forest Regressor

Un-Supervised learning => Unlabeled Data

Reinforcement learning

=======================================  Logistic Regression ===========================================
It is used to find the probability of any categoriacal Data.
Mostly used for binary type outputs.

NOTE : The probability should be in between 0 and 1.
ex:- p => .67 => 67% 
ex:- p => .7 =>  70% 
ex:- p => .89 => 89% 
 

=> yes / no
=> spam / Not Spam
=> Loan Apporoved / Not Approved
=> Fail / Pass.

Data => Input features / output(target/label)

Study_hours | Result
-------------------------
6               1(pass)
7               1(pass)
3               0(Fail)
8               0(Fail)
5               1(pass)
4               0(Fail)

5.5(Y_Test)  
--------------------------
feature => Study_hours ===> No of Features => 1 => X1
target/label => Result



1. Find the Linear Relation in Data 

z = b0 + b1.x1  ====> for single feature(input data) 
z = b0 + b1.x1 + b2.x2 + b3.x3 + ....   ===> More than one feature.

x1,x2,x3 => features 
b0 => Intercept
b1,b2,b3 => Cofficient/weight


2. Sigmoid Function => It brings value of z in between 0 and 1.

sigmoid = 1/1+e**-z


3. Find Probability using sigmoid value.

*=================================================================================================================
*============================================= DECISION TREE =====================================================
It works for both supervised learning algorithm - classification and regression 
=> DecisionTreeClassifier :- for categorical data. 
=> DecisionTreeRegressor  :- for numerical data.

It creates a tree like structure to decide/predict on unseen data.

product => probability 
Earbirds

----------------------------------
age  salary  product_parchase
----------------------------------
20      25K     1
30      30K     1
45      50K     0
18      10K     0 
19      17K     1 
-----------------------------------

(condition)
root Node
middle nodes
leaf Nodes 

(age >= 20)===> root node

 => yes => 20,30,45 ==> salary>10K(middle node) ==> yes(1,1)  | No(1)(leaf node)
 => no => 18 ==> (salary>15K)(middle node) ==> yes(1) | No(0) (leaf node)


*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""