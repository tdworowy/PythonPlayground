class NewProps:

    def __init__(self):
        self._age = 40

    def get_age(self):
        return self._age

    def set_age(self, value):
        print("Set age: ", value)
        self._age = value

    age = property(get_age, set_age, None, None)


if __name__ == "__main__":
    x = NewProps()
    print(x.age)
    x.age = 2
    print(x.age)
