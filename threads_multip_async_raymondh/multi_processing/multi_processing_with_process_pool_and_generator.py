# Multiprocessing and passing messages amongst them with the help of queue.
import multiprocessing as mp
import random
import time


def a_generator():
    for i in range(10):
        yield i


def task(i):
    time.sleep(random.randint(1, 10))
    print("Do some work here", i * 10)


def parallel_runner(no_of_process=4):
    processes = int(no_of_process)
    pool = mp.Pool(processes)
    try:
        pool = mp.Pool(processes)
        jobs = []
        for i in a_generator():
            jobs.append(pool.apply_async(task, (i,)))
        for job in jobs:
            job.get()
        pool.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parallel_runner()
