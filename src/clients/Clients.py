import threading
import Client


def main():
    address = "http://127.0.0.1:5000"

    client = Client.Client()

    for i in range(3):

        th1 = threading.Thread(target=client.simple_client(address, 'normal' + str(i), 400))
        th1.start()

        th2 = threading.Thread(target=client.active_client(address, 'active' + str(i), 'a', 100, "The Post",
                                                           {'address': address, 'zip_code': "1234",
                                                            'full_name': "name surname", 'age': "20"}))
        th2.start()
        th3 = threading.Thread(target=client.random_user(address, 'random', 'r' + str(i), 200, "The Post",
                                                           {'address': address, 'zip_code': "1234",
                                                            'full_name': "name surname", 'age': "20"}))
        th3.start()


if __name__ == "__main__":
    main()

