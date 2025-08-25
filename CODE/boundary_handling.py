import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv("C:\\Users\\anjor\\Documents\\batch 888\\ANOMALITY PROJECT\\transactions_nigeria.csv")
X = data[['Amount', 'Time']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X_scaled)
data['Cluster'] = kmeans.labels_

distances = np.min(kmeans.transform(X_scaled), axis=1)
data['Distance'] = distances

cluster_distances = kmeans.transform(X_scaled)
sorted_indices = np.argsort(np.std(cluster_distances, axis=1))
boundary_txn = data.iloc[sorted_indices[0]]

print(f"\nTransaction ID: {boundary_txn['TransactionID']}")
print(f"Name: {boundary_txn['Name']}")
print(f"Cluster: {boundary_txn['Cluster']}")
print(f"Distance to Center: {boundary_txn['Distance']:.4f}")