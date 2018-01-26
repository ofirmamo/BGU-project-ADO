from scipy.spatial import distance
from statistics import median, stdev


class Centroid:

    def __init__(self, centroid, data_set):
        self.centroid = centroid
        total_distance = []
        for data_point in data_set:
            total_distance.append(distance.euclidean(centroid, data_point))

        self.median = median(total_distance)
        self.stdev = stdev(total_distance)

    def score(self, data_point):
        distance_from_centroid = distance.euclidean(data_point, self.centroid)
        distance_from_median = abs(distance_from_centroid - self.median)
        return distance_from_median / self.stdev
