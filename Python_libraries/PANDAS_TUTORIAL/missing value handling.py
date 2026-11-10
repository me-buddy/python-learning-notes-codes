"""
===========================================Missing value:=======================================
* .drop(columnName,axis=1) => remove entire column from dataFrame
OR
* .drop(index,axis=0) => remove entire row from dataFrame

axis = 0 ==> row_wise
axis = 1 ==> column_wise

.isna()
"""

import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\e-commerce.csv")
# # ['Order_ID', 'Customer_ID', 'Category', 'Quantity', 'Price', 'Discount','Shipping_Cost', 'Total_Amount']
# df = df.drop("Quantity",axis=1) # Remove Column
df = df.drop(3, axis=0) # remove row
# print(df.head())

# print(df.isna().sum())
# print(df.isnull().sum())



# -------------------------------------------------------------------------
data = {
    "Name": ["Deepak", "Aman", None, "Rohit", "Priya"],
    "Age": [21, np.nan, 23, 25, None],
    "City": ["Agra", "Delhi", "Mumbai", None, "Lucknow"],
    "Salary": [30000, 45000, np.nan, 50000, None]
}

df = pd.DataFrame(data)

# print(df)
# print(df.isna())
# print(df.isna().sum())

# df = df["Salary"].dropna(axis=0)
# df = df.dropna(axis=0)
salary_average = average = df["Salary"].median()
df2=df["Salary"].fillna(salary_average)
df = df["City"].fillna(df["City"].mode())
print(df)
# print((30000+45000+50000)/3)

"""
categorical data(column) ==> column which contains string value 
numeric data(column) ==> column which contains numeric value

RULE:-
------
categorical ==> .mode()
numeric ======> .mean() , .median()
---------------------------------------------------------------------
mean()
median()
mode()
"""