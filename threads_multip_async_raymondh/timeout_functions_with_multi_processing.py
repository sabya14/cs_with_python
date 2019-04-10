import multiprocessing
import time


def foo(n, send):
    for i in range(8):
        print("Counting")
        time.sleep(1)
    send_end.send("Process completed")


if __name__ == '__main__':
    recv_end, send_end = multiprocessing.Pipe(False)
    p = multiprocessing.Process(target=foo, name="Foo", args=(10, send_end))
    p.start()
    p.join(5)
    if p.is_alive():
        p.terminate()
        p.join()
        send_end.send("Process timed out killing it")
    print("Result", recv_end.recv())
