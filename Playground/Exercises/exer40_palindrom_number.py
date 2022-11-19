def is_pal_until(num: int, dup_num: list) -> bool:
    if 0 <= num < 10:
        return num == (dup_num[0]) % 10
    if not is_pal_until(num // 10, dup_num):
        return False
    dup_num[0] = dup_num[0] // 10
    return num % 10 == (dup_num[0]) % 10


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    dup_num = [x]
    return is_pal_until(x, dup_num)


if __name__ == "__main__":
    print(is_palindrome(121))
    print(is_palindrome(122))

