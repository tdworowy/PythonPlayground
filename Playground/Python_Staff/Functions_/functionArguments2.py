if __name__ == "__main__":

    def f(a,b,c,d): print(a,b,c,d)

    args = (1,2)
    args +=(3,4)

    f(*args)

    args = {'a':1,'b':2,'c':3,'d':4}
    f(**args)


    def f(a,*b,c): print(a,b,c)

    f(1,2,c=3)
    f(1,2,3,4,5,6,c='C')

    def f(a,*,b,c): print(a,b,c)

    f(1,b="B",c=3)