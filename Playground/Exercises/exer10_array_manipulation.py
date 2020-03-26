import threading

n = 5
queries = [[1, 2, 100],
           [2, 5, 100],
           [3, 4, 100]]

n2 = 100000


def update_array(array, i, j):
    array[i] = array[i] + j


def array_manipulation(n, queries):
    array = [0] * n
    threads = []
    for query in queries:
        for i in range(query[0] - 1, query[1]):
            thread = threading.Thread(target=update_array,
                                      args=(array, i, query[2]),
                                      )
            thread.start()
    [thread.join() for thread in threads]

    return max(array)


if __name__ == "__main__":
    print(array_manipulation(n, queries))
