def count_moves(tower_size):
    return pow(2, tower_size) - 1


if __name__ == "__main__":
    print(count_moves(64))
