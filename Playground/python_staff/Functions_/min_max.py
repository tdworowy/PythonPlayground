def min_max(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def less_than(x, y):
    return x < y


def grtr_than(x, y):
    return x > y


if __name__ == "__main__":
    print(min_max(less_than, 4, 2, 1, 5))
    print(min_max(grtr_than, 4, 2, 1, 5))
    # same think as built-in functions min and max
