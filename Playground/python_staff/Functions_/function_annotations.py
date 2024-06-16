def func(a: "spam", b: (1, 10), c: float) -> int:
    return a + b + c


if __name__ == "__main__":
    print(func(1, 2, 3))
    print(func.__annotations__)
