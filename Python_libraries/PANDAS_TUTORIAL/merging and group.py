"""
# ======================== merging two or more tables =========================
Mysql Join  => Merge two or more tables based on common column in between them.

inner join 
left join 
right join
cross join => left join + right join
outer join


In pandas Merge is same as mysql joins.
"""
import pandas as pd
import numpy as np


customer_df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\olist_customers_dataset.csv") 
order_df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\olist_orders_dataset.csv") 
# print(customer_df.head())

# print(customer_df.columns)
# print(customer_df.size)
# print(customer_df.shape)


# print("customers DF columns \n\n",customer_df.columns)
# print("\n\nOrder DF columns \n\n",order_df.columns)

# common Column => customer_id


#* pd.merge(df1,df2, on="commonColumnName" , how="inner/left/right/outer") 

# df = pd.merge(customer_df,order_df, on="customer_id")
df = pd.merge(customer_df,order_df, on="customer_id",how ="outer")

# print(df.size) # 1193292 => innerJOIN
# print(df.size) # 1193292 => leftJOIN

# print(df.head())

# for i in df:
#     print(i)
#     print("-------------------")

""" 
customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state,
order_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delive
"""
# .loc[row,column]
selected_columns_df = df.loc[:,["customer_id","customer_city","order_id","order_purchase_timestamp"]]

unique_cities = np.unique(df["customer_city"])

# print(len(unique_cities))
# print(unique_cities)

# print(selected_columns_df.shape)


"""
======================================= group columns in pandas ====================================

df.groupby("columnName")["common Value"].aggregatedFunction()
"""
# abadiania
group = df.groupby("customer_city")["order_purchase_timestamp"].count()
print(group)
print(group.head())