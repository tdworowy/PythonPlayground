import itertools as it

"""Brute force"""


def is_solution(perm: tuple) -> bool:
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True


def find_perm(size: int) -> tuple:
    solutions = []
    for perm in it.permutations(range(size)):
        if is_solution(perm):
            solutions.append(perm)
    return solutions


"""Backtracking Solution """


def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()


if __name__ == "__main__":
    # print(find_perm(8))
    #  print(len(find_perm(8)))
    #  for solution in find_perm(8):
    #      print(solution)
    extend(perm=[], n=30)
