from typing import List

from sklearn.cluster import KMeans
import numpy as np

from kmeans.MyCentroid import Centroid


class MyKMeans:

    def __init__(self, threshold: int, n_cluster: int, data_set: list):
        self.threshold = threshold
        k_means_data = np.array(list(zip(data_set)))
        self.kmeans = KMeans(n_cluster)
        self.kmeans.fit(k_means_data)
        labels = self.kmeans.predict(k_means_data)
        centers = self.kmeans.cluster_centers_
        self.centroids: List[Centroid] = []

        for i, center in enumerate(centers):
            centroid = Centroid(center)
            data_set = (k_means_data[j] for j in range(len(k_means_data)) if labels[j] == i)
            centroid.initialize(data_set)
            self.centroids.append(centroid)

    def z_score(self, dot: int):
        dot_position = np.asarray([dot])
        scores = (centroid.score(dot_position) for centroid in self.centroids)
        return min(scores)

    def is_anomaly(self, dot: int):
        return self.z_score(dot) > self.threshold


