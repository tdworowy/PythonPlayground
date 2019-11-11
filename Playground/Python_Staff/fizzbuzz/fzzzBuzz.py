def fizzbuzz1():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzbuzz2():
    s = ""
    for i in range(1, 100):
        if i % 3 == 0: s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        else:
            s += str(i)
    return s



def fizzbuzz3():
    for i in range(1, 100):
        print("Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i)



def fizzbuzz4():
    fizzbuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i
                in range(1, 100)]
    return fizzbuzz


def fizzbuzz5():
    fizzbuzz = ("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i
                in range(1, 100))
    return fizzbuzz

def fizzbuzz6():
    fizzbuzz = map(
        (lambda i: "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i),
        range(1, 100))
    print(list(fizzbuzz))


def fizzbuzz7():
    print(list(map(
        (lambda i: "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i),
        range(1, 100))))


def fizzbuzz8():
    print(["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i for i in range(1, 100)])


def fizzbuzz9():
    print(list(map((lambda i: "Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i), range(1, 100))))

if __name__ == "__main__":
    fizzbuzz1()
    print(fizzbuzz2())
    fizzbuzz3()
    print(fizzbuzz4())
    print(list(fizzbuzz5()))

    fizzbuzz6()
    fizzbuzz7()
    fizzbuzz8()
    fizzbuzz9()
