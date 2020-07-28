class rec: pass


if __name__ == '__main__':
    rec.test = "Test1"
    rec.a = 1
    rec.b = 2

    print(rec.test)
    print(rec.a + rec.b)

    x = rec()
    x.test2 = "Test2"

    print(x.test2)
    print(x.test)

    print(rec.__dict__.keys())
    print(x.__dict__.keys())
