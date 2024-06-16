def prime_number(*numbers):
    for number in numbers:
        x = number // 2
        while x > 1:
            if number % x == 0:
                print(number, "divide by", x)
                break
            x -= 1
        else:
            print(number, "is prime")


if __name__ == "__main__":
    prime_number(13)
    prime_number(13.0)
    prime_number(15)
    prime_number(15.0)

    prime_number(15.0, 12, 1, 100, 12.5)
