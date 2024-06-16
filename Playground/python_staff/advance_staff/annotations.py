def f(ham: str, eggs: str = "eggs") -> str:
    pass


if __name__ == "__main__":
    print(f.__annotations__)
    f(1, 2)  # annotations is just information
