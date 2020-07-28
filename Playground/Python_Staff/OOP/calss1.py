class tester:
    def __init__(self, start):
        self.sate = start

    def nested(self, label):
        print(label, self.sate)
        self.sate += 1


class tester2:
    def __init__(self, start):
        self.state = start

    def __call__(self, label):
        print(label, self.state)
        self.state += 1


class klas1:
    class klaas2:
        def display(self):
            print("___________")
            print("Test")


if __name__ == '__main__':
    f = tester(0)
    f.nested('spam')
    f.nested('dupa')

    g = tester(33)
    g.nested("spam2")
    f.nested('dupa2')

    print(f.sate)
    print(g.sate)
    H = tester2(99)
    H("xxx")
    H("xxx2")

    obj1 = klas1()
    obj2 = obj1.klaas2()
    obj2.display()
