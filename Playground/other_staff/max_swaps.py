from random import shuffle

if __name__ == "__main__":
    result = {}
    for i in range(1, 10000):
        A = list(range(1, 11))
        shuffle(A)
        shuffled = A[:]
        swaps = 0
        for i in range(len(A)):

            min_idx = i
            for j in range(i + 1, len(A)):
                if A[min_idx] > A[j]:
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
            swaps += 1
        result[swaps] = shuffled

    max_swaps = max(result.keys())
    print(result[max_swaps])
