from copy import deepcopy
from MyCentroid import Centroid
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing the dataset
data = pd.read_csv('xclara.csv')
# print("Input Data and Shape")
# print(data.shape)
# data.head()

plt.interactive(False)

# Getting the values and plotting it
f1 = data['V1'].values
# f2 = data['V2'].values
X = np.array(list(zip(f1)))
plt.scatter(f1, np.zeros_like(f1), c='black', s=7)

# plt.show()

# Euclidean Distance Caculator
# def dist(a, b, ax=1):
#     return np.linalg.norm(a - b, axis=ax)
#
# # Number of clusters
# k = 3
# # X coordinates of random centroids
# C_x = np.random.randint(0, np.max(X)-20, size=k)
# # Y coordinates of random centroids
# C_y = np.random.randint(0, np.max(X)-20, size=k)
# C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
# print("Initial Centroids")
# print(C)
#
# # Plotting along with the Centroids
# plt.scatter(f1, c='y', s=7)
# plt.scatter(C_x, marker='*', s=200, c='b')
#
# plt.show()
#
#
# # To store the value of centroids when it updates
# C_old = np.zeros(C.shape)
# # Cluster Lables(0, 1, 2)
# clusters = np.zeros(len(X))
# # Error func. - Distance between new centroids and old centroids
# error = dist(C, C_old, None)
# # Loop will run till the error becomes zero
# while error != 0:
#     # Assigning each value to its closest cluster
#     for i in range(len(X)):
#         distances = dist(X[i], C)
#         cluster = np.argmin(distances)
#         clusters[i] = cluster
#     # Storing the old centroid values
#     C_old = deepcopy(C)
#     # Finding the new centroids by taking the average value
#     for i in range(k):
#         points = [X[j] for j in range(len(X)) if clusters[j] == i]
#         C[i] = np.mean(points, axis=0)
#     error = dist(C, C_old, None)
#
# colors = ['r', 'g', 'b', 'y', 'c', 'm']
# fig, ax = plt.subplots()
# for i in range(k):
#         points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
#         ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
# ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')
# plt.show()


'''
==========================================================
scikit-learn
==========================================================
'''

from sklearn.cluster import KMeans

# Number of clusters
n_clusters = 3

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
ax.scatter(anomalies[:, 0], np.zeros_like(anomalies), marker='v', s=10, c='r')

plt.scatter(centers, np.zeros_like(centers), marker='*', s=200, c='black')

plt.show()

# Comparing with scikit-learn centroids
# print("Centroid values")
# print("Scratch")
# print(C) # From Scratch
# print(centers) # From sci-kit learn