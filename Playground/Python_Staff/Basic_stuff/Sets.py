if __name__ == "__main__":
    set_ = {1, 2, 3}
    print(set_)
    set_ = set([1, 2, 3])
    print(set_)

    set_ = {x ** 2 for x in range(10)}
    print(set_)
