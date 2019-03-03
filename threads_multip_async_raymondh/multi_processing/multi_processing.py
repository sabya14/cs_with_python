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
    queue_1 = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p_1 = multiprocessing.Process(target=worker, args=(queue_1,))
    p.start()
    p_1.start()
    queue.put(MyProcess("New Process"))
    queue.close()
    queue.join_thread()
    queue_1.put(MyProcess("New Process_1"))
    queue_1.close()
    queue_1.join_thread()
    p.join()
    p_1.join()
