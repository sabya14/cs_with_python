import datetime
import threading

import requests


def io_bound_task(url):
    resp = requests.get(url)
    print("Received Response", resp.status_code)


def sequential(url):
    # call the function sequentially 5 times.
    start_time = datetime.datetime.now()
    for i in range(5):
        io_bound_task(url)
    time_elapsed = datetime.datetime.now() - start_time
    print("Time Elapsed using normal sequential method", time_elapsed)
    return time_elapsed


def threader(url):
    # call the function in 5 separate threads.
    threads = []
    start_time = datetime.datetime.now()
    for i in range(5):
        # Create a new thread, assign it the worker function, and the argument for it
        p = threading.Thread(target=io_bound_task, args=(url,))
        p.start()  # Start the thread
        threads.append(p)  # Add it to list of threads
    for thread in threads:
        thread.join()  # wait for all the threads to finish
    time_elapsed = datetime.datetime.now() - start_time
    print("Time Elapsed using multi threading", time_elapsed)
    return time_elapsed


if __name__ == "__main__":
    url = "https://www.spotify.com"
    normal_time = sequential(url)
    threading_time = threader(url)
    print("Improved percent", int((normal_time - threading_time) / normal_time * 100))
