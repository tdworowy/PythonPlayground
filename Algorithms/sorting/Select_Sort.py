from random import randint


def select_sort(list_):
    result = []
    list_sort = list_[:]
    while len(list_sort) > 0:
        result.append(min(list_sort))
        index = list_sort.index(min(list_sort))
        list_sort.pop(index)
    return result


if __name__ == '__main__':
    list_sort = [randint(0, 1000) for x in range(10)]
    sortedList = select_sort(list_sort)
    print(sortedList)

    list_sort.sort()
    print(list_sort)
    assert sortedList == list_sort
