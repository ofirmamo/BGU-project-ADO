import random
from app.logger import log_manager, log_manager_user, log_manager_posts, log_manager_userinfo
import pandas as pd

user_table_max_transaction = 0
post_table_max_transaction = 0
userinfo_table_mac_transaction = 0

transaction_max = 0

labels = ['total transactions',
          'num_logs_to_init',
          'threshold',
          'total transactions after initialization',
          'total saved logs',
          'total saved logs after initialization',
          'total injected',
          'injected caught',
          'falsely caught',
          'ratio',
          'ratio after initialization']

def write_to_csv(file, values):
    df = pd.DataFrame.from_records(values, columns=labels)
    print(df)
    sorted_df = df.sort_values(['num_logs_to_init', 'threshold', 'total injected'])
    sorted_df.to_csv(file, index=False)
    file.close()

def build_df_server():
    server_csv = open('./app/data/server.csv', 'w')
    values = log_manager.values_table
    write_to_csv(server_csv, values)


def build_df_user():
    user_csv = open('./app/data/user.csv', 'w')
    values = log_manager_user.values_table
    write_to_csv(user_csv, values)

def build_df_posts():
    posts_csv = open('./app/data/posts.csv', 'w')
    values = log_manager_posts.values_table
    write_to_csv(posts_csv, values)


def build_df_userinfo():
    userinfo_csv = open('./app/data/userinfo.csv', 'w')
    values = log_manager_userinfo.values_table
    write_to_csv(userinfo_csv, values)


def append_csv():
    build_df_server()
    build_df_user()
    build_df_posts()
    build_df_userinfo()

def update_user_max(curr_time):
    global user_table_max_transaction
    if curr_time > user_table_max_transaction:
        user_table_max_transaction = curr_time
    return

def update_post_max(curr_time):
    global post_table_max_transaction
    if curr_time > post_table_max_transaction:
        post_table_max_transaction = curr_time
        return

def update_userinfo_max(curr_time):
    global userinfo_table_mac_transaction
    if curr_time > userinfo_table_mac_transaction:
        userinfo_table_mac_transaction = curr_time
    return

def update_max(curr_time):
    global transaction_max
    if curr_time > transaction_max:
        transaction_max = curr_time


epsilon: float = 2
noise: int = 1
dictionary: dict = {'manager': log_manager,
                    'user': log_manager_user,
                    'post': log_manager_posts,
                    'userinfo': log_manager_userinfo
                    }


def get_total_time(component_type: str):
    manager = dictionary[component_type]
    stats = manager.stats
    if stats is None:
        return 0
    mean, stdev, threshold = random.choice(stats)
    dec, inc = mean - (threshold * stdev + epsilon), mean + (threshold * stdev + epsilon)
    if dec < 0:
        return round(inc + 1)
    else:
        return round(random.choice([dec - 1, inc + 1]))
