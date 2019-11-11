def tester1(start):
    state = start

    def nested(label):
        print(label, state)

    return nested


def tester2(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested

if __name__ == "__main__":
    F = tester1(0)

    print(F('Spam'))
    print(F('Dupa'))

    F = tester2(0)
    print(F('Spam'))
    print(F('Dupa'))

    G = tester2(50)
    print(G('Spam'))
    print(G('Dupa'))

    print(F('AAAA'))
