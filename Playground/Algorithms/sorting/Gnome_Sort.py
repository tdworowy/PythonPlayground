from random import randint

from Playground.my_utils.staff.timer3 import timer3


@timer3
def gnome_sort(list_: list) -> list:
    pos = 0
    while pos < len(list_):
        if pos == 0 or list_[pos] >= list_[pos - 1]:
            pos += 1
        else:
            list_[pos], list_[pos - 1] = list_[pos - 1], list_[pos]
            pos -= 1
    return list_


if __name__ == '__main__':
    list_sort = [randint(0, 10000) for x in range(10000)]
    sorted_list = gnome_sort(list_sort[:])

    list_sort.sort()
    assert sorted_list == list_sort
