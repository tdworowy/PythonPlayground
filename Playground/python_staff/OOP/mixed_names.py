class MixedNames:
    data = "spam"

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


if __name__ == "__main__":
    a = MixedNames(1)
    b = MixedNames(2)

    a.display()
    b.display()
