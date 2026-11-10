"""
Most of the time, when we load any csv or other format file , the date time records are return in the form of string.
=> To convert this string values into real date and time format.

*=> df["dateTimeColumn"] = pd.to_datetime(df["dateTimeColumn"])

After convert this into date-time format we can access 

1. date
2. time
3. days
4. month
5. yead

"""
import pandas as pd

df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\olist_orders_dataset.csv")
# print(df.columns)
# [ 'order_id', 'customer_id', 'order_status', 'order_purchase_timestamp',
#   'order_approved_at', 'order_delivered_carrier_date',
#   'order_delivered_customer_date', 'order_estimated_delivery_date']
# print(df.head())

df.rename(columns={"order_delivered_carrier_date":"Order_date"},inplace=True)
# print(df.columns)

df["Order_date"] = pd.to_datetime(df["Order_date"])

# print(df["Order_date"].dtype) # datetime64[us]

print(df["Order_date"][0]) # 2017-10-04 19:55:00

# print(df["Order_date"][0].month)
# print(df["Order_date"][0].year)
# print(df["Order_date"][0].day_name())

# print(df["Order_date"].dt.year)

df["Date"] = df["Order_date"].dt.date # object

#* to convert date object into datetime format
df["Date"]=pd.to_datetime(df["Date"]) # datetime

print(df["Date"].dtype)
total_days = df[
    df["Date"] >= "2018-01-01"
].count()
print(total_days)

#* Here we set Order_date column into index based column
df.set_index("Order_date", inplace=True)

# Now 2017-10-04 19:55:00 is an Index
#print(df.loc["2017-10-04 19:55:00"])
