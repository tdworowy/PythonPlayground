import sys
from cmath import inf


def staff():
    x = [(i, j) for i in range(0, 10) for j in range(0, 10)]
    print(x)

    for i, j in enumerate(x):
        num = int(''.join(map(str, [x[i][0], x[i][1]])))
        if (j[0] + j[1]) * 5 == num: print(num)


def primes(num):
    num = int(num)
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        return num


def staff2():
    e_ = '2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149 '
    return map(primes, list(e_.replace(".", "")))


def Ackermann(m, n):
    sys.setrecursionlimit(10000)
    if m == 0: return n + 1
    if m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    else:
        return Ackermann(m - 1, Ackermann(m, n - 1))


def alg(n):
    if n == 1:
        return n
    else:
        res = 1 + alg(n) + 1
        n = n - 1
        return res


def recur(num):
    if num > 100:
        return num - 10
    else:
        return recur(recur(num + 11))


def minimize_path(grid, num):
    """min(x,y)=grid(x,y) + min(min(x+1,y),min(x,y+1)"""

    def min(x, y):
        if (x, y) == (num - 1, num - 1):
            return grid[num - 1][num - 1]
        to_visit = [(x + 1, y), (x, y + 1)]
        minimum = inf
        for m, n in to_visit:
            if (m < 0) or (m >= num) or (n < 0) or (n >= num):
                continue
            else:
                cost = grid[x][y] + min(m, n)
                if cost < minimum:
                    minimum = cost
        return minimum

    return min


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


# i thin it don't work
#TODO
def magic_squer(size):
    count = size ** 2
    matrix = [[(size * y) + x + 1 for x in range(size)] for y in range(size)]
    for i in range(0, size // 4):
        for j in range(3 * (size // 4), size):
            matrix[i][j] = (count + 1) - matrix[i][j]

    for i in range(3 * (size // 4), size):
        for j in range(1, size // 4):
            matrix[i][j] = (size * size + 1) - matrix[i][j]

    for i in range(3 * (size // 4), size):
        for j in range(3 * (size // 4), size):
            matrix[i][j] = (count + 1) - matrix[i][j]

    for i in range(size // 4, 3 * (size // 4)):
        for j in range(size // 4, 3 * (size // 4)):
            matrix[i][j] = (count + 1) - matrix[i][j]
    return matrix


if __name__ == "__main__":
    # print(list(staff2()))
    #  print(Ackermann(3, 6))
    # print(recur(98))
    # grid = [[23, 32, 62, 20, 77, 42, 31],
    #         [15, 14, 10, 11, 48, 32, 30],
    #         [14, 46, 71, 31, 53, 7, 82],
    #         [20, 12, 78, 78, 46, 24, 43],
    #         [37, 16, 12, 99, 15, 97, 85],
    #         [13, 29, 82, 71, 63, 27, 75],
    #         [44, 81, 80, 48, 2, 45, 17]]
    #
    # num = 7
    # x = minimalize_path(grid, num)
    # print(x(0, 0))
    # x = sum([i for i in range(10001) if perfect_number(i)])
    # print(x)
    for row in magic_squer(4):
        print(row)
