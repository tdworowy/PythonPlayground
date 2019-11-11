def power(values):
    for value in values:
        print("Power : %s" % value)
        yield value

def adder(values):
    for value in values:
        print("add to %s" % value)
        if value %2 ==0:
            yield  value +3
        else:
            yield  value +2

if __name__ == "__main__":


    l = [1,2,4,6,17,12,5,7]

    x = adder(power(l))

    for i in l:
        print(next(x))