class Numbers:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self


class Numbers2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Numbers2(self.val + other)


if __name__ == '__main__':
    x = Numbers(5)
    x += 1
    x += 1

    print(x)
    print(x.val)

    x = Numbers2(5)
    x += 1
    x += 1

    print(x)
    print(x.val)
