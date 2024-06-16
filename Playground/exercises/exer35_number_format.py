def print_formatted(number):
    w = len(f"{number:b}")
    for n in range(1, number + 1):
        print(f"{n:={w}} {n:={w}o} {n:={w}X} {n:={w}b}")


if __name__ == "__main__":
    print_formatted(99)
