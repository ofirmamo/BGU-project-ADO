import requests
import threading
import Client


def request(address):

    i = 0
    while i < 10:
        i += 1
        response = requests.get(address)
        print(response.url)  # remove later - check pritn


def main():
    address = "http://www.google.com"
    # threads = []
    client = Client.Client()
    # for j in range(7):
    t1 = threading.Thread(target=client.get_request(address))
    t2 = threading.Thread(target=client.post_request(address, 'a'))
    t3 = threading.Thread(target=client.delete_request(address, 'a'))

    # threads.append(t)
    t1.start()
    #t2.start()
    #t3.start()


if __name__ == "__main__":
    main()
