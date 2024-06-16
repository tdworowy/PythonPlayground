class Name:
    "Documentation"

    def __get__(self, instance, owner):
        print("get...")
        return instance._name

    def __set__(self, instance, value):
        print("set name as %s" % value)
        instance._name = value

    def __delete__(self, instance):
        print("delete...")
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name

    name = Name()


if __name__ == "__main__":
    bob = Person("Name test1")
    print(bob.name)
    bob.name = "Name test2"
    print(bob.name)
    del bob.name
