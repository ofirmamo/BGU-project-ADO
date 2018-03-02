import requests


class Client:

    def get_request(self, address):
        i = 0
        while i < 100:
            requests.get(address)
            i += 1
            print('got')

    def post_request(self, address, init_user):
        current_user = init_user
        i = 0
        while i < 100:
            mail = current_user + '@ado.com'
            requests.post(address, data={current_user, mail})
            current_user = current_user + current_user
            i += 1
            print('posted')

    def delete_request(self, address, init_user):
        current_user = init_user
        i = 0
        while i < 100:
            mail = current_user + '@ado.com'
            requests.delete(address, data={current_user, mail})
            current_user = current_user + current_user
            i += 1
            print('posted')
