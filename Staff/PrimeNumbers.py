
z =100000
for i in range(1 , z):
    y= i
    x = y //2
    while x > 1:
        if y % x == 0:
         #   print(y , 'ma czynnik', x)
            break
        x -=1
    else:
        print(y, "jest liczbą pierwszą")