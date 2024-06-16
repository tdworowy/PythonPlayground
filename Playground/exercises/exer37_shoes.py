from collections import Counter


class shoeShop:
    def __init__(self, shoes_sizes: list):
        self.shoes_sizes = Counter(shoes_sizes)
        self.earnings = 0

    def sale(self, size: int, price: int):
        if self.shoes_sizes[size]:
            self.shoes_sizes[size] -= 1
            self.earnings += price


if __name__ == "__main__":
    number_of_shoes = 10
    shoes_sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    number_of_customers = 6
    demands = [(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)]
    shoe_shop = shoeShop(shoes_sizes)
    for demand in demands:
        shoe_shop.sale(*demand)
    print(shoe_shop.earnings)  # 200
