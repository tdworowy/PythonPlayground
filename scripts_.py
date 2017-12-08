import sys


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


if __name__ == "__main__":
    # print(list(staff2()))
    print(Ackermann(3, 6))
