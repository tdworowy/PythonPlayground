from random import randint

from Playground.my_utils.staff.timer3 import timer3


@timer3
def insertion_sort(list_: list) -> list:
    for i in range(1, len(list_)):
        j = i - 1
        element_next = list_[i]
        while list_[j] > element_next and j >= 0:
            list_[j + 1] = list_[j]
            j = j - 1
        list_[j + 1] = element_next
    return list_


if __name__ == "__main__":
    list_ = [randint(0, 10000) for x in range(10000)]
    sorted_list = insertion_sort(list_[:])

    list_.sort()
    assert list_ == sorted_list
