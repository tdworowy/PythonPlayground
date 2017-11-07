from random import randint


def buble_sort(list_):
    list = list_[:]
    result = []
    i = 1
    while len(result) < len(list_):
        for j in range(len(list) - 1):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
            i += 1
        i = 1
        result.append(list[-1])
        list = list[:-1]
    return result[::-1]


if __name__ == '__main__':
    list = [randint(0, 1000) for x in range(1000)]
    sortedList = buble_sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list
