from copy import deepcopy
from MyCentroid import Centroid
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing the dataset
data = pd.read_csv('xclara.csv')
print("Input Data and Shape")
print(data.shape)
data.head()

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
# Centroid values
centroids = kmeans.cluster_centers_

print(centroids)

my_centroids: [Centroid] = []

for i, centroid in enumerate(centroids):
    data_set = []
    for j, label in enumerate(labels):
        if label == i:
            data_set.append(X[j])
    my_centroids.append(Centroid(centroid=centroid, data_set=data_set))

for my_centroid in my_centroids:
    for data_point in X:
        print(my_centroid.score(data_point))


plt.scatter(centroids, np.zeros_like(centroids), marker='*', s=200, c='y')

plt.show()

# Comparing with scikit-learn centroids
# print("Centroid values")
# print("Scratch")
# print(C) # From Scratch
print("sklearn")
print(centroids) # From sci-kit learn