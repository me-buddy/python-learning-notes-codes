import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv(
    r"C:\Users\sagar\Desktop\shreyas AIML\ai projects\loan_approval_dataset.csv"
)


# ============================================================
# 2. CLEAN COLUMN NAMES
# ============================================================

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Columns:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)


# ============================================================
# 3. CHECK LOAN STATUS
# ============================================================

print("\nLoan Status:")
print(df["loan_status"].value_counts())


# ============================================================
# 4. BASIC INFORMATION
# ============================================================

print("\nDataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 5. AVERAGE LOAN AMOUNT
# ============================================================

avg_approved_amount = df.loc[
    df["loan_status"] == " Approved",
    "loan_amount"
].mean()

avg_rejected_amount = df.loc[
    df["loan_status"] == " Rejected",
    "loan_amount"
].mean()

print(
    f"\nAverage Approved Loan Amount: "
    f"{avg_approved_amount:,.2f}"
)

print(
    f"Average Rejected Loan Amount: "
    f"{avg_rejected_amount:,.2f}"
)


# ============================================================
# 6. MACHINE LEARNING
# ============================================================

# Remove target column and loan_id
# loan_id is not useful for predicting loan approval
X = df.drop(
    columns=["loan_status", "loan_id"]
).copy()

# Target variable
y = df["loan_status"].copy()


# ============================================================
# 7. ENCODE CATEGORICAL DATA
# ============================================================

# Education
#
# Graduate     -> 1
# Not Graduate -> 0

X["education"] = X["education"].map({
    " Graduate": 1,
    " Not Graduate": 0
})


# Self employed
#
# No  -> 0
# Yes -> 1

X["self_employed"] = X["self_employed"].map({
    " No": 0,
    " Yes": 1
})


# ============================================================
# 8. ENCODE TARGET VARIABLE
# ============================================================

# Approved -> 1
# Rejected -> 0

y = y.map({
    " Approved": 1,
    " Rejected": 0
})


# Check encoded data
print("\nEncoded Features:")
print(X.head())

print("\nEncoded Target:")
print(y.head())


# ============================================================
# 9. TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=0.70,
    test_size=0.30,
    random_state=42,
    stratify=y
)


print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)


# ============================================================
# 10. CREATE DECISION TREE MODEL
# ============================================================

model_tree = DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)


# ============================================================
# 11. HYPERPARAMETER TUNING
# ============================================================

param_grid = {
    "max_depth": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10
    ],

    "min_samples_split": [
        2, 3, 4, 5, 7
    ]
}


gridCV = GridSearchCV(
    estimator=model_tree,
    param_grid=param_grid,
    scoring="accuracy",
    cv=5,
    n_jobs=-1
)


# ============================================================
# 12. TRAIN MODEL
# ============================================================

gridCV.fit(
    X_train,
    y_train
)


# ============================================================
# 13. BEST PARAMETERS
# ============================================================

print("\n====================================")
print("BEST MODEL")
print("====================================")

print(
    "Best Parameters:",
    gridCV.best_params_
)

print(
    "Best Cross Validation Score:",
    gridCV.best_score_
)


# ============================================================
# 14. TRAINING PREDICTION
# ============================================================

y_train_pred = gridCV.predict(
    X_train
)

train_accuracy = accuracy_score(
    y_train,
    y_train_pred
)

print(
    f"\nTraining Accuracy: "
    f"{train_accuracy:.4f}"
)


# ============================================================
# 15. TESTING PREDICTION
# ============================================================

y_test_pred = gridCV.predict(
    X_test
)

test_accuracy = accuracy_score(
    y_test,
    y_test_pred
)

print(
    f"Testing Accuracy: "
    f"{test_accuracy:.4f}"
)


# ============================================================
# 16. CLASSIFICATION REPORT
# ============================================================

print("\n====================================")
print("CLASSIFICATION REPORT")
print("====================================")

print(
    classification_report(
        y_test,
        y_test_pred,
        target_names=[
            "Rejected",
            "Approved"
        ]
    )
)


# ============================================================
# 17. PREDICT NEW / UNSEEN DATA
# ============================================================

columns = [
    "no_of_dependents",
    "education",
    "self_employed",
    "income_annum",
    "loan_amount",
    "loan_term",
    "cibil_score",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value"
]


# ------------------------------------------------------------
# New applicants
# ------------------------------------------------------------

unseen_data = [

    # Case 1
    # High income
    # Graduate
    # Good CIBIL
    # Good assets

    [
        1,          # no_of_dependents
        1,          # education -> Graduate
        0,          # self_employed -> No
        12000000,   # income_annum
        15000000,   # loan_amount
        24,         # loan_term
        820,        # cibil_score
        5000000,    # residential_assets_value
        20000000,   # commercial_assets_value
        30000000,   # luxury_assets_value
        12000000    # bank_asset_value
    ],


    # Case 2
    # Low income
    # Not Graduate
    # Poor CIBIL
    # Low assets

    [
        4,          # no_of_dependents
        0,          # education -> Not Graduate
        1,          # self_employed -> Yes
        3500000,    # income_annum
        18000000,   # loan_amount
        12,         # loan_term
        450,        # cibil_score
        500000,     # residential_assets_value
        0,          # commercial_assets_value
        1200000,    # luxury_assets_value
        800000      # bank_asset_value
    ],


    # Case 3
    # Medium income
    # Large loan
    # Decent CIBIL

    [
        2,          # no_of_dependents
        1,          # education -> Graduate
        0,          # self_employed -> No
        5000000,    # income_annum
        45000000,   # loan_amount
        36,         # loan_term
        680,        # cibil_score
        4000000,    # residential_assets_value
        8000000,    # commercial_assets_value
        10000000,   # luxury_assets_value
        3500000     # bank_asset_value
    ]
]


# ============================================================
# 18. CREATE DATAFRAME FOR NEW DATA
# ============================================================

X_unseen = pd.DataFrame(
    unseen_data,
    columns=columns
)


print("\n====================================")
print("NEW APPLICANTS")
print("====================================")

print(X_unseen)


# ============================================================
# 19. PREDICT
# ============================================================

new_pred = gridCV.predict(
    X_unseen
)


# ============================================================
# 20. DISPLAY PREDICTIONS
# ============================================================

print("\n====================================")
print("LOAN PREDICTIONS")
print("====================================")

for i, prediction in enumerate(
    new_pred,
    start=1
):

    if prediction == 1:
        result = "Approved"
    else:
        result = "Rejected"

    print(
        f"Case {i}: {result}"
    )
