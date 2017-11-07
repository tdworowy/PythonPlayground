import sys
from random import randint

sys.setrecursionlimit(10000)


def merge_sort(list):
    result = []
    if len(list) < 2:
        return list
    mid = int(len(list) / 2)
    part_list1 = merge_sort(list[:mid])
    part_list2 = merge_sort(list[mid:])
    i = 0
    j = 0
    while i < len(part_list1) and j < len(part_list2):
        if part_list1[i] > part_list2[j]:
            result.append(part_list2[j])
            j += 1
        else:
            result.append(part_list1[i])
            i += 1
    result.extend(part_list1[i:])
    result.extend(part_list2[j:])
    return result


if __name__ == '__main__':
    list = [randint(0, 10000) for x in range(1000)]
    sortedList = merge_sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list
