class SuperMeta:
    def __call__(self, classname, supers, classdic):
        print("in SuperMeta.call: ", classname, supers, classdic, sep="\n")
        Class = self.__new__(classname, supers, classdic)
        self.__init__(Class, classname, supers, classdic)
        return Class


class SubMeta(SuperMeta):
    def __new__(self, classname, supers, classdic):
        print("in SubMeta.new: ", classname, supers, classdic, sep="\n")
        return type(classname, supers, classdic)

    def __init__(self, Class, classname, supers, classdic):
        print("in SubMeta.init: ", classname, supers, classdic, sep="\n")
        print("...... Object initialized. Class:", list(Class.__dict__.keys()))


class Eggs:
    pass


if __name__ == "__main__":
    print("Create class")

    class Spam(Eggs, metaclass=SubMeta()):  # that example did not work
        data = 1

        def meth(self, arg):
            pass

    print("Add instance")
    X = Spam()
    print("Data: ", X.data)
