"""
==================================== pivot table ====================================
it is used to summarize the dataframe on the basis of some aggregated functions.

pivotTableName = pd.pivot_table(
                    dataFrameName,
                    index=["columnName"],
                    value = ["columnName"],
                    aggfunc = ["sum"]
                )


"""
import pandas as pd

df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\e-commerce.csv")

# print(df.columns)
# ['Order_ID', 'Customer_ID', 'Category', 'Quantity', 'Price', 'Discount','Shipping_Cost', 'Total_Amount']

# print(df["Category"].unique()) # ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']

electronic_df = df[df["Category"]=="Electronics"]
Clothing_df = df[df["Category"]=="Clothing"]
Books_df = df[df["Category"]=="Books"]
Sports_df = df[df["Category"]=="Sports"]
Home_df = df[df["Category"]=="Home"]


# print(electronic_df)
print("\n------------------------------------------------------------------\n")
# print(Clothing_df)
# print("\n------------------------------------------------------------------\n")
# print(Books_df)
# print("\n------------------------------------------------------------------\n")
# print(Sports_df)
# print("\n------------------------------------------------------------------\n")
# print(Home_df)

electronic_sum = electronic_df["Total_Amount"].sum()
electronic_mean = electronic_df["Total_Amount"].mean()
Sports_sum = Sports_df["Total_Amount"].sum()
Books_sum= Books_df["Total_Amount"].sum()
Home_sum = Home_df["Total_Amount"].sum()
Clothing_sum = Clothing_df["Total_Amount"].sum()
print("Total amount Invest on Electronic Category :- ",electronic_sum)
print("Average amount Invest on Electronic Category :- ",electronic_mean)
# print("Total amount Invest on Sports Category :- ",Sports_sum)



pv_table = pd.pivot_table(
                            df,
                            index=["Category"],
                            values=["Quantity","Total_Amount"],
                            aggfunc=["sum","mean","count","min","max"]

                          )

print(pv_table)