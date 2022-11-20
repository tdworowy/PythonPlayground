from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix([""]))
    print(longest_common_prefix(["a"]))
    print(longest_common_prefix(["ab", "a"]))
    print(longest_common_prefix(["aa", "ab"]))
    print(longest_common_prefix(["aca", "cba"]))
    print(longest_common_prefix(["", ""]))
    print(longest_common_prefix(["", "b"]))
    print(longest_common_prefix(["a", "ac"]))
    print(longest_common_prefix(["baab", "bacb", "b", "cbc"]))
    print(longest_common_prefix(["reflower", "flow", "flight"]))
    print(longest_common_prefix(["aaa", "aa", "aaa"]))
