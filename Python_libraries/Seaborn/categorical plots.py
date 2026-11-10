#^======================================SEABORN MODULE===================================
#^ =====================================CATEGORICAL PLOTS:================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""
Categorical plots are used to compare a numeric column with categorical(string) column
"""
df = sns.load_dataset("tips")
"""
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""
# ^Count Plot — sns.countplot()

# print(df.head())

# sns.barplot(
#     data = df,
#     x = "total"
# )
# plt.figure(figsize=(10,8))

# sns.barplot(
#             data=df,
#             x="sex",
#             y= "total_bill",
#             palette="bright"
# )

plt.figure(figsize=(15,10))

student_df = pd.DataFrame({
                        "names":["Ram","Mohan","suresh","Lakhan"],
                        "marks" :[20,30,40,20]
                        }
                        )
#* ============== count plot ===================
# sns.countplot(
#     data=student_df,
#     x="marks"
# )
# plt.show()

#* ============== bar plot =====================

# sns.barplot(data=student_df,y="marks",x="names",palette="dark")

# plt.title("Name wise Marks")
# plt.xlabel("names")
# plt.ylabel("marks")

# plt.show()


#* =============== Box Plot ====================
# sns.boxplot(data=df,x="day", y="total_bill",palette="bright")
# print(df.head())
# print()
# days_thur = df[df["day"]=="Thur"] # return all records related to thursday

# print("Max bill = ",days_thur["total_bill"].max())
# print("Minimum Bill = ",days_thur["total_bill"].min())

# print("Median Bill = ",days_thur["total_bill"].median())

# print("25% = ",(days_thur["total_bill"]*25)/100)
# print("50% = ",(days_thur["total_bill"]*50)/100)

# print("25% (Q1) =", days_thur["total_bill"].quantile(0.25))
# print("50% (Median) =", days_thur["total_bill"].quantile(0.50))
# print("75% (Q3) =", days_thur["total_bill"].quantile(0.75))

# plt.title("Box Plot of Total Bill by Day")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")
# plt.show()

# ======================== KDE Plot ===========================
# KDE => Kernel Density Estimation
# It is used to distribute data and represents smooth curve visualization.

df = pd.DataFrame(
    {
        "Names" : ["ram","Rahul","Karan","Jatin","Mahesh","Ganesh","Rahul singh","Dinesh","Manish"],
        "Marks" : [56,43,65,76,43,32,65,90,58]
    }
)


# print(data.shape) # (9, 2) => rows => 9 and Columns => 2
# print(data.describe())
# print(data.info())

# sns.kdeplot(
#     data=df,
#     x=df["Marks"]
# )

# sns.histplot(
#     data=df,
#     x = df["Marks"],
#     kde=True,
#     palette="bright"
# )
# plt.show()


tips = sns.load_dataset("tips")
# print(tips.info())

# sns.kdeplot(
#     data=tips,
#     x = tips["tip"],
#     palette="bright"

# )
# plt.show()

# ======================== violin Plot ========================
# It is combination of KDE + Box Plot
# It is used to show numerical Data Distribution on the basis of some categorical data.

# sns.violinplot(
#     data=tips,
#     x="tip",
#     y="total_bill",
#     hue="sex",
#     palette={
#         "Male": "#3498DB",
#         "Female": "#E91E63"
#     }
# )

"""
df = sns.load_dataset("titanic")
# sns.violinplot(data=df, x="class", y="age", hue="alive")
# sns.violinplot(data=df, x="class", y="age", hue="alive", fill=False)
# sns.violinplot(data=df, x="class", y="age", hue="alive", split=True, inner="quart")
sns.violinplot(data=df, x="age", inner_kws=dict(box_width=15, whis_width=2, color=".8"))
plt.show()
"""


# ============================ pair Plot ======================================
# It is used to show relationship of all numeric columns from a dataset/dataframe 
# To get relationship it provide two plots :- scatter plot and histogram

df = sns.load_dataset("iris")
# print(df.head())

# sns.pairplot(df,hue="sepal_length",palette="bright",diag_kind="hist")
# plt.show()

df=sns.load_dataset("iris")
sns.pairplot(df,hue="sepal_length",palette="dark",diag_kind="hist")
plt.show()

# ========================= matrix(heatmap) Plot =======================================
# correlations :- It arranges values in between -1 to +1.
# -1 => Opposite 
# 0 => No Relation
# +1 => Perfect match(Relation)
# .5 => 50% relation


df = pd.DataFrame({
"names" : ["Ram","Rahul","Raju","Raman","Rajeev","Rajendra"],
"rollNumber" : [1,2,3,4,5,6],
"marks" : [89,54,65,78,98,43]

})

# print(df.head())
# mat = df[["rollNumber","marks"]].corr()


# print(mat)



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset similar to the Iris dataset
data = pd.DataFrame({
    "sepal_length": [5.1, 4.9, 4.7, 6.3, 5.8, 7.1, 6.3, 6.5, 5.0, 5.9],
    "sepal_width": [3.5, 3.0, 3.2, 3.3, 2.7, 3.0, 2.9, 3.2, 3.6, 3.0],
    "petal_length": [1.4, 1.4, 1.3, 4.7, 4.1, 5.9, 4.9, 5.6, 1.5, 4.2],
    "petal_width": [0.2, 0.2, 0.2, 1.6, 1.0, 2.3, 1.5, 1.8, 0.2, 1.3],
    "species": ["setosa", "setosa", "setosa", "versicolor", "versicolor", 
                "virginica", "versicolor", "virginica", "setosa", "versicolor"]
})

# Compute correlation matrix (only numerical columns)
# corr = data.corr(numeric_only=True)

# # Create heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# sns.set_theme(style="darkgrid") 


# # Add title
# plt.title("Correlation Heatmap")

# # Show plot
# plt.show()


