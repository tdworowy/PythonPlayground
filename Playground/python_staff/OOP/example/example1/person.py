from Playground.my_utils.classTools_.class_tools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, precent):
        self.pay = self.pay * (1 + precent / 100)


class Manager(Person):

    def __init__(self, name, pay=0):
        Person.__init__(self, name, "Manager", pay)

    def give_raise(self, precent, bonus=10):
        Person.give_raise(self, precent + bonus)


class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'Manager', pay)

    def giveRaise(self, precent, bonus=10):
        self.person.give_raise(precent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


def test1():
    homer = Person("Homer Simposon")
    boJack = Person("BoJack Horseman ", job="Actor", pay=1000)
    rick = Manager("Rick Sanches", 20000)
    print(homer)
    print(boJack)
    print(rick)
    print(homer.last_name(), boJack.last_name())
    boJack.give_raise(11)
    rick.give_raise(11)
    print(boJack)
    print(rick)

    team = Department(boJack, rick)
    team.addMember(homer)
    team.giveRaises(10)
    team.showAll()


if __name__ == '__main__':
    test1()
