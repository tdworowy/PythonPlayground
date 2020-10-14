from random import randint

from Playground.my_utils.staff.timer3 import timer3


@timer3
def select_sort(list_: list) -> list:
    result = []
    while len(list_) > 0:
        result.append(min(list_))
        index = list_.index(min(list_))
        list_.pop(index)
    return result


if __name__ == '__main__':
    list_sort = [randint(0, 10000) for x in range(10000)]
    sorted_list = select_sort(list_sort[:])

    list_sort.sort()
    assert sorted_list == list_sort
