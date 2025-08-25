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

distances = np.min(kmeans.transform(X_scaled), axis=1)

threshold = np.percentile(distances, 95)
print(f"Anomaly threshold (95th percentile distance): {threshold:.4f}\n")
