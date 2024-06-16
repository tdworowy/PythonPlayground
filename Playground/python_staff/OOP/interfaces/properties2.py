class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        "DOCUMENTATION: Property name documentation"
        print("Get...")
        return self._name

    @name.setter
    def name(self, name):
        print("Set...")
        self._name = name

    @name.deleter
    def name(self):
        print("Delete...")
        del self._name


if __name__ == "__main__":

    homer = Person("Homer Simpson")
    print(homer.name)
    homer.name = "Homer2"
    print(homer.name)
    del homer.name
    try:
        print(homer.name)
    except Exception as ex:
        print(ex)

    print(Person.name.__doc__)
