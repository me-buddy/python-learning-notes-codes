"""
1. Clustering => kmeans , hierarichal clustering
2. Dimensionality Reduction => To reduce no of dimensions/features.


1D ,2D,3D,nD => 10 features => 5features => 

Creates new features from existing features without loosing Data.

PCA => Principal Component Analysis.

columnTransformation

df["col"] = StandardScaler().fit_transfor(df["col"])
df["col"] = OneHotEncoder().fit_transfor(df["col"])


------------------------------------------------------------
variance
Covariance Matrix
EigenValue
EigenVector


"""


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ----------------------------------
# Step 1: Download historical prices
# ----------------------------------
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]

prices = yf.download(
    tickers,
    period="5y",
    interval="1d",
    auto_adjust=True,
    progress=False
)["Close"]

prices = prices.dropna()

print("Stock prices:")
print(prices.head())

# ----------------------------------
# Step 2: Calculate daily returns
# ----------------------------------
returns = prices.pct_change().dropna()

print("\nDaily returns:")
print(returns.head())

# ----------------------------------
# Step 3: Standardize returns
# ----------------------------------
scaler = StandardScaler()
returns_scaled = scaler.fit_transform(returns)

# ----------------------------------
# Step 4: Apply PCA
# ----------------------------------
pca = PCA()
principal_components = pca.fit_transform(returns_scaled)

# Explained variance
explained_variance = pca.explained_variance_ratio_

print("\nExplained variance ratio:")
print(pd.Series(
    explained_variance,
    index=[f"PC{i+1}" for i in range(len(tickers))]
).round(4))

print("\nCumulative explained variance:")
print(np.cumsum(explained_variance).round(4))

# ----------------------------------
# Step 5: Plot explained variance
# ----------------------------------
plt.figure(figsize=(8, 5))

plt.bar(
    range(1, len(tickers) + 1),
    explained_variance * 100,
    alpha=0.7,
    label="Individual variance"
)

plt.plot(
    range(1, len(tickers) + 1),
    np.cumsum(explained_variance) * 100,
    marker="o",
    color="red",
    label="Cumulative variance"
)

plt.xlabel("Principal Component")
plt.ylabel("Explained Variance (%)")
plt.title("PCA on Stock Market Returns")
plt.xticks(range(1, len(tickers) + 1))
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# ----------------------------------
# Step 6: Plot first two components
# ----------------------------------
pc_df = pd.DataFrame(
    principal_components[:, :2],
    index=returns.index,
    columns=["PC1", "PC2"]
)

plt.figure(figsize=(10, 5))
plt.scatter(
    pc_df["PC1"],
    pc_df["PC2"],
    alpha=0.35,
    s=12
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Stock Return Observations in PCA Space")
plt.grid(alpha=0.3)
plt.show()

# ----------------------------------
# Step 7: Examine component loadings
# ----------------------------------
loadings = pd.DataFrame(
    pca.components_.T,
    index=tickers,
    columns=[f"PC{i+1}" for i in range(len(tickers))]
)

print("\nPCA loadings:")
print(loadings.round(3))

plt.figure(figsize=(8, 5))
sns.heatmap(
    loadings.iloc[:, :3],
    annot=True,
    cmap="coolwarm",
    center=0
)
plt.title("Stock Loadings on First Three PCs")
plt.show()
