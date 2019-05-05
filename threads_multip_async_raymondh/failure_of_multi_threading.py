import datetime
import threading

import requests


def cpu_bound_task(number):
    sum = 0
    for i in range(number):
        sum += i
    print(sum)
    return sum


def sequential(number):
    # call the function sequentially 5 times.
    start_time = datetime.datetime.now()
    for i in range(5):
        cpu_bound_task(number)
    time_elapsed = datetime.datetime.now() - start_time
    print("Time Elapsed using normal sequential method", time_elapsed)
    return time_elapsed


def threader(number):
    # call the function in 5 separate threads.
    threads = []
    start_time = datetime.datetime.now()
    for i in range(5):
        # Create a new thread, assign it the worker function, and the argument for it
        p = threading.Thread(target=cpu_bound_task, args=(number,))
        p.start()  # Start the thread
        threads.append(p)  # Add it to list of threads
    for thread in threads:
        thread.join()  # wait for all the threads to finish
    time_elapsed = datetime.datetime.now() - start_time
    print("Time Elapsed using multi threading", time_elapsed)
    return time_elapsed


if __name__ == "__main__":
    number = 50000000
    normal_time = sequential(number)
    threading_time = threader(number)
    print("Improved percent", int((normal_time - threading_time) / normal_time * 100))
