from typing import List


def maximum_bags(capacity: List[int], rocks: List[int], additional_rocks: int) -> int:
    full_bags_count = 0
    not_full_bags = []
    for cap, rocks in zip(capacity, rocks):
        if cap == rocks:
            full_bags_count += 1
        else:
            not_full_bags.append(cap - rocks)

    not_full_bags.sort()
    for i in range(len(not_full_bags)):
        if not_full_bags[i] <= additional_rocks:
            full_bags_count += 1
            additional_rocks -= not_full_bags[i]
        else:
            break
    return full_bags_count


if __name__ == "__main__":
    print(maximum_bags([2, 3, 4, 5], [1, 2, 4, 4], 2))  # 3
    print(maximum_bags([10, 2, 2], [2, 2, 0], 100))  # 3
    print(maximum_bags([91, 54, 63, 99, 24, 45, 78], [35, 32, 45, 98, 6, 1, 25], 17))  # 2
    print(maximum_bags(
        [54, 18, 91, 49, 51, 45, 58, 54, 47, 91, 90, 20, 85, 20, 90, 49, 10, 84, 59, 29, 40, 9, 100, 1, 64, 71, 30, 46,
         91],
        [14, 13, 16, 44, 8, 20, 51, 15, 46, 76, 51, 20, 77, 13, 14, 35, 6, 34, 34, 13, 3, 8, 1, 1, 61, 5, 2, 15, 18],
        77))  # 13
