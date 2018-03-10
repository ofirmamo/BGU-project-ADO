import requests


class Client:

    def client_requests(self, address ,init_user: str='defult', tail: str='a', num_messages: int =100):
        current_user = init_user
        for i in range (num_messages):
            requests.get("{}/get".format(address), params = {'username':'ADO'})
            mail = current_user + '@ado.com'
            requests.post("{}/post".format(address), data={'username': 'current_user', 'email': mail})
            requests.delete("{}/delete".format(address), data={'username': current_user})
            current_user = current_user + tail

    '''
    def get_request(self, address: str, num_messages: int = 10):
        for i in range(num_messages):
            requests.get("{}/get".format(address), params={'username': 'Ofir'})


    def post_request(self, address, init_user, num_messages: int = 10):
        current_user = init_user
        for i in range(num_messages):
            mail = current_user + '@ado.com'
            requests.post("{}/post".format(address), params={'username': 'Ofir', 'email': 'a'})
            current_user = current_user + 'a'

    def delete_request(self, address, init_user, num_messages: int = 10):
        current_user = init_user
        for i in range(num_messages):
            mail = current_user + '@ado.com'
            requests.delete("{}/delete".format(address), params={'username': 'Ofir'})
            current_user = current_user + 'a'
    '''
