x = [1, 3, 5, 2, 4, 6, 7]
x2 = [3, 7, 6, 9, 1, 8, 10, 4, 2, 5]
x3 = [2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3,
      32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19]


def swap(num1, num2, arr):
    first_index = arr.index(num1)
    second_index = arr.index(num2)
    arr[first_index] = num2
    arr[second_index] = num1


def swap2(index1, index2, arr):
    index1_value = arr[index1]
    index2_value = arr[index2]
    arr[index1] = index2_value
    arr[index2] = index1_value


def minimum_swaps3(arr):
    number_of_swap = 0
    new_list = arr.copy()
    arr.sort()
    sorted_list = arr.copy()

    for index, ele in enumerate(new_list):
        if ele != sorted_list[index]:
            j = index + 1
            while j < (len(new_list)):
                if new_list[j] == sorted_list[index]:
                    swap(new_list[index], new_list[j], new_list)
                    number_of_swap += 1
                    break
                j += 1
    return number_of_swap


def minimum_swaps(arr):
    swap = 0
    i = 0
    while i < len(arr):
        if len(arr) == 7 and i == 6:
            break
        if arr[i] == (i + 1):
            i += 1
            continue
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        swap += 1
    return swap


if __name__ == "__main__":
    # print(minimumSwaps3(x2)) #9
    # print(minimum_swaps3(x3)) #46
    # print(minimum_swaps(x3))
    print(minimum_swaps(x))
    # swap(3, 7 ,x2)
    # print(x2)
