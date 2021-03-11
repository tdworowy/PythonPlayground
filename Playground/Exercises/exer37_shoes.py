from collections import Counter


# it is ugly
def count_earnings(shoes_sizes: list, demands: list):
    shoes_sizes = Counter(shoes_sizes)
    indexes = []
    earnings = 0
    for size in shoes_sizes:
        shou_count = shoes_sizes[size]
        for count in range(shoes_sizes[size]):
            for i, demand in enumerate(demands):
                if size == demand[0] and i not in indexes and shou_count != 0:
                    indexes.append(i)
                    earnings += demand[1]
                    shou_count -= 1
    return earnings


if __name__ == '__main__':
    number_of_shoes = 10
    shoes_sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    number_of_customers = 6
    demands = [
        (6, 55),
        (6, 45),
        (6, 55),
        (4, 40),
        (18, 60),
        (10, 50)
    ]
    print(count_earnings(shoes_sizes, demands))
