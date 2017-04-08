class Person:
    def __init__(self,name,job=None ,pay=0):
        self.name  = name
        self.job = job
        self.pay= pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,precent):
        self.pay  =self.pay * (1+precent/100)

    def __str__(self):
        return '[Person : %s, Job: %s , Pay: %s]' % (self.name, self.job,self.pay)


class Manager(Person):

    def __init__(self,name,pay=0):
        Person.__init__(self,name,"Manager",pay)

    def giveRaise(self,precent,bonus=10):
         Person.giveRaise(self,precent + bonus)


class Manager2:
    def __init__(self,name,pay):
        self.person = Person(name , 'Manager',pay)
    def giveRaise(self,precent,bonus=10):
        self.person.giveRaise(precent + bonus)

    def __getattr__(self, attr):
        return  getattr(self.person,attr)
    def __str__(self):
        return str(self.person)


class Department:
    def __init__(self,*args):
        self.members = list(args)
    def addMember(self,person):
        self.members.append(person)

    def giveRaises(self,percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


def test1():
    homer = Person("Homer Simposon")
    boJack = Person("BoJack Horseman ",job="Actor" ,pay=1000)
    rick = Manager("Rick Sanches",20000)
    print(homer)
    print(boJack)
    print(rick)
    print(homer.lastName() , boJack.lastName())
    boJack.giveRaise(11)
    rick.giveRaise(11)
    print(boJack)
    print(rick)

    team = Department(boJack,rick)
    team.addMember(homer)
    team.giveRaises(10)
    team.showAll()

if __name__ == '__main__':
    test1()