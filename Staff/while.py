x = "test"*10
while x:
    print(x)
    x = x[1:]


x = 100
while x:
    x -= 1
    print(x)
    if x % 2 != 0: continue
    print(x, end=' ')