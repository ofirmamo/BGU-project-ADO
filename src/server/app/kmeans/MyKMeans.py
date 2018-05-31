from typing import List

from flask import make_response
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from io import BytesIO

from .MyCentroid import Centroid


class MyKMeans:

    def __init__(self, threshold: float, n_cluster: int, data_set: list):
        self.threshold = threshold
        self.data_set = data_set
        k_means_data = np.array(list(zip(data_set)))
        self.kmeans = KMeans(n_cluster)
        self.kmeans.fit(k_means_data)
        self.labels = self.kmeans.predict(k_means_data)
        self.centers = self.kmeans.cluster_centers_
        self.centroids: List[Centroid] = []
        self.anomalies = []

        for i, center in enumerate(self.centers):
            centroid = Centroid(center)
            data_set = (k_means_data[j] for j in range(len(k_means_data)) if self.labels[j] == i)
            centroid.initialize(data_set)
            self.centroids.append(centroid)

    def z_score(self, dot: int):
        dot_position = np.asarray([dot])
        scores = (centroid.score(dot_position) for centroid in self.centroids)
        return min(scores)

    def is_anomaly(self, dot: int):
        ans = self.z_score(dot) > self.threshold
        if ans:
            self.anomalies.append(dot)
        return ans

    def display(self):
        plt.rcParams['figure.figsize'] = (16, 9)

        X = np.asarray(list(zip(self.data_set)))

        colors = ['C4', 'C5', 'C6', 'C7', 'C8']

        fig = Figure()
        ax = fig.add_subplot(111)
        for i in range(len(self.centers)):
            points = np.array([X[j] for j in range(len(X)) if self.labels[j] == i])
            ax.scatter(points[:, 0], np.zeros_like(points), s=7, c=colors[i])
        ax.scatter(self.anomalies[:], np.zeros_like(self.anomalies), marker='v', s=10, c='r')
        plt.scatter(self.centers, np.zeros_like(self.centers), marker='*', s=200, c='black')

        canvas = FigureCanvas(fig)
        png_output = BytesIO()
        canvas.print_png(png_output)
        canvas.print_png(png_output)
        response = make_response(png_output.getvalue())
        response.headers['Content-Type'] = 'image/png'
        return response

def main():
    data_set = list(range(0, 10000))
    data_set.append(15000)
    my_kmeans = MyKMeans(threshold=3.5, n_cluster=3, data_set=data_set)
    my_kmeans.display()


if __name__ == '__main__':
    main()
