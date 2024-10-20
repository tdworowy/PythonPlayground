from Playground.algorithms.math.sieve_of_eratosthenes import is_prime2


def find_triplets() -> list:
    triplets = []
    temp = []
    for i in range(2, 1000000):
        if not is_prime2(i):
            temp.append(i)
        if len(temp) == 3:
            triplets.append(temp)
            temp = []
    return triplets


if __name__ == "__main__":
    triplets = find_triplets()
    for x in triplets:
        if x[2] - x[1] == 2 and x[1] - x[0] == 2:
            print(x)
