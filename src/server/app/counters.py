
user_table_max_transaction = 0
post_table_max_transaction = 0
userinfo_table_mac_transaction = 0

transaction_max = 0

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