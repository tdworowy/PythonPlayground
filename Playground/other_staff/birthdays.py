from random import randrange

if __name__ == "__main__":
    duplicates_count = 0
    people_count = 40
    for i in range(10000):
        days_set = set([randrange(1, 365) for x in range(1, people_count)])
        if len(days_set) < people_count-1:
            duplicates_count += 1

    print(duplicates_count)
