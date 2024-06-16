if __name__ == "__main__":

    def f1():
        x = 88

        def f2():
            print(x)

        return f2

    action = f1()
    action()

    def maker(N):
        def action(X):
            return X**N

        return action

    f1 = maker(2)
    f2 = maker(3)
    print(f1)
    print(f2)

    print(f1(2))
    print(f2(3))

    def function(x="spam"):
        print(x)

    function()
    function("Dupa")
    function(2)

    def f1():
        x = 88
        f2(x)

    def f2(x):
        print(x)

    f1()
