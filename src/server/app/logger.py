import logging
import sys
from app.logsmanager.LogsManager import LogsManager


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# adding filter
log_manager = LogsManager()
logger.addFilter(log_manager)

# create the log file or clean it
f = open('./app/logs/Transactions.log', 'w')
f.close()

# create file handler
handler = logging.FileHandler('./app/logs/Transactions.log')
handler.setLevel(logging.INFO)

# create stdout handler
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)

# add handler to the logger
logger.addHandler(handler)
logger.addHandler(stdout_handler)