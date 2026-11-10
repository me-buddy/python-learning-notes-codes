import pandas as pd
import numpy as np

df = pd.read_csv(r"PANDAS_TUTORIAL/e-commerce.csv")
# print(df.head())

df2 = df[["Category","Quantity","Price"]]

electronic_df = df.loc[(df["Category"] == "Electronics")]

# electronic_df["last_day_price"] = electronic_df["Price"].shift(1)
# electronic_df["difference"] = electronic_df["Price"].diff()

# # print(electronic_df)
# print(electronic_df[["Quantity" ,"Price","last_day_price" ,"difference","Shipping_Cost"  ,"Total_Amount"]])

roll = electronic_df["Price"].rolling(3).sum()
print(roll)
