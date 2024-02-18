import timeit

if __name__ == "__main__":
    for e in range(301, 324):
        x = float(f"1.234e-{e}")
        t = timeit.Timer(lambda: x * 2.1)
        print(x.hex(), t.timeit(number=1000000))
