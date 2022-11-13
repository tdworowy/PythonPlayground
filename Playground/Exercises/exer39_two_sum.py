from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    if len(nums) == 2:
        return [0, 1]
    checked = {}
    for i, number in enumerate(nums):
        r = target - nums[i]
        if r in checked:
            return [i, checked[r]]
        else:
            checked[number] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))
