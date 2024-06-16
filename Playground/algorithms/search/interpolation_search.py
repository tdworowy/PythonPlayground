from random import randint

from Playground.my_utils.staff.timer3 import timer3


@timer3
def interpolation_search(list_: list, item):
    """list_ must be sorted"""
    idx_0 = 0
    idx_n = len(list_) - 1

    while idx_0 <= idx_n and list_[idx_0] <= item <= list_[idx_n]:
        mid_point = idx_0 + int(
            (
                (float(idx_n - idx_0) / (list_[idx_n] - list_[idx_0]))
                * (item - list_[idx_0])
            )
        )
        if list_[mid_point] == item:
            return True
        if list_[mid_point] < item:
            idx_0 = mid_point + 1
    return False


if __name__ == "__main__":
    list_ = [randint(0, 10000) for x in range(100000)]
    list_.sort()
    print(interpolation_search(list_, 500))
