class Descriptor:
    "Documentation abc 123"

    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')

    def __set__(self, instance, value):
        print(self, instance, value, sep='\n')


class Subject:
    attr = Descriptor()


if __name__ == '__main__':
    x = Subject()
    x.attr
    x.attr = "Test"
