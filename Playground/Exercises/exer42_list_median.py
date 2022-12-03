from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()
    center = len(nums) // 2
    if len(nums) % 2 != 0:
        return nums[center]
    else:
        return (nums[center - 1] + nums[center]) / 2


if __name__ == "__main__":
    num1 = [1, 2]
    num2 = [3, 4]
    expected_median = 2.5
    print(find_median_sorted_arrays(num1, num2))
    print(find_median_sorted_arrays([1, 2], [3]))
    print(find_median_sorted_arrays([0, 0], [0, 0]))
