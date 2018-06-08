import functools
import logging
import threading
from typing import List

from pyaml import yaml

from app.kmeans.MyKMeans import MyKMeans

from app.kmeans.MyCentroid import Centroid


def synchronized(wrapped):
    lock = threading.Lock()

    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)

    return _wrap


class LogsManager(logging.Filter):

    def __init__(self, configuration: str = './app/resources/configuration.yml'):
        super().__init__()
        with open(configuration, 'r') as config_file:
            config = yaml.load(config_file)
            self.n_logs_to_init = config['n_logs_to_init']
            self.n_cluster = config['n_clusters']
            self.threshold = config['threshold']

        self.data_set = []
        self.initialized: bool = False
        self.kmeans: MyKMeans = None
        self.stats: List[(float, float, float)] = None

    @synchronized
    def filter(self, record: str) -> bool:
        try:
            msg = record.msg
            list_of_words = msg.split()
            value = list_of_words[list_of_words.index('time:') + 1]
            value = int(value)

            if self.initialized:
                ans = self.kmeans.is_anomaly(value)
                if ans:
                    record.msg = '{} - k-means says it anomaly'.format(record.msg)
                return ans
            else:
                self.data_set.append(value)
                if len(self.data_set) == self.n_logs_to_init:
                    self.kmeans = MyKMeans(threshold=self.threshold, n_cluster=self.n_cluster, data_set=self.data_set)
                    centroids: List[Centroid] = self.kmeans.centroids
                    self.stats = [(centroid.mean, centroid.stdev, self.threshold) for centroid in centroids]
                    self.initialized = True
                record.msg = '{} - k-means not yet initialized'.format(record.msg)
                return True

        except ValueError as e:
            return False

    def display(self):
        return self.kmeans.display()
