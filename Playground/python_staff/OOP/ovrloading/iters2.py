class Iters1:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, index):
        print("get[%s]: " % index, end="")
        return self.data[index]

    def __iter__(self):
        print("iter=> ", end="")
        self.ix = 0
        return self

    def __next__(self):
        print("next: ", end="")
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print("Contains: ", end="")
        return item in self.data


class Iters2:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, index):
        print("get[%s]: " % index, end="")
        return self.data[index]

    def __iter__(self):
        print("iter=> ", end="")
        self.ix = 0
        return self

    def __next__(self):
        print("next: ", end="")
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item


class Iters3:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, index):
        print("get[%s]: " % index, end="")
        return self.data[index]


def Iter_est(obj):
    print("\n" + "_" * 20)
    print("Test: ", obj.__name__)
    print("_" * 20)
    X = obj([x for x in range(1, 10)])
    print(3 in X)

    for i in X:
        print(i, end=" | ")

    print()

    print([i**2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)
    while True:
        try:
            print(next(I), end=" @ ")
        except StopIteration:
            break


if __name__ == "__main__":
    for obj in [Iters1, Iters2, Iters3]:
        Iter_est(obj)
