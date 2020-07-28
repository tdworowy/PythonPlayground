# for python 2.6 (can use nonlocal in 3.x)
def tester(start):
    global state
    state = start

    def nested(label):
        global state
        print(label, state)
        state += 1

    return nested


if __name__ == "__main__":
    f = tester(0)
    f("spam1")
    f("test1")

    g = tester(22)

    g("test2")
    f("spam2")
