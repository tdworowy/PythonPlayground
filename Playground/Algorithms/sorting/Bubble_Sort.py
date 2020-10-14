from random import randint

from Playground.my_utils.staff.timer3 import timer3


@timer3
def bubble_sort1(list_: list) -> list:
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


@timer3
def bubble_sort2(list_: list) -> list:
    last_element_index = len(list_) - 1
    for pass_no in range(last_element_index, 0, -1):
        for idx in range(pass_no):
            if list_[idx] > list_[idx + 1]:
                list_[idx], list_[idx + 1] = list_[idx + 1], list_[idx]
    return list_


if __name__ == '__main__':
    list_ = [randint(0, 10000) for x in range(10000)]
    sorted_list1 = bubble_sort1(list_)
    sorted_list2 = bubble_sort2(list_[:])

    list_.sort()
    assert sorted_list1 == list_ == sorted_list2
