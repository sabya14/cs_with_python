# Multiprocessing and passing messages amongst them with the help of queue.
import multiprocessing


class MyProcess:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def process(self):
        process_name = multiprocessing.current_process().name
        print(f'Processing in {process_name} for {self.name}')


def worker(q):
    obj = q.get()  # Get the obj from queue, and processing it.
    obj.process()


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    queue.put(MyProcess("New asd Process"))
    queue.put(MyProcess("New Process 1"))
    queue.put(MyProcess("New Process 2"))
    queue.close()
    queue.join_thread()
    p.join()
