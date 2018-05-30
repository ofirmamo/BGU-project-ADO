from pyaml import yaml

from app.kmeans.MyKMeans import MyKMeans
from app.logger import logger


class LogsManager:

    def __init__(self, configuration: str = '../../resources/configuration.yml', verbose: bool = False):
        with open(configuration, 'r') as config_file:
            config = yaml.load(config_file)
            self.n_logs_to_init = config['n_logs_to_init']
            self.n_cluster = config['n_clusters']
            self.threshold = config['threshold']

        self.data_set = []
        self.initialized = False
        self.kmeans: MyKMeans = None
        self.verbose = verbose

    def manage(self, value: int) -> bool:
        if self.initialized:
            ans = self.kmeans.is_anomaly(value)
            if ans:
                logger.info('Initialized and is anomaly')
            else:
                logger.info('Initialized and is not an anomaly')
            return ans
        else:
            self.data_set.append(value)
            if len(self.data_set) == self.n_logs_to_init:
                logger.info('initializing model')
                self.kmeans = MyKMeans(threshold=self.threshold, n_cluster=self.n_cluster, data_set=self.data_set)
                self.initialized = True
            return True
