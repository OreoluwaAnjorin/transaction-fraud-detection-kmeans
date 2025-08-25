import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:\\Users\\anjor\\Documents\\batch 888\\ANOMALITY PROJECT\\transactions_nigeria.csv")
print(f"Dataset shape: {data.shape}")
print("\nFirst few rows:")
print(data.head())

X = data[['Amount', 'Time']]
print(f"\nFeature statistics:")
print(X.describe())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X_scaled)

data['Cluster'] = kmeans.labels_
distances = np.min(kmeans.transform(X_scaled), axis=1)
data['Distance_to_Center'] = distances

threshold = np.percentile(distances, 95)
print(f"\nAnomaly threshold (95th percentile): {threshold:.4f}")

# Flag anomalies
data['Is_Anomaly'] = distances > threshold

anomaly_count = data['Is_Anomaly'].sum()
anomaly_percentage = (anomaly_count / len(data)) * 100

print(f"\nAnomaly Detection Results:")
print(f"Total transactions: {len(data)}")
print(f"Anomalies detected: {anomaly_count}")
print(f"Anomaly rate: {anomaly_percentage:.2f}%")

print(f"\nDetailed Anomaly Report:")
anomalies = data[data['Is_Anomaly']].sort_values('Distance_to_Center', ascending=False)

for idx, row in anomalies.iterrows():
    print(f"Transaction ID: {row['TransactionID']}")
    print(f"Name: {row['Name']}")
    print(f"Amount: ₦{row['Amount']:.2f}")
    print(f"Time: {row['Time']:.2f}")
    print(f"Cluster: {row['Cluster']}")
    print(f"Distance to Center: {row['Distance_to_Center']:.4f}")
    print(f"Anomaly Score: {(row['Distance_to_Center']/threshold)*100:.1f}% of threshold")

# Cluster analysis
print(f"\nCluster Analysis:")
cluster_summary = data.groupby('Cluster').agg({
    'Amount': ['count', 'mean', 'std', 'min', 'max'],
    'Time': ['mean', 'std', 'min', 'max'],
    'Is_Anomaly': 'sum'
}).round(2)

cluster_summary.columns = ['Count', 'Avg_Amount', 'Std_Amount', 'Min_Amount', 'Max_Amount',
                          'Avg_Time', 'Std_Time', 'Min_Time', 'Max_Time', 'Anomalies']
print(cluster_summary)

print(f"\nKey Insights:")

most_anomalous = data.loc[data['Distance_to_Center'].idxmax()]
print(f"Most anomalous transaction: ID {most_anomalous['TransactionID']} by {most_anomalous['Name']}")
print(f"  Amount: ₦{most_anomalous['Amount']:.2f}, Time: {most_anomalous['Time']:.2f}")
print(f"  Distance score: {most_anomalous['Distance_to_Center']:.4f}")


anomaly_by_cluster = data[data['Is_Anomaly']].groupby('Cluster').size()
if len(anomaly_by_cluster) > 0:
    cluster_with_most_anomalies = anomaly_by_cluster.idxmax()
    print(f"Cluster with most anomalies: Cluster {cluster_with_most_anomalies} ({anomaly_by_cluster[cluster_with_most_anomalies]} anomalies)")

print(f"\nAnomaly Pattern Analysis:")
if anomaly_count > 0:
    avg_anomaly_amount = anomalies['Amount'].mean()
    avg_normal_amount = data[~data['Is_Anomaly']]['Amount'].mean()
    avg_anomaly_time = anomalies['Time'].mean()
    avg_normal_time = data[~data['Is_Anomaly']]['Time'].mean()
    
    print(f"Average anomalous transaction amount: ₦{avg_anomaly_amount:.2f}")
    print(f"Average normal transaction amount: ₦{avg_normal_amount:.2f}")
    print(f"Anomalies are {avg_anomaly_amount/avg_normal_amount:.2f}x the average normal amount")
    
    print(f"\nAverage anomalous transaction time: {avg_anomaly_time:.2f}")
    print(f"Average normal transaction time: {avg_normal_time:.2f}")
    
    # Extra Check if anomalies tend to be high-value transactions
    high_amount_anomalies = (anomalies['Amount'] > data['Amount'].quantile(0.9)).sum()
    print(f"Anomalies in top 10% of transaction amounts: {high_amount_anomalies}/{anomaly_count}")