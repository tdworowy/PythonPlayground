import numpy as np
import math


def generate_square(size: int) -> np.ndarray:
    magic_square = np.zeros((size, size))
    i = size / 2
    j = size - 1
    num = 1
    while num <= (size * size):
        if i == -1 and j == size:
            j = size - 2
            i = 0
        else:
            if j == size:
                j = 0
            if i < 0:
                i = size - 1
        if magic_square[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            magic_square[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1
    return magic_square


def generate_all_magic_squares(size: int) -> list:
    rotations = [np.rot90(generate_square(size), x) for x in range(size + 1)]
    reflections = [np.flip(x, 1) for x in rotations]
    all_magic = rotations + reflections
    return [ele.tolist() for ele in all_magic]


def forming_magic_square(square: list) -> int:
    all_magic_squares = generate_all_magic_squares(len(square[0]))

    if square in all_magic_squares:
        return 0

    all_costs = []
    for magic_square in all_magic_squares:
        cost = 0
        for m_row, s_row in zip(magic_square, square):
            for i, j in zip(m_row, s_row):
                if i != j:
                    cost += math.fabs(i - j)
        all_costs.append(cost)
    return int(min(all_costs))


if __name__ == "__main__":
    # print(generate_all_magic_squares(3))
    s1 = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    result = forming_magic_square(s1)
    print(result)  # 7
    s2 = [[2.0, 7.0, 6.0], [9.0, 5.0, 1.0], [4.0, 3.0, 8.0]]
    result = forming_magic_square(s2)
    print(result)  # 0
