import logging
import sys
from app.logsmanager.LogsManager import LogsManager


flask_logger = logging.getLogger('werkzeug')
flask_logger.setLevel(logging.ERROR)

logger = logging.getLogger(__name__)
user_logger = logging.getLogger("user.logger")
post_logger = logging.getLogger('posts.logger')
user_information_logger = logging.getLogger('user_information.logger')

# Creating managers filters
log_manager = LogsManager()
log_manager_user = LogsManager()
log_manager_posts = LogsManager()
log_manager_userinfo = LogsManager()


# specifying log files
files = ['./app/logs/Transactions.log',
         './app/logs/user_logs.log',
         './app/logs/posts_logs.log',
         './app/logs/userinfo_logs.log'
         ]

# Creating/Cleaning log files
for path in files:
    f = open(path, 'w')
    f.close()


# create file handlers
handler = logging.FileHandler('./app/logs/Transactions.log')
user_handler = logging.FileHandler('./app/logs/user_logs.log')
posts_handler = logging.FileHandler('./app/logs/posts_logs.log')
userinfo_handler = logging.FileHandler('./app/logs/userinfo_logs.log')

# create stdout handler
# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setLevel(logging.INFO)


loggers: dict = {'logger': logger,
                 'user_logger': user_logger,
                 'post_logger': post_logger,
                 'user_information_logger': user_information_logger
                 }

log_managers: dict = {'logger_manager': log_manager,
                      'user_logger_manager': log_manager_user,
                      'post_logger_manager': log_manager_posts,
                      'user_information_logger_manager': log_manager_userinfo
                      }

handlers: dict = {'logger_handler': handler,
                  'user_logger_handler': user_handler,
                  'post_logger_handler': posts_handler,
                  'user_information_logger_handler': userinfo_handler}

# create a logging format
formatter = logging.Formatter('%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')

# initializing all loggers
for key, specific_logger in loggers.items():
    specific_logger.setLevel(logging.INFO)
    # adding the correct file handler
    handler = handlers['{}_handler'.format(key)]
    handler.setLevel(logging.INFO)
    specific_logger.addHandler(handler)
    # adding the correct filter
    specific_logger.addFilter(log_managers['{}_manager'.format(key)])