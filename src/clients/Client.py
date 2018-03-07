import requests


class Client:

    def get_request(self, address: str):
        i = 0
        while i < 1:
            requests.get("{}/get".format(address), params={'username': 'Ofir'})
            i += 1

    def post_request(self, address, init_user):
        current_user = init_user
        i = 0
        while i < 1:
            mail = current_user + '@ado.com'
            requests.post("{}/post".format(address), params={'username': 'Ofir', 'email': 'a'})
            current_user = current_user + 'a'
            i += 1
            print('posted')

    def delete_request(self, address, init_user):
        current_user = init_user
        i = 0
        while i < 1:
            mail = current_user + '@ado.com'
            requests.delete("{}/delete".format(address), params={'username': 'Ofir'})
            current_user = current_user + 'a'
            i += 1
            print('deleted')
