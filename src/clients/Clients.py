import threading

import yaml

import Client
import requests


def main():
    address = "http://127.0.0.1:5000"

    client = Client.Client()

    # with open('./src/clients/Tests/tests.yml', 'r') as config_file:
    with open('./Tests/tests.yml', 'r') as config_file:
        config = yaml.load(config_file)
        thresholds = config['thresholds']
        n_logs_to_init = config['n_logs_to_init']
        num_messages = config['num_messages']
        num_injects = config['num_injects']
        num_tests = config['num_tests']

    configurations = [(threshold, n_logs, num_message, num_inject, num_tests)
                      for threshold in thresholds
                      for n_logs in n_logs_to_init
                      for num_message in num_messages
                      for num_inject in num_injects
                      ]

    for configuration in configurations:
        run_test(address, client, configuration)

    requests.get("{}/stats".format(address))


def run_test(address, client, configuration):
    threshold, n_logs_to_init, num_messages, num_injects, num_tests = configuration

    requests.get('{}/set_configuration'.format(address), params={'threshold': threshold,
                                                                 'n_logs_to_init': n_logs_to_init,
                                                                 })
    for i in range(num_tests):
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
        th3 = threading.Thread(target=client.random_user(address, 'random', 'r', num_messages, "The Post",
                                                         {'address': address, 'zip_code': "1234",
                                                          'full_name': "name surname", 'age': "20"}))
        th3.start()
        th1.join()
        th2.join()
        th3.join()
        th4 = threading.Thread(target=client.error_inject(address, num_injects))
        th4.start()
        th4.join()
        requests.get('{}/reset_test'.format(address))


if __name__ == "__main__":
    main()
