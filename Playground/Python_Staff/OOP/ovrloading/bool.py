class F_alse:
    def __bool__(self): return False


class Length:
    def __len__(self): return 10


if __name__ == '__main__':

    x = F_alse()
    if not x:  print("False")
    x = Length()
    print(len(x))
