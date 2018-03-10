import requests
import threading
import Client

def main():
    address = "http://127.0.0.1:5000"

    client = Client.Client()

    '''

	    t1 = threading.Thread(target=client.get_request(address))
	    t2 = threading.Thread(target=client.post_request(address, 'b'))
	    t3 = threading.Thread(target=client.delete_request(address, 'b'))
	    t1.start()
    	t2.start()
   		t3.start()
    '''
    for i in range(10):
    	init_user='user'+str(i)
    	th = threading.Thread(target=client.client_requests(address ,init_user, str(i), 1))
    	th.start() 
    


if __name__ == "__main__":
    main()