# ===============================================Hist and scatter
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Record_ID": range(1, 101),
    "Score": [
        42, 55, 67, 71, 83, 59, 64, 78, 91, 73,
        48, 62, 69, 75, 81, 88, 53, 57, 66, 72,
        45, 51, 63, 70, 76, 84, 89, 94, 58, 61,
        39, 47, 54, 68, 74, 79, 82, 87, 92, 97,
        43, 56, 65, 71, 77, 85, 90, 95, 60, 69,
        50, 52, 59, 64, 73, 78, 83, 86, 91, 96,
        41, 49, 55, 67, 70, 75, 80, 84, 88, 93,
        44, 53, 61, 66, 72, 76, 81, 85, 89, 98,
        46, 57, 63, 68, 74, 79, 82, 87, 92, 99,
        38, 48, 56, 62, 65, 71, 77, 83, 90, 94
    ]
}

df = pd.DataFrame(data)


# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# for i in df["Score"]:
#     if(i>=0 and i<=40):
#         count1+=1
#     if(i>40 and i<=50):
#         count2+=1
#     if(i>50 and i<=70):
#         count3+=1
#     if(i>70 and i<=80):
#             count4+=1
#     if(i>80 and i<=100):
#             count5+=1

# print("Total students Scores between 0-40 Marks : ",count1)
# print("Total students Scores between 40-50 Marks : ",count2)
# print("Total students Scores between 50-70 Marks : ",count3)
# print("Total students Scores between 70-80 Marks : ",count4)
# print("Total students Scores between 80-100 Marks : ",count5)

# plt.figure(figsize=(10, 7))

plt.hist(
    df["Score"],
    bins=[30, 40, 50, 60, 70, 80, 90, 100],
    # orientation="horizontal",
    edgecolor="black",
    color="skyblue"
)

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Scores")
plt.show()
# ============================== E-Commerce DataFrame ================================
# df2 = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\PANDAS_TUTORIAL\e-commerce.csv")
# print(df2.head())
# total_records = df2["Total_Amount"].count()
# print("\nTotal Records : ",total_records)
# print("Manimum Total Amount  : ",df2["Total_Amount"].min())
# print("Maximum Total Amount  : ",df2["Total_Amount"].max())


# plt.hist(df2["Total_Amount"],bins=[400,800,1200,1600,1800,2000,2200],edgecolor="red",orientation="horizontal")
# plt.show()
# plt.hist(df["Score"], bins=7, edgecolor="black")


# plt.scatter(df2["Category"],df2["Price"])
# plt.show()


import pandas as pd

data = {
    "Student_ID": range(1, 101),

    "Hours_Studied": [
        1.2, 2.5, 3.1, 4.0, 5.2, 2.8, 6.1, 7.0, 8.2, 4.5,
        1.8, 3.5, 4.2, 5.8, 6.5, 7.2, 8.5, 2.2, 3.8, 5.0,
        1.5, 2.9, 4.5, 6.0, 7.5, 8.0, 9.2, 3.2, 4.8, 5.5,
        2.0, 3.0, 5.2, 6.8, 7.8, 8.7, 9.5, 4.1, 5.9, 6.3,
        1.7, 2.7, 3.9, 5.1, 6.2, 7.4, 8.3, 9.0, 4.6, 5.7,
        2.3, 3.4, 4.7, 5.6, 6.7, 7.1, 8.8, 9.3, 3.7, 5.3,
        1.4, 2.6, 4.3, 5.4, 6.4, 7.7, 8.1, 9.1, 4.9, 6.0,
        2.1, 3.6, 4.4, 5.0, 6.6, 7.3, 8.6, 9.4, 3.3, 5.8,
        1.9, 2.4, 3.8, 5.5, 6.9, 7.6, 8.4, 9.6, 4.0, 5.2,
        2.8, 3.9, 4.5, 6.1, 7.0, 8.2, 9.0, 3.5, 5.4, 6.8
    ],

    "Exam_Score": [
        42, 48, 55, 61, 68, 52, 73, 79, 88, 64,
        45, 57, 62, 71, 75, 81, 89, 50, 59, 67,
        44, 53, 63, 72, 82, 86, 94, 56, 65, 70,
        47, 54, 69, 77, 84, 91, 96, 60, 74, 78,
        43, 51, 58, 66, 73, 80, 87, 92, 63, 71,
        49, 56, 64, 69, 76, 82, 90, 95, 58, 68,
        41, 50, 61, 67, 74, 83, 85, 93, 65, 72,
        46, 55, 60, 66, 78, 81, 88, 97, 54, 70,
        45, 49, 57, 71, 79, 85, 90, 98, 62, 69,
        52, 59, 64, 73, 80, 86, 94, 55, 67, 76
    ]
}

df = pd.DataFrame(data)

# # print(df)
# plt.figure(figsize=(10,7))
# plt.scatter(df["Hours_Studied"],df["Exam_Score"])
# plt.xlabel("Hour Studies")
# plt.ylabel("marks")

# plt.bar(df["Hours_Studied"],df["Exam_Score"])
# plt.hist(df["Hours_Studied"],edgecolor="aqua")
# plt.xlabel("Hour Studies")
# plt.ylabel("Number of Students")
# counts = df["Hours_Studied"].value_counts()
# print(counts)

# table = pd.pivot_table(
#      df,
#      index="Hours_Studied",
#      values="Exam_Score",
#      aggfunc="count"
# )
# print(table)

count=0
c=0
for i in df["Hours_Studied"]:
    #  print(i)
    if(i>=0 and i<=2):
         count+=1
    if(i>2.2 and i<=3):
             c+=1
# print(count)
# print(c)
# plt.show()