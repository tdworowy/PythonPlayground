class Employee:
    def __init__(self,name,salary = 0):
        self.name = name
        self.salary = salary

    def giveRaise(self,precent):
        self.salary = self.salary + (self.salary * precent)

    def work(self):
        print(self.name, 'Doing staff')

    def __repr__(self):
        return '<Employee: name= %s, salary= %s>' % (self.name, self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,5000)
    def work(self):
        print(self.name , 'Cooking food')


class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,40000)

    def work(self):
        print(self.name, 'Serving client')

class PIzzaRobot(Chef):
    def __init__(self,name):
         Chef.__init__(self,name)

    def work(self):
        print(self.name,'Makeing pizza')

if __name__ == '__main__':
    bob = PIzzaRobot('Robert')
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob)

    for klass in Employee,Chef,Server,PIzzaRobot:
        obj = klass(klass.__name__)
        obj.work()