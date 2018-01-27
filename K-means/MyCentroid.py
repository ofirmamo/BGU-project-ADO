from scipy.spatial import distance
from statistics import median, stdev
import logging


class Centroid:

    def __init__(self, centroid, data_set=None):
        self.centroid = centroid
        self.initialized = False
        self.median = None
        self.stdev = None
        if data_set is not None:
            self.initialize(data_set)

    def initialize(self, data_set):
        if self.initialized is False:
            total_distance = []
            for data_point in data_set:
                total_distance.append(distance.euclidean(self.centroid, data_point))

            self.median = median(total_distance)
            self.stdev = stdev(total_distance)
            self.initialized = True
        else:
            logging.warning('Centroid already initialized')

    def score(self, data_point):
        if self.initialized:
            distance_from_centroid = distance.euclidean(data_point, self.centroid)
            distance_from_median = abs(distance_from_centroid - self.median)
            return distance_from_median / self.stdev
        else:
            logging.warning('Model not yet initialized')
            return None
