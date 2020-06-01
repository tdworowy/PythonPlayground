from contextlib import contextmanager


@contextmanager
def context_illustration():
    print("Open context")
    try:
        yield  # required by contextlib
    except Exception as e:
        print("Close context")
        print("With error %s" % e)
        raise
    else:
        print("Close context")
        print("Without error")


if __name__ == "__main__":
    with context_illustration() as action:
        print("Done")

    print("_" * 20)

    with context_illustration() as action:
        raise TypeError
        print("Not Done")
