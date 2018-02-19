import requests
import threading


def request(address):

    i = 0
    while i < 10:
        i += 1
        response = requests.get(address)
        print(response.url)  # remove later - check pritn



def main():
    address = "http://localhost:8080/WebApp/HelloServlet"
    threads = []
    for j in range(7):
        t = threading.Thread(target=request(address))
        threads.append(t)
        t.start()


if __name__ == "__main__":
    main()
