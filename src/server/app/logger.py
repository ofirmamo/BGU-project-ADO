import logging
import sys
from app.logsmanager.LogsManager import LogsManager


flask_logger = logging.getLogger('werkzeug')
flask_logger.setLevel(logging.ERROR)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

user_logger = logging.getLogger("user.logger")
user_logger.setLevel(logging.INFO)

post_logger = logging.getLogger('posts.logger')
post_logger.setLevel(logging.INFO)

user_information_logger = logging.getLogger('user_information.logger')
user_information_logger.setLevel(logging.INFO)

# adding filter
log_manager = LogsManager()
logger.addFilter(log_manager)

#adding user_logger filter
log_manager_user = LogsManager()
user_logger.addFilter(log_manager_user)

#adding posts logger filter
log_manager_posts = LogsManager()
post_logger.addFilter(log_manager_posts)

#adding user_information logger filter
log_manager_userinfo = LogsManager()
user_information_logger.addFilter(log_manager_userinfo)

# create the log file or clean it
f = open('./app/logs/Transactions.log', 'w')
f.close()

f = open('./app/logs/user_logs.log', 'w')
f.close()

f = open('./app/logs/posts_logs.log', 'w')
f.close()

f = open('./app/logs/userinfo_logs.log', 'w')

# create file handler
handler = logging.FileHandler('./app/logs/Transactions.log')
handler.setLevel(logging.INFO)

user_handler = logging.FileHandler('./app/logs/user_logs.log')
user_handler.setLevel(logging.INFO)

posts_handler = logging.FileHandler('./app/logs/posts_logs.log')
posts_handler.setLevel(logging.INFO)

userinfo_handler = logging.FileHandler('./app/logs/userinfo_logs.log')
userinfo_handler.setLevel(logging.INFO)

# create stdout handler
# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
user_handler.setFormatter(formatter)
posts_handler.setFormatter(formatter)
userinfo_handler.setFormatter(formatter)
# stdout_handler.setFormatter(formatter)

# add handler to the logger
logger.addHandler(handler)
# logger.addHandler(stdout_handler)

user_logger.addHandler(user_handler)
post_logger.addHandler(posts_handler)
user_information_logger.addHandler(userinfo_handler)
