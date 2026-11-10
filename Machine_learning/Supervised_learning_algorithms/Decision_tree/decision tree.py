import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV


df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\ai_projects\loan_approval_dataset.csv")

#* removes all spaces from the columns of dataset. 
df.columns = df.columns.str.strip()

# print(df.head())
# print(df.columns)
# for i in df.columns:
#     print(i,end=" , ")

# print(df[[" loan_term"," loan_amount"," loan_status"]])

# print(df["bank_asset_value"])
# print(df["loan_status"])
"""
Index(['loan_id', ' no_of_dependents', ' education', ' self_employed',
       ' income_annum', ' loan_amount', ' loan_term', ' cibil_score',
       ' residential_assets_value', ' commercial_assets_value',
       ' luxury_assets_value', ' bank_asset_value', ' loan_status'],
      dtype='str')
"""


# Rejected , Approved

# print(df.shape)
# total  records => 4268

# loan_not_approved = df[df[" loan_status"] == "Rejected"]
# loan_approved = df[df[" loan_status"] == "Approved"]

# print("Rejected loans : ", loan_not_approved)
# print("Approved loans : ", loan_approved)


# table = pd.pivot_table(
#     df,
#     index=" loan_amount",
#     values=" loan_status",
#     aggfunc="count"
# )
# print(table)


# rejected = df.loc[df[" loan_status"]=="Approved"," loan_status"].value_counts()
# print(rejected)



#* Get percentage of out of total loans how many rejected and how many approved
counts = df["loan_status"].value_counts()
"""
loan_status
Approved    2656
Rejected    1613
Name: count, dtype: int64
"""
# print((2656/4269)*100) => 62.2%
# print((1613/4269)*100) => 37.78%

#* average loan amount that bank approved  
avg_approved_amount = df.loc[df["loan_status"] == " Approved", "loan_amount"].mean()
# print(f"Average Approved Loan: {avg_approved_amount:,.2f}")
# Average Approved Loan: 15,247,251.51

avg_rejected_amount = df.loc[df["loan_status"] == " Rejected", "loan_amount"].mean()
# print(f"Average Approved Loan: {avg_rejected_amount:,.2f}")
# Average Rejected Loan: 14,946,063.24

# print(df["education"].unique())  # [' Graduate', ' Not Graduate']

# print(df["self_employed"].unique()) # [' No', ' Yes']

print(df["loan_status"].unique()) # [' Approved', ' Rejected']



# print(df["loan_status"].unique())
"""
<StringArray>
[' Approved', ' Rejected']
Length: 2, dtype: str
"""


approved_loan = df.loc[df["loan_status"] == " Approved", ["loan_amount","loan_term","cibil_score","bank_asset_value"]]
# print(f"Average Approved Loan: {approved_loan}")


# --------------------- machine learning ------------------------------------
drop = df.drop(columns=["loan_status"])  # remove/drop entire column from dataframe
X = drop
y = df["loan_status"]

# print(X.head())
# print(y.head())


# print(X.describe())
# print(X.info())

#* Encode categorial/string data into numeric By using .map({"value":number ,...}) from pandas   

X["education"]     = X["education"].map({' Graduate':1,' Not Graduate':0})
X["self_employed"] = X["self_employed"].map({' No':0 , " Yes":1})

y = df["loan_status"]  # Use the exact column name with/without space

y = y.map({" Approved": 1, " Rejected": 0})

# 3. Check the distribution to confirm it worked perfectly
# print(y)

model_tree = DecisionTreeClassifier(criterion="gini",random_state=42,max_depth=5)

X_train,X_test,y_train,y_test = train_test_split(
                                        X,y,
                                        train_size=0.7 ,
                                        test_size=0.3 ,
                                        random_state=42) 

#* Here model learns from training data.
model_tree.fit(X_train , y_train)

# X_pred = model_tree.predict(X_train)
y_train_pred = model_tree.predict(X_train)

accuracy = accuracy_score(y_train, y_train_pred)
# print(f"Training Accuracy: {accuracy:.4f}") # Training Accuracy: 0.9796

columns = [
    "loan_id", "no_of_dependents", "education", "self_employed", 
    "income_annum", "loan_amount", "loan_term", "cibil_score", 
    "residential_assets_value", "commercial_assets_value", 
    "luxury_assets_value", "bank_asset_value"
]

unseen_data = [
    # Case 1: Low-risk applicant (High income, excellent CIBIL score, low loan ratio)
    [2, 1, 1, 0, 12000000, 15000000, 24, 820, 5000000, 20000000, 30000000, 12000000],
    
    # Case 2: High-risk applicant (High dependents, poor CIBIL score, low assets)
    [3, 4, 0, 1, 3500000, 18000000, 12, 450, 500000, 0, 1200000, 800000],
    
    # Case 3: Borderline applicant (Decent score, but asking for a very large loan relative to income)
    [4, 2, 1, 0, 5000000, 45000000, 36, 680, 4000000, 8000000, 10000000, 3500000]
]

X_unseen = pd.DataFrame(unseen_data, columns=columns)


new_pred = model_tree.predict(X_unseen)
print(new_pred)


"""
X => Features/input or data which we given to machine to learn.
y => output/target => On the basis of this data machine model will predict

100% of Data.

Training => 80%  
Testing => 20%

X_train    , y_train   ==> 80% >> seen data
X_test     , y_test    ==> 20% >> unseen data
(question) , (answer)

model.fit(X_train , y_train) ===> machine learns from this data.

*==> prediction on testing data 

y_test_pred = model.predict(X_test) => 90%
accuracy_score(y_test  , y_test_pred)


*==> prediction on training data

y_train_pred = model.predict(X_train)
accuracy_score(y_train , y_train_pred) 


"""

