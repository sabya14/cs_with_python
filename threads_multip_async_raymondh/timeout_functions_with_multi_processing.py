import multiprocessing
import time


def foo(n, send):
    for i in range(8):
        print("Counting")
        time.sleep(1)
    send.send("Process completed")


if __name__ == '__main__':
    receive, send = multiprocessing.Pipe(False)
    p = multiprocessing.Process(target=foo, name="Foo", args=(10, send))
    p.start()
    p.join(5)
    if p.is_alive():
        p.terminate()
        p.join()
        send.send("Process timed out killing it")
    print("Result", receive.recv())
