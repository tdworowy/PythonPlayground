class Indexer:
    def __getitem__(self, item):
        return item ** 2

X = Indexer()
print(X[2])