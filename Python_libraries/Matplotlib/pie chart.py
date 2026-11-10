"""
Pie chart is used to find the percentage of distribution 
"""
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\e-commerce.csv")
# print(df.head())

# categories = df["Category"].unique()
# print(categories)

students = ["Ram","Shyam","Karan","Rahul"]
attendence  = [90,70,80,87]
marks  = [89,65,76,87]
# plt.figure(figsize=(10,8))
# plt.scatter(attendence,marks,marker="*")
color = ["grey","pink","yellow","red"]
plt.pie(
    marks,
    labels=students,
    autopct="%1.3f%%",
    colors=color
)
plt.show()