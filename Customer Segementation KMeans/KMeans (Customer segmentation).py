import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the Data:
data = pd.read_csv('customer_data.csv')

# Feature Engineering:
# Assuming these features might be relevant for customer segmentation
features = ['age', 'income', 'spending']
X = data[features]  # Select the chosen features

# Create a K-Means Model:
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the Model:
kmeans.fit(X)

# Get Cluster Labels:
labels = kmeans.labels_

# Evaluate the Model:
silhouette_avg = silhouette_score(X, labels)
print("Silhouette score:", silhouette_avg)

# Analyze the characteristics of each cluster
cluster_0 = data[labels == 0]
cluster_1 = data[labels == 1]
cluster_2 = data[labels == 2]

# Visualize the clusters (e.g., using scatter plots)
# ... (add your visualization code here)
