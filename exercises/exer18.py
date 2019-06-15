def bubble_sort(list_):
    list_sort = list_[:]
    result = []
    swaps = 0
    i = 1
    while len(result) < len(list_):
        for j in range(len(list_sort) - 1):
            if list_sort[j] > list_sort[i]:
                list_sort[j], list_sort[i] = list_sort[i], list_sort[j]
                swaps += 1
            i += 1
        i = 1
        result.append(list_sort[-1])
        list_sort = list_sort[:-1]
    print(result)
    result = result[::-1]
    print(result)
    print("Array is sorted in %s swaps." % swaps)
    print("First Element: %s" % result[0])
    print("Last Element: %s" % result[-1])


bubble_sort([1,2,3])