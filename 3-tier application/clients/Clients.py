import requests
import threading
import Client


def main():
    address = "http://127.0.0.1:5000"

    client = Client.Client()
    t1 = threading.Thread(target=client.get_request(address))
    t2 = threading.Thread(target=client.post_request(address, 'b'))
    t3 = threading.Thread(target=client.delete_request(address, 'b'))

    t1.start()
    t2.start()
    t3.start()


if __name__ == "__main__":
    main()


