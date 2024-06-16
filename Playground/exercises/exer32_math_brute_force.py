# take to mach time
if __name__ == "__main__":
    for i in range(9999999999999, 1, -1):
        number = [char for char in str(i)]
        number[0], number[-1] = number[-1], number[0]
        number = int("".join(number))
        if number == i * 2:
            print(i)
            break
