#
# z =100
# for i in range(1 , z):
#     y= i
#     x = y //2
#     while x > 1:
#         if y % x == 0:
#          #   print(y , 'ma czynnik', x)
#             break
#         x -=1
#     else:
#         print(y, "jest liczbą pierwszą")


def primeNumber(*numbers):
    for number in numbers:
        x = number//2
        while x >1:
            if number % x == 0:
                print(number, "dzieli się przez",x)
                break
            x -=1
        else:
            print(number, "jest liczbą pierwszą")

primeNumber(13)
primeNumber(13.0)
primeNumber(15)
primeNumber(15.0)

primeNumber(15.0,12,1,100,12.5)
