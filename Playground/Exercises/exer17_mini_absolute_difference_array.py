import math

array1= [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]

def minimum_absolute_difference(arr):
    abs_diffs = set()

    for n in range(0,len(arr)):
        ele_i = arr[n]
        for ele_j in arr[n+1:]:
            abs_diffs.add(abs(ele_i-ele_j))
    return min(abs_diffs)

def minimum_absolute_difference2(arr):
    abs_diffs = set()

    for n in range(0,len(arr)):
        ele_i = arr[n]
        [abs_diffs.add(abs(ele_i-ele_j)) for ele_j in arr[n+1:]]
    return min(abs_diffs)


def minimum_absolute_difference3(arr): #Fastest
    arr.sort()
    diff = arr[-1] #biggest element
    for i in range(1, len(arr)):
        diff = min(diff, arr[i] - arr[i - 1])
    return diff


if __name__ == "__main__":
    print(minimum_absolute_difference3(array1))