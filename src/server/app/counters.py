import random
from app.logger import log_manager, log_manager_user, log_manager_posts, log_manager_userinfo
import pandas as pd

user_table_max_transaction = 0
post_table_max_transaction = 0
userinfo_table_mac_transaction = 0

transaction_max = 0

def build_df_server():
    server_csv = open('./app/resources/server.csv', 'a+')
    raw_data = {'total_transactions': [log_manager.get_total_transaction()]}
    df = pd.DataFrame(raw_data, columns=['total_transactions'])
    df.to_csv(server_csv, header=False)
    server_csv.close()

def build_df_user():
    user_csv = open('./app/resources/user.csv', 'a+')
    raw_data = {'total_transactions': [log_manager_user.get_total_transaction()]}
    df = pd.DataFrame(raw_data, columns=['total_transactions'])
    df.to_csv(user_csv, header=False)
    user_csv.close()

def build_df_posts():
    posts_csv = open('./app/resources/posts.csv', 'a+')
    raw_data = {'total_transactions': [log_manager_posts.get_total_transaction()]}
    df = pd.DataFrame(raw_data, columns=['total_transactions'])
    df.to_csv(posts_csv, header=False)
    posts_csv.close()

def build_df_userinfo():
    userinfo_csv = open('./app/resources/userinfo.csv', 'a+')
    raw_data = {'total_transactions': [log_manager_userinfo.get_total_transaction()]}
    df = pd.DataFrame(raw_data, columns=['total_transactions'])
    df.to_csv(userinfo_csv, header=False)
    userinfo_csv.close()

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
        return round(random.choice([dec, inc]) + 1)
