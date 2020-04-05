def is_permutation(permutation: list) -> bool:
    return set(permutation) == set(range(len(permutation)))


def is_even_permutation(permutation: list) -> bool:
    steps = 0
    for i in range(1, len(permutation)):
        key = permutation[i]
        j = i - 1
        while j >= 0 and key < permutation[j]:
            permutation[j + 1] = permutation[j]
            steps += 1
            j -= 1
        permutation[j + 1] = key
    return steps % 2 == 0


def puzzle_15_solver(permutation: list) -> list:
    assert len(permutation) == 16
    assert is_permutation(permutation)
    assert is_even_permutation(permutation[:-1])
    steps = []
    # TODO someday


if __name__ == "__main__":
    permutation = [1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0]
    puzzle_15_solver(permutation)
