import threading
import Client
import requests


def main():
    address = "http://127.0.0.1:5000"

    client = Client.Client()

    test_counts = 3

    num_messages = 100

    inject_count = 50

    # for i in range(3):

    for i in range(test_counts):
        # th1 = threading.Thread(target=client.simple_client(address, 'normal' + str(i), num_messages))
        th1 = threading.Thread(target=client.simple_client(address, 'normal', num_messages))
        th1.start()

        # th2 = threading.Thread(target=client.active_client(address, 'active' + str(i), 'a', num_messages, "The Post",
        #                                                    {'address': address, 'zip_code': "1234",
        #                                                     'full_name': "name surname", 'age': "20"}))

        th2 = threading.Thread(target=client.active_client(address, 'active', 'a', num_messages, "The Post",
                                                           {'address': address, 'zip_code': "1234",
                                                            'full_name': "name surname", 'age': "20"}))
        th2.start()
        # th3 = threading.Thread(target=client.random_user(address, 'random', 'r' + str(i), num_messages, "The Post",
        #                                                  {'address': address, 'zip_code': "1234",
        #                                                     'full_name': "name surname", 'age': "20"}))
        th3 = threading.Thread(target=client.random_user(address, 'random', 'r' , num_messages, "The Post",
                                                         {'address': address, 'zip_code': "1234",
                                                            'full_name': "name surname", 'age': "20"}))
        th3.start()

        th1.join()
        th2.join()
        th3.join()

        th4 = threading.Thread(target=client.error_inject(address, inject_count))
        th4.start()
        th4.join()

        requests.get('{}/reset_test'.format(address))

    requests.get("{}/stats".format(address))


if __name__ == "__main__":
    main()

