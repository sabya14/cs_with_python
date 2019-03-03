# Multiprocessing and passing messages amongst them with the help of queue.
import multiprocessing
import sys
import time


class MyProcess:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def process(self):
        process_name = multiprocessing.current_process().name
        print(f'Processing in {process_name} for {self.name}')


def worker(lock, stream):
    print("Getting lock in process 1")
    with lock:
        print("Got lock in process 1")
        stream.write('Lock acquired 1')
        time.sleep(3)


def worker_1(lock, stream):
    print("Getting lock in process 2, has to wait for 3 seconds as worker 1 has lock")
    with lock:
        print("Got lock in process 2")
        stream.write('Lock acquired 2')


if __name__ == "__main__":
    _lock = multiprocessing.Lock()
    _stream = sys.stdout
    p = multiprocessing.Process(target=worker, args=(_lock, _stream))
    p1 = multiprocessing.Process(target=worker_1, args=(_lock, _stream))
    p.start()
    p1.start()
    p.join()
    p1.join()
