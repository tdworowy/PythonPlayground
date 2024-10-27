def is_pair_amicable(a: int, b: int) -> bool:
    a_divisors = [i for i in range(a - 1, 0, -1) if a % i == 0]
    b_divisors = [i for i in range(b - 1, 0, -1) if b % i == 0]
    return sum(a_divisors) == b and sum(b_divisors) == a


if __name__ == "__main__":
    print(is_pair_amicable(220, 284))
