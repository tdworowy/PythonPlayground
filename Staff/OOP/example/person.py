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
    def giveRaise(self,precent,bonus=10):
         Person.giveRaise(self,precent +bonus)


def test1():
    homer = Person("Homer Simposon")
    boJack = Person("BoJack Horseman ",job="Actor" ,pay=1000)
    rick = Manager("Rick Sanches",'alcoholic',20000)
    print(homer)
    print(boJack)
    print(rick)
    print(homer.lastName() , boJack.lastName())
    boJack.giveRaise(11)
    rick.giveRaise(11)
    print(boJack)
    print(rick)

if __name__ == '__main__':
    test1()