class Limiter:
    __slots__ = ["age", "name", "job"]


if __name__ == "__main__":
    x = Limiter()
    x.age = 12
    print(x.age)
    # print(x.name)
    x.spam = "Spam"
