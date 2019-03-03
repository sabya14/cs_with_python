# Multiprocessing and passing messages amongst them with the help of queue.
import multiprocessing
import random
import time

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
    if FUZZ:
        time.sleep(random.random())


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        process_name = multiprocessing.current_process().name
        while True:
            next_task = self.task_queue.get()
            print("Next task", next_task)
            if next_task is None:
                print("Tasks overs, calling task done")
                self.task_queue.task_done()
                return
            result = next_task.process()
            self.task_queue.task_done()
            self.result_queue.put(result)


class MyProcess:

    def __init__(self, name):
        fuzz()
        print("Starting Jobs", name)
        fuzz()
        self.name = name

    def __str__(self):
        return self.name

    def process(self):
        fuzz()
        process_name = multiprocessing.current_process().name
        fuzz()
        return f"Processing in {process_name} for {self.name}"


if __name__ == "__main__":
    task_queue = multiprocessing.JoinableQueue()
    results_queue = multiprocessing.Queue()
    no_of_consumers = multiprocessing.cpu_count() * 2
    print(f"No of consumers", no_of_consumers)
    consumers = [Consumer(task_queue, results_queue) for i in range(no_of_consumers)]
    for consumer in consumers:
        consumer.start()

    num_of_jobs = 10
    for i in range(num_of_jobs):
        task_queue.put(MyProcess(f"Process {str(i)}"))

    # Add a poison pill for each consumer
    for i in range(no_of_consumers):
        task_queue.put(None)

    task_queue.join()
    while num_of_jobs:
        result = results_queue.get()
        print(result)
        num_of_jobs -= 1
