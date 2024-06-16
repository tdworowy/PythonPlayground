input = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
input2 = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5],
]
input3 = [
    [-1, 1, -1, 0, 0, 0],
    [0, -1, 0, 0, 0, 0],
    [-1, -1, -1, 0, 0, 0],
    [0, -9, 2, -4, -4, 0],
    [-7, 0, 0, -2, 0, 0],
    [0, 0, -1, -2, -4, 0],
]
input4 = [
    [3, 7, -3, 0, 1, 8],
    [1, -4, -7, -8, -6, 5],
    [-8, 1, 3, 3, 5, 7],
    [-2, 4, 3, 1, 2, 7],
    [2, 4, -5, 1, 8, 4],
    [5, -7, 6, 5, 2, 8],
]


def __print(arr):
    for ele in arr:
        print(ele)


def get_all_hourgs(arr):
    hourugs = []
    for li in range(len(arr)):
        i, j = 0, 3
        z = 1
        if li + 2 > len(arr) - 1:
            break
        while j <= len(arr[li]):
            x1 = arr[li][i:j]
            x2 = arr[li + 1][z]
            x3 = arr[li + 2][i:j]
            hourugs.append(x1 + [x2] + x3)
            i += 1
            j += 1
            if z < len(arr[li]):
                z += 1
    __print(hourugs)
    return hourugs


def hourglass_sum(arr):
    return max(list(map(sum, get_all_hourgs(arr))))


if __name__ == "__main__":
    print(hourglass_sum(input4))
