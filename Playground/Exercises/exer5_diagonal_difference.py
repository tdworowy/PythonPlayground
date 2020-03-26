def count(arr):
    diagonal = 0
    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            if i == j:
                diagonal = diagonal + element
    return diagonal


def diagonal_difference(arr):
    diagonal1 = count(arr)
    diagonal2 = count(reversed(arr))
    return abs(diagonal1 - diagonal2)


x = [[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]]

if __name__ == "__main__":
    print(diagonal_difference(x))
