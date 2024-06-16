class Indexer1:
    def __getitem__(self, item):
        return item**2


class Indexer2:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        print("getitem: ", item)
        return self.data[item]

    def __setitem__(self, key, value):
        print("setitem: key: ", key)
        print("setitem: value: ", value)
        data_length = len(self.data)
        if data_length >= key:
            self.data[key] = value
        else:
            for i in range(key - data_length):
                self.data.append(None)
            else:
                self.data.append(value)


if __name__ == "__main__":

    X = Indexer1()
    print(X[2])

    Y = Indexer2([5, 6, 7, 8, 9])
    print(Y[0])
    print(Y[-1])

    print(Y[2:4])

    Y[4] = 10
    Y[1] = 11

    Y[14] = 14

    print(Y[0:])

    Y[20] = 20

    print(Y[0:])

    for i in Y:
        print(i)
