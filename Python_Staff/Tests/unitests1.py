print("I'm : ", __name__)


def min_max(test, *args):
    res = args[0]
    for arg in args:
        if test(arg, res):
            res = arg
    return res


def less_than(x, y): return x < y


def greater_than(x, y): return x > y


if __name__ == '__main__':  # tests , won't run if module is imported
    print(min_max(less_than, 4, 2, 1, 4, 67, 8, 9, 3, 1))
    print(min_max(greater_than, 4, 2, 1, 4, 67, 8, 9, 3, 1))
