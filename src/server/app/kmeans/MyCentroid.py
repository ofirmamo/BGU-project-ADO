from scipy.spatial import distance
from statistics import mean, stdev
import logging

epsilon: float = 0.001


class Centroid:

    def __init__(self, centroid, data_set=None):
        self.centroid = centroid
        self.initialized = False
        self.mean = None
        self.stdev = None
        if data_set is not None:
            self.initialize(data_set)

    def initialize(self, data_set):
        if self.initialized is False:
            total_distance = []
            for data_point in data_set:
                total_distance.append(distance.euclidean(self.centroid, data_point))

            self.mean = mean(total_distance)
            self.stdev = stdev(total_distance, self.mean)
            if self.stdev == 0:
                self.stdev = epsilon
            logging.info('mean ={}, stdev = {}', self.mean, self.stdev)
            self.initialized = True
        else:
            logging.warning(msg='Centroid already initialized')

    def score(self, data_point):
        if self.initialized:
            distance_from_centroid = distance.euclidean(data_point, self.centroid)

            distance_from_mean = abs(distance_from_centroid - self.mean)
            return distance_from_mean / self.stdev
        else:
            logging.warning(msg='Centroid not yet initialized')
            return None
