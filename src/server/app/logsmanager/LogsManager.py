import functools
import logging
import threading
from typing import List

from pyaml import yaml

from app.kmeans.MyKMeans import MyKMeans
from .counters import Counters
from app.kmeans.MyCentroid import Centroid


def synchronized(method):
    outer_lock = threading.Lock()
    lock_name = "__" + method.__name__ + "_lock" + "__"

    @functools.wraps(method)
    def sync_method(self, *args, **kws):
        with outer_lock:
            if not hasattr(self, lock_name): setattr(self, lock_name, threading.Lock())
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)

    return sync_method


class LogsManager(logging.Filter):

    def __init__(self, configuration: str = './app/resources/configuration.yml'):
        super().__init__()
        with open(configuration, 'r') as config_file:
            config = yaml.load(config_file)
            self.n_logs_to_init: int = config['n_logs_to_init']
            self.n_cluster: int = config['n_clusters']
            self.threshold: float = config['threshold']

        self.data_set = []
        self.initialized: bool = False
        self.kmeans: MyKMeans = None
        self.stats: List[(float, float, float)] = None
        self.counters: Counters = Counters()
        self.values_table = []

    @synchronized
    def filter(self, record: str) -> bool:
        try:
            msg = record.msg

            injected = 'injected' in msg

            if injected:
                self.counters.injected_trans += 1

            self.counters.total_transaction += 1

            list_of_words = msg.split()
            value = list_of_words[list_of_words.index('time:') + 1]
            value = int(value)
            if self.initialized:
                ans = self.kmeans.is_anomaly(value)
                if ans:
                    if injected:
                        self.counters.injected_caught += 1
                    else:
                        self.counters.falsely_caught += 1
                    record.msg = '{} - k-means says it anomaly'.format(record.msg)
                return ans
            else:
                self.data_set.append(value)
                if self.n_logs_to_init <= len(self.data_set):
                    print('Initializing k-means')
                    self._init_k_means()
                    self.data_set.clear()
                record.msg = '{} - k-means not yet initialized'.format(record.msg)
                return True

        except ValueError as e:
            return False

    @synchronized
    def reset(self):
        record = [self.counters.total_transaction,
                  self.n_logs_to_init,
                  self.threshold,
                  self.counters.total_transaction - self.n_logs_to_init,
                  self.n_logs_to_init + self.counters.injected_caught + self.counters.falsely_caught,
                  self.counters.injected_caught + self.counters.falsely_caught,
                  self.counters.injected_trans,
                  self.counters.injected_caught,
                  self.counters.falsely_caught,
                  self.counters.total_transaction / float(self.n_logs_to_init + self.counters.injected_caught + self.counters.falsely_caught),
                  (self.counters.total_transaction - self.n_logs_to_init) / float(self.counters.injected_caught + self.counters.falsely_caught + 1)]
        self.values_table.append(record)
        self.initialized = False
        self.kmeans = None
        self.counters.clear()

    def _init_k_means(self):
        self.kmeans = MyKMeans(threshold=self.threshold, n_cluster=self.n_cluster, data_set=self.data_set)
        centroids: List[Centroid] = self.kmeans.centroids
        self.stats = [(centroid.mean, centroid.stdev, self.threshold) for centroid in centroids]
        self.initialized = True
        self.data_set.clear()

    @synchronized
    def set_configurations(self, threshold: float, n_logs_to_init: int):
        self.threshold = threshold
        self.n_logs_to_init = n_logs_to_init
        # print(self.n_logs_to_init, self.threshold, type(self.n_logs_to_init), type(self.threshold))

    def get_total_transaction(self):
        return self.counters.total_transaction

    def display(self):
        if not self.initialized:
            return 'K-means not yet initialized'
        else:
            return self.kmeans.display()
