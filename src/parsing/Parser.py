import json
import logging


class Parser:

    @staticmethod
    def parse_log(json_string):
        log = json.loads(json_string)
        total = log['time']
        return total

    @staticmethod
    def parse_file(output_filename):
        total_times = []
        # Open output file in 'append' mode
        with open(output_filename, "r") as in_file:
            # Loop over each log line
            for line in in_file:
                log = json.loads(line)
                total_times.append(log['time'])
        return total_times


# dictionary: dict = {'hi': 50, 'bye': 60}
#
# logger = logging.getLogger()
#
# logHandler = logging.StreamHandler()
# logHandler.setFormatter()