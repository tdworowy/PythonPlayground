class First():
    def message(self):
        print("In first class")


class Second(First):
    def message(self):
        super().message()
        print("In Second class")


class Third(Second):
    def message(self):
        super(Third, self).message()  # optional arguments
        print("In Third Class")


if __name__ == '__main__':
    x = Second()
    x.message()
    print('_' * 10)
    y = Third()
    y.message()

    super(Third, y).message()  # works
