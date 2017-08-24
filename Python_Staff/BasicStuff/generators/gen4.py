def gen():
    while True:
        x = (yield)
        print(x)

y = gen()
next(y)
y.send("Test")
# next(y)
y.send(1)
y.send(2)
y.send("Dupa")