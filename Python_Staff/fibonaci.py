def fib1():
    a,b =0,1
    while 1:
        yield b
        a,b =b,a+b
f = fib1()
for i in range(20):
    print(next(f))

def fib2(count):
    fibo = []
    a, b = 0, 1
    for i in range(count):
        a, b = b, a + b
        fibo.append(b)
    return fibo


print(fib2(20))
