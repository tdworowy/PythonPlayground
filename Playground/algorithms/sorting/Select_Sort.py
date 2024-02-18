from random import randint

from Playground.my_utils.staff.timer3 import timer3


@timer3
def select_sort1(list_: list) -> list:
    result = []
    while len(list_) > 0:
        result.append(min(list_))
        index = list_.index(min(list_))
        list_.pop(index)
    return result


@timer3
def select_sort2(list_: list) -> list:
    list_len = len(list_)
    for fill_slot in range(list_len - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list_[location] > list_[max_index]:
                max_index = location
            list_[fill_slot], list_[max_index] = list_[max_index], list_[fill_slot]
    return list_


if __name__ == '__main__':
    list_sort = [randint(0, 10000) for x in range(10000)]
    sorted_list1 = select_sort1(list_sort[:])
    sorted_list2 = select_sort2(list_sort[:])

    list_sort.sort()
    assert sorted_list1 == sorted_list2 == list_sort
