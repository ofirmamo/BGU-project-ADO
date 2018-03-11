import requests
import threading
import Client

def main():
    address = "http://127.0.0.1:5000"

    client = Client.Client()

    for i in range(5):
    	init_user='user'+str(i)
    	th = threading.Thread(target=client.client_requests(address ,init_user, str(i), 55))
    	th.start() 
    


if __name__ == "__main__":
    main()