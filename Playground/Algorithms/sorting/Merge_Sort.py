import sys
from random import randint

from Playground.my_utils.staff.timer3 import timer3

sys.setrecursionlimit(10000)


@timer3
def merge_sort1(list_: list) -> list:
    result = []
    if len(list_) < 2:
        return list_

    mid = len(list_) // 2
    part_list1 = merge_sort1(list_[:mid])
    part_list2 = merge_sort1(list_[mid:])

    i = 0
    j = 0
    len1 = len(part_list1)
    len2 = len(part_list2)

    while i < len1 and j < len2:
        if part_list1[i] > part_list2[j]:
            result.append(part_list2[j])
            j += 1
        else:
            result.append(part_list1[i])
            i += 1
    result.extend(part_list1[i:])
    result.extend(part_list2[j:])
    return result


@timer3
def merge_sort2(list_: list) -> list:
    if len(list_) >1:
        mid = len(list_) // 2
        left = list_[:mid]
        right = list_[mid:]

        merge_sort2(left)
        merge_sort2(right)
        a, b, c = 0, 0, 0

        len_left = len(left)
        len_right = len(right)

        while a < len_left and b < len_right:
            if left[a] < right[b]:
                list_[c] = left[a]
                a += 1
            else:
                list_[c] = right[b]
                b += 1
            c += 1

        while a < len_left:
            list_[c] = left[a]
            a += 1
            c += 1

        while b < len_right:
            list_[c] = right[b]
            b += 1
            c += 1

    return list_


if __name__ == '__main__':
    list_sort = [randint(0, 10000) for x in range(100000)]
    sorted_list1 = merge_sort1(list_sort[:])
    sorted_list2 = merge_sort2(list_sort[:])

    list_sort.sort()
    assert sorted_list1 == sorted_list2 == list_sort
