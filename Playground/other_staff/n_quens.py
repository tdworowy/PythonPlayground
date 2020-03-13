import itertools as it

"""Brute force"""
def is_solution(perm: tuple) -> bool:
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True


def find_perm(size: int) -> tuple:
    for perm in it.permutations(range(size)):
        if is_solution(perm):
            return perm


if __name__ == "__main__":
    print(find_perm(15))
