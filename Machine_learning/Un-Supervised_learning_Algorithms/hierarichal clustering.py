"""
#^================= Hierarichal CLUSTERING ==================
#^================= agglmerative Clustering ===================== 


clustering => groups => These are not prerior known
----------------------------------------------------
=> KMeans

=> Hierarichal Clustering => It treats every data point(features) as a cluster

Here we have to create a group on the basis of similaries/distance of two clusters :-
--------------------------------------------------------------------------------------
formula to claculate distance => Euclidian Distance

=> single linkage => minimum distance between two points.
=> complete linkage => maximum distance between two points. 
=> Average linkage => Average distance between two points.
=> centeroid linkage => Centeroid distance between two poins.
=> Ward => variance distance between two points.


dendrogram

There are two types of hierarichal clustering :-
-------------------------------------------------
=> divisive - top-bottom approch
=> agglomerative -  bottom-top  approch
"""


"""
Clustering algorithms are useful in -
    *information theory, 
    *target detection, 
    *communications, 
    *compression, and other areas. 
The vq module only supports vector quantization and the k-means algorithms.

The hierarchy module provides functions for hierarchical and agglomerative clustering. 
Its features include generating hierarchical clusters from distance matrices, 
calculating statistics on clusters, cutting linkages to generate flat clusters, 
and visualizing clusters with "dendrograms".
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

from scipy.cluster.hierarchy import linkage,dendrogram
from sklearn.cluster import AgglomerativeClustering


df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\ai projects\Mall_Customers.csv")
# print(df.columns)
"""
Index(['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
       'Spending Score (1-100)'],
      dtype='str')
"""

df = df[["Annual Income (k$)","Spending Score (1-100)"]]
# print(df.head())


#* Here we scaled data .
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
# print(X_scaled)

#* Here we create a linkage between data. 
link = linkage(X_scaled,method="ward")
# print(link)


# * Creating a Dendogram Structure

dendrogram(link)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Annual Incove VS Speding Score")
plt.show()

model = AgglomerativeClustering(n_clusters=5)

prediction = model.fit_predict(X_scaled)
# print(len(prediction))
# print(len(prediction))
s = pd.Series(prediction)
# print(s.value_counts())

cluster_names = {
    0: "Thrifty Savers",
    1: "Standard Consumers",
    2: "Market Stars",
    3: "Target Targets",
    4: "Careless Spenders"
}

df['Persona_Name'] = s.map(cluster_names)
print(df["Persona_Name"].value_counts())
