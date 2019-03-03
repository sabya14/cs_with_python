# Multiprocessing and passing messages amongst them with the help of queue.
import multiprocessing
import time


class MyProcess:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def process(self):
        process_name = multiprocessing.current_process().name
        print(f'Processing in {process_name} for {self.name}')


def worker(e):
    print("Waiting for event to start")
    e.wait()
    print("Event has now started")


if __name__ == "__main__":
    e = multiprocessing.Event()
    p = multiprocessing.Process(target=worker, args=(e,))
    p.start()
    print("Event now is paused now ", e, )
    time.sleep(3)
    print("Starting worker of process")
    e.set()
    p.join()
