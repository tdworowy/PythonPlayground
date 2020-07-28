def gen():
    while True:
        x = (yield)
        print(x)


if __name__ == "__main__":
    y = gen()
    next(y)
    y.send("Test")
    # next(y)
    y.send(1)
    y.send(2)
    y.send("Dupa")
