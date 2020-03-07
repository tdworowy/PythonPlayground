from random import randrange

if __name__ == "__main__":
    duplicates_count = 0
    for i in range(10000):
        days_set = set([randrange(1, 365) for x in range(1, 51)])
        if len(days_set) < 50:
            duplicates_count += 1

    print(duplicates_count)
