from itertools import permutations


# performance could by much better
def count_triplets(arr: list, r: int) -> int:
    try:
        if len(arr) <= 2:
            return 0
        triplets = [tuple(sorted(per)) for per in permutations(arr, 3)]
        count = 0
        for triplet in triplets:
            if triplet[1] == triplet[0] * r and triplet[2] == triplet[1] * r:
                count += 1

        return count // 6
    except Exception:
        return 0


if __name__ == '__main__':
    arr = [1, 5, 5, 25, 125]
    r = 5
    triplets_count = count_triplets(arr, r)
    print(triplets_count)  # 4

    arr = [1, 3, 9, 9, 27, 81]
    r = 3
    triplets_count = count_triplets(arr, r)
    print(triplets_count)  # 6

    arr = [1] * 100
    r = 1
    triplets_count = count_triplets(arr, r)
    print(triplets_count)  # 161700

    arr = [1237] * 100000
    r = 1
    triplets_count = count_triplets(arr, r)
    print(triplets_count)  # 166661666700000 # memory error
