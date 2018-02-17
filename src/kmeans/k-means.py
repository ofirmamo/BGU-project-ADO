from copy import deepcopy
from MyCentroid import Centroid
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing the dataset
# data = pd.read_csv('xclara.csv')
# print("Input Data and Shape")
# print(data.shape)
# data.head()

plt.interactive(False)

# Getting the values and plotting it
# f1 = data['V1'].values
# f2 = data['V2'].values
f1 = list(range(0, 10000))
f1.append(15000)
X = np.array(list(zip(f1)))
plt.scatter(f1, np.zeros_like(f1), c='black', s=7)

plt.show()

'''
==========================================================
scikit-learn
==========================================================
'''

from sklearn.cluster import KMeans

# Number of clusters
n_clusters = 2

kmeans = KMeans(n_clusters)

# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Getting each data point score
scores = []
# Centers values
centers = kmeans.cluster_centers_
# Centroids in the same order as centers
my_centroids: [Centroid] = []

# Associate each data point to its closest centroid
for i, center in enumerate(centers):
    centroid = Centroid(center)
    data_set = (X[j] for j in range(len(X)) if labels[j] == i)
    centroid.initialize(data_set)
    my_centroids.append(centroid)

# Associate each data point with its score
for i, data_point in enumerate(X):
    label = labels[i]
    center = my_centroids[label]
    score = center.score(data_point)
    scores.append(score)


colors = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

# plot each cluster with its unique color
fig, ax = plt.subplots()
for i in range(n_clusters):
        points = np.array([X[j] for j in range(len(X)) if labels[j] == i])
        ax.scatter(points[:, 0], np.zeros_like(points), s=7, c=colors[i])

# plot anomalies in red
anomalies = np.array([X[i] for i in range(len(X)) if scores[i] > 3])
ax.scatter(anomalies[:], np.zeros_like(anomalies), marker='v', s=10, c='r')

plt.scatter(centers, np.zeros_like(centers), marker='*', s=200, c='black')

plt.show()

# Comparing with scikit-learn centroids
# print("Centroid values")
# print("Scratch")
# print(C) # From Scratch
# print(centers) # From sci-kit learn