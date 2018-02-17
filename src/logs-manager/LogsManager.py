from pyaml import yaml

from parsing.Parser import Parser

from kmeans.MyKMeans import MyKMeans


class LogsManager:

    def __init__(self, configuration='../../resources/configuration.yml'):
        with open(configuration, 'r') as config_file:
            config = yaml.load(config_file)
            self.n_logs_to_init = config['n_logs_to_init']
            self.n_cluster = config['n_clusters']
            self.threshold = config['threshold']

        self.parser = Parser()
        self.data_set = []
        self.initialized = False
        self.kmeans: MyKMeans = None
        # todo - Add logger which actually writes the logs
        # self.logger =


    def manage(self, log: str):
        value = self.parser.parse_log(log)
        if self.initialized:
             isAnomaly = self.kmeans.is_anomaly(value)
             if isAnomaly:
                 print(value)
        else:
             self.data_set.append(value)
            # self.logger.log(log)
        if len(self.data_set) == self.n_logs_to_init:
            self.initialized = True
            self.kmeans = MyKMeans(threshold=self.threshold, n_cluster=self.n_cluster, data_set=self.data_set)


