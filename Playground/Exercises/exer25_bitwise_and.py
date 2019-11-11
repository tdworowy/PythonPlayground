from itertools import combinations

def bitwise_and(n,k):
    result = []
    for combination in combinations(range(1, n+1), 2):
        bit_and = combination[0] & combination[1]
        if bit_and < k:
            result.append(bit_and)
    return max(result)

def bitwise_and(n,k):
    return max([(combination[0] & combination[1]) for combination in combinations(range(1, n+1), 2) if combination[0] & combination[1] < k ])


def bitwise_and(n,k):
    return k - 1 if ((k - 1) | k) <= n else k - 2
if __name__ == "__main__":
    print(bitwise_and(5,2))