class ex1:
    x = 1
if __name__ == '__main__':


    a =ex1()
    b =ex1()

    a.x = 10

    print(a.x)
    print(b.x)

    ex1.x = 11

    print(a.x)
    print(b.x)