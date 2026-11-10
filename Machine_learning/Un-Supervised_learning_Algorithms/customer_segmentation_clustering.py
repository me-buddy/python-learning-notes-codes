import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\ai projects\Mall_Customers.csv")


# print(df.columns) 
# ['CustomerID', 'Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']
# print(df.describe())
# print(df.info())

# print(df["Gender"].value_counts())

# plt.bar(
#     df["Age"],
#     df["Annual Income (k$)"]
# )
# plt.xlabel("Age")
# plt.ylabel("Annual Income")
# plt.title("Age VS Annual Income")
# plt.show()

df["inr"] = df["Annual Income (k$)"]*95.30 
df2 = df[["Age","Annual Income (k$)","inr"]]
df3 = df[["Age","Spending Score (1-100)"]]

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df[["Annual Income (k$)","Spending Score (1-100)"]])

# data[n] => row+column ==> data[row,col] ===> data[:,n]
# print(data[:,0])
# print(data[:,1])
# print(data)


# for k in range(1,11):
#     kmean = KMeans(
#         n_clusters=k,
#         random_state=42,
#         n_init=10
#     )
    
#     score = kmean.fit_predict(data)
    
#     silhouette_score(data,score)


wcss = []
silhouette_scores = []

for k in range(2,11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_data)
    
    wcss.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_data, cluster_labels))

# Plotting the Elbow Method
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(range(2,11), wcss, marker='o', color='blue') # line plot
plt.title('Elbow Method')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS / Inertia')

# Plotting Silhouette Scores
plt.subplot(1, 2, 2)
plt.plot(range(2,11), silhouette_scores, marker='o', color='orange')
plt.title('Silhouette Scores')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Silhouette Score')

plt.tight_layout()
plt.show()

# for i in silhouette_scores:
#     print(i)

