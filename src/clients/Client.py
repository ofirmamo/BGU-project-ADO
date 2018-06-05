import requests
import random


class Client:

    def simple_client(self, address, user: str='default', num_messages: int =100):
        current_user = user
        for i in range(num_messages):
            mail = current_user + '@ado.com'
            requests.post("{}/post-user".format(address), params={'username': current_user, 'email': mail})
            requests.get("{}/get-user".format(address), params={'username': current_user})
            requests.delete("{}/delete-user".format(address), params={'username': current_user})
            current_user = user + str(i)

    def active_client(self, address, user: str='active', tail: str='a',
                      num_messages: int =100, msg: str = "A great Post", post_info:  dict = {}):
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

    def random_user(self, address, user: str='random', tail: str='r', num_messages: int =100,
                    msg: str = "A great Post", post_info:  dict = {}):
        mail = user + '@ado.com'
        requests.post("{}/post-user".format(address), params={'username': user, 'email': mail})
        requests.post("{}/post-user-information".format(address), params={'username': user}.update(post_info))
        curr_msg = msg + ' ' + tail
        for i in range(num_messages):
            rand = random.randint(1, i+20)
            modrand = rand % 4
            if modrand == 0:
                requests.post("{}/post-post".format(address), params={'username': user, 'body': curr_msg})
            else:
                if modrand == 1:
                    requests.post("{}/change-user-information".format(address),
                                  params={'username': user}.update(post_info))
                    # requests.get("{}/get-post".format(address), params={'username': user})
            requests.get("{}/get-user-information".format(address), params={'username': user})

