import threading
import Client


def main():
    address = "http://127.0.0.1:5000"

    client = Client.Client()

    for i in range(3):

        th1 = threading.Thread(target=client.simple_client(address, 'normal' + str(i), 400))
        th1.start()
        th1.join()

        th2 = threading.Thread(target=client.active_client(address, 'active' + str(i), 'a', 400, "The Post",
                                                           {'address': address, 'zip_code': "1234",
                                                            'full_name': "name surname", 'age': "20"}))
        th2.start()
        th2.join()
        th3 = threading.Thread(target=client.random_user(address, 'random', 'r' + str(i), 400, "The Post",
                                                         {'address': address, 'zip_code': "1234",
                                                            'full_name': "name surname", 'age': "20"}))
        th3.start()
        th3.join()

    th4 = threading.Thread(target=client.error_inject(address, 100))

if __name__ == "__main__":
    main()

