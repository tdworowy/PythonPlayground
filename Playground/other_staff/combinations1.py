from itertools import product

if __name__ == "__main__":
    i = 0
    for x in product([0, 1], repeat=6):
        print(x)
        if x.count(1) == x.count(0):
            i += 1
    print(i)
