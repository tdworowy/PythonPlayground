class false:
    def __bool__(self):return  False


class length:
    def __len__(self): return  10

if __name__ == '__main__':

    x = false()
    if not x:  print("False")
    x= length()
    print(len(x))
