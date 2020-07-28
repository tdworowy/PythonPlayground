import _thread


def func():
    for i in range(10):
        print(i)


if __name__ == "__main__":

    try:
        _thread.start_new_thread(func, ())
        _thread.start_new_thread(func, ())
    except Exception:
        print("Error: unable to start thread")

    while 1:
        pass
