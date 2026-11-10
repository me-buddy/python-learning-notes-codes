
import pandas as pd

file = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\e-commerce.xlsx")
# print(file)


# df = file[file["Category"]=="Electronics"] # SINGLE CONDITION



"""
To get records based on multiple conditions :-
----------------------------------------------
& => used to perform logical and 
| => used to perform logical or
~ => used to perform logical not

SYNTAX :  df[(condition1) & (condition2)]
--------

To get specific columns records based on condition
=> .loc(condition,[columnName1,columnName2,..])
ex:-
-----
df2 = file.loc[(file["Category"]=="Electronics") | (file["Category"]=="Sports"),["Customer_ID","Category","Total_Amount"]]

"""
# df = file[file["Category"]=="Electronics"]

# df2 = file[(file["Category"]=="Electronics") | (file["Category"]=="Sports"),["Customer_ID","Category","Total_Amount"]]
# df3 = file.loc[(file["Category"]=="Electronics") | (file["Category"]=="Sports"),["Customer_ID","Category","Total_Amount"]]
# df4 = file[file["Category"].str.startswith("C")]

cricket_df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\NUMPY TUTORIAL\cricket_stats.csv")
names_start_A = cricket_df[cricket_df["Player"].str.startswith("A")]
# print(names_start_A)

# print(cricket_df.info())

print(cricket_df["Runs"].mean())



# print(file.shape) # (100, 8) => 100 ROWS and 8 columns
# print(file.size) # 800
# print()

# .head() :- It returns the first 5 rows data from the file.
# .head(n) :- It returns  first number of rows from the file.
# ------------------------------------------------------------------------------
# .tail() :- It return the last 5 records from the file.
# .tail(n) :- It returns the last n of rows from the file.

# ------------------------------------------------------------------------------
# .describe() :- return the statistical summary of the entire numberic records
# .dtypes :- return the summary of the all columns from the file.
# .columns :- return the list of all columns from the dataFrame

#--------------------------------------------------------------------------------
# .iloc[numberIndex]
# loc[rowNumber , "columnName"]

head = file.head()
head = file.head(15)
tail = file.tail()
tail = file.tail(15)

# print(file.dtypes)

# print(file.columns)
# Index(['Order_ID', 'Customer_ID', 'Category', 'Quantity', 'Price', 'Discount','Shipping_Cost', 'Total_Amount'], dtype='str')

# print(file["Category"]) # <class 'pandas.Series'>

# print(file[["Category","Quantity"]].head()) # <class 'pandas.DataFrame'>


#* get records from a range
#^ df.iloc[startIndex : stopIndex+1 : step+1]
# print(file.iloc[3:15])


# print(file.loc[:, ["Category", "Quantity"]])

# Filter records 
# print(file.loc[file["Category"] == "Electronics", "Quantity"])

# print(file[file["Category"] == "Electronics"])

#* Read sql file
#^ pd.read_sql("sql_query",conection)

#! NOTE :- To read sql file data we have to create a sql connection using "mysql-connector-python" Module.
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "sreyas"
)


# print(df)

#* filtering Records  :- For Sql filtering we have to change in our sql query.
# ex:-
# ----
sql = "SELECT * FROM practice where class=11"
df = pd.read_sql(sql,connection)
pd.read

# print(df["name"])

# df = df[df["class"]==11]
# print(df)
connection.close()