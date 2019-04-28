import gc
import multiprocessing
import os
import threading
from multiprocessing import Process

import psycopg2

config = {
    "user": "sabyasachi",
    "password": "qweasdzxc",
    "host": "localhost",
    "database": "explore_data",
    "database_type": "postgres"
}


def create_postgres_connection(config, return_dict=None, ns=None):
    # Connect to the database, we have to timeout this function if it takes too long.
    print(os.getpid())
    host = config['host']
    database = config['database']
    username = config['user']
    password = config['password']
    connection = psycopg2.connect(host=host, database=database, user=username, password=password)
    print(return_dict)
    if return_dict is not None:
        return_dict['connection'] = connection
    if ns:
        ns.result = connection
    print("ID", id(connection))


def run_with_limited_time(func, args, kwargs, time):
    """Runs a function with time limit

    :param func: The function to run
    :param args: The functions args, given as tuple
    :param kwargs: The functions keywords, given as dict
    :param time: The time limit in seconds
    :return: True if the function ended successfully. False if it was terminated.
    """
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()
    p.join()
    return True


def run_with_limited_time_thread(func, args, kwargs, time):
    """Runs a function with time limit

    :param func: The function to run
    :param args: The functions args, given as tuple
    :param kwargs: The functions keywords, given as dict
    :param time: The time limit in seconds
    :return: True if the function ended successfully. False if it was terminated.
    """
    p = threading.Thread(target=func, args=args, kwargs=kwargs)
    p.start()
    p.join(timeout=5)
    if p.is_alive():
        print("TIme out")
    else:
        print("Get Value")
    return True


def objects_by_id(id_):
    for obj in gc.get_objects():
        if id(obj) == id_:
            return obj
    raise Exception("No found")


if __name__ == '__main__':
    result = {}
    run_with_limited_time_thread(create_postgres_connection, (config, result), {}, 3)
    print(type(list(result.values())[0]))
    # obj = objects_by_id(list(result.values())[0])
    # print("Obj", obj)

# if __name__ == '__main__':
#     manager = multiprocessing.Manager()
#     return_dict = manager.dict()
#     manager = multiprocessing.Manager()
#     ns = manager.Namespace()
#     ns.x = 10
#     ns.y = 20
#     run_with_limited_time(create_postgres_connection, (config, return_dict, ns), {}, 3)
#     print(os.getpid())
#     print(return_dict.values()[0])
#     print(ns)