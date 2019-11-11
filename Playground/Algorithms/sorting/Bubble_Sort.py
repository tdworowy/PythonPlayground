from random import randint


def bubble_sort(list_):
    list_sort = list_[:]
    result = []
    i = 1
    while len(result) < len(list_):
        for j in range(len(list_sort) - 1):
            if list_sort[j] > list_sort[i]:
                list_sort[j], list_sort[i] = list_sort[i], list_sort[j]
            i += 1
        i = 1
        result.append(list_sort[-1])
        list_sort = list_sort[:-1]
    return result[::-1]


if __name__ == '__main__':
    list_sort = [randint(0, 1000) for x in range(1000)]
    sortedList = bubble_sort(list_sort)
    print(sortedList)

    list_sort.sort()
    print(list_sort)
    assert sortedList == list_sort
