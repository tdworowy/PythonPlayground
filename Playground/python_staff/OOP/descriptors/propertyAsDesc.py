class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instance_type=None):
        if instance is None:
            return self

        if self.fget is None:
            raise AttributeError("Can't get attribute!!")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute!!")

        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Can't delete attribute!!")
        self.fdel(instance)


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("Get...")
        return self._name

    def set_name(self, name):
        print("Set...")
        self._name = name

    def del_name(self):
        print("Delete...")
        del self._name

    name = Property(
        get_name, set_name, del_name, "DOCUMENTATION: Property name documentation"
    )


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
