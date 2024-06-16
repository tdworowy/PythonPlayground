if __name__ == "__main__":
    number = 10
    while 1:
        if number / 57 == int(str(number)[1:]):
            print(number)
            break
        else:
            number = number + 1
