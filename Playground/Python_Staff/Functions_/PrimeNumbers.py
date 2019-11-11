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


def prime_number(*numbers):
    for number in numbers:
        x = number//2
        while x >1:
            if number % x == 0:
                print(number, "dzieli się przez",x)
                break
            x -=1
        else:
            print(number, "jest liczbą pierwszą")

if __name__ == "__main__":
    prime_number(13)
    prime_number(13.0)
    prime_number(15)
    prime_number(15.0)

    prime_number(15.0, 12, 1, 100, 12.5)
