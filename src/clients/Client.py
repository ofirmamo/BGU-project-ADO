import requests
import random

loop_count = 3

class Client:

    # real number of messages - num_mes * 3
    def simple_client(self, address, user: str = 'default', num_messages: int = 100):
        current_user = user
        for i in range(loop_count):
            current_user += str(i)
            for j in range(num_messages):
                mail = current_user + '@ado.com'
                requests.post("{}/post-user".format(address), params={'username': current_user, 'email': mail})
                requests.get("{}/get-user".format(address), params={'username': current_user})
                requests.delete("{}/delete-user".format(address), params={'username': current_user})
                current_user += str(j)

    # real number of messages - num_mes * 3 + num_mes/5 + 3
    def active_client(self, address, user: str = 'active', tail: str = 'a',
                      num_messages: int = 100, msg: str = "A great Post", post_info: dict = {}):
        for j in range(loop_count):
            user += str(j)
            mail = user + '@ado.com'
            curr_msg = msg + tail
            requests.post("{}/post-user".format(address), params={'username': user, 'email': mail})
            requests.post("{}/post-user-information".format(address), params={'username': user}.update(post_info))
            for i in range(num_messages):
                requests.post("{}/post-post".format(address), params={'username': user, 'body': curr_msg})
                requests.post("{}/change-user-information".format(address), params={'username': user}.update(post_info))
                requests.get("{}/get-user".format(address), params={'username': user})
                curr_msg = msg + str(i)
                if i % 5 == 0:
                    requests.get("{}/get-user-information".format(address), params={'username': user})

            requests.delete("{}/delete-user".format(address), params={'username': user})

    # eal number of messages ~ num_mes * 1.5 + 2
    def random_user(self, address, user: str = 'random', tail: str = 'r', num_messages: int = 100,
                    msg: str = "A great Post", post_info: dict = {}):
        for j in range(loop_count):
            user += str(j)
            mail = user + '@ado.com'
            requests.post("{}/post-user".format(address), params={'username': user, 'email': mail})
            requests.post("{}/post-user-information".format(address), params={'username': user}.update(post_info))
            curr_msg = msg + ' ' + tail
            for i in range(num_messages):
                rand = random.randint(1, i + 20)
                modrand = rand % 4
                if modrand == 0:
                    requests.post("{}/post-post".format(address), params={'username': user, 'body': curr_msg})
                else:
                    if modrand == 1:
                        requests.post("{}/change-user-information".format(address),
                                      params={'username': user}.update(post_info))
                        requests.get("{}/get-post".format(address), params={'username': user})
                requests.get("{}/get-user-information".format(address), params={'username': user})

    def error_inject(self, address, num_messages: int = 100):
        for i in range(num_messages):
            requests.get("{}/inject".format(address))
