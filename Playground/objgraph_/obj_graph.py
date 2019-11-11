import objgraph


class Staff:
    def __init__(self, ele):
        self.ele = ele

    def get(self):
        return self.ele


def example(count):
    x = range(3)
    y = [Staff(i) for i in x]
    if count == 0:
        return Staff(y)
    else:
        return example(count - 1)


def example2():
    y = 1
    for i in range(10):
        y = Staff(y)
    return y


def example3():
    l = []
    l1 = []
    for x in range(7):
        z = example(5)
        q = example2()
        l.append(z)
        l.append(q)
        l.append((z, q))
        l1.append(l)
    l.append(l1)
    return Staff(l)


def test1():
    objgraph.show_refs(example(3), filename="obj.png", refcounts=True)


def test2():
    x = range(100)
    y = map(example, x)
    objgraph.show_refs(y, filename="obj2.png", refcounts=True)


def test3():
    objgraph.show_refs(example2(), filename="obj3.png", refcounts=True, max_depth=5, too_many=10)


def test4():
    """Take lot of time"""
    objgraph.show_refs(example3(), filename="obj4.png", refcounts=True, max_depth=10, too_many=100)


def test5():
    objgraph.show_refs(example3(), filename="obj5.png", refcounts=True, max_depth=10, too_many=20)


if __name__ == "__main__":
    test5()
