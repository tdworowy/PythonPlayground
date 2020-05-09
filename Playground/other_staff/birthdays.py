from random import randrange

if __name__ == "__main__":
    duplicates_count = 0
    people_count = 50
    for i in range(10):
        days_set = set([randrange(1, 365) for x in range(1, people_count)])
        # print(days_set)
        if len(days_set) < people_count - 1:
            duplicates_count += 1

    print(duplicates_count)
