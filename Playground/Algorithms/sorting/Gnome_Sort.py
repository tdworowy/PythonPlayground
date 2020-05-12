from random import randint


def gnome_sort(list_):
    pos = 0
    list_sort = list_[:]
    while pos < len(list_sort):
        if pos == 0 or list_sort[pos] >= list_sort[pos - 1]:
            pos += 1
        else:
            list_sort[pos], list_sort[pos - 1] = list_sort[pos - 1], list_sort[pos]
            pos -= 1
    return list_sort


if __name__ == '__main__':
    list_sort = [randint(0, 10000) for x in range(1000)]
    sortedList = gnome_sort(list_sort)
    print(sortedList)

    list_sort.sort()
    print(list_sort)
    assert sortedList == list_sort
