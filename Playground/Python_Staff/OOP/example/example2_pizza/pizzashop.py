from Playground.Python_Staff.OOP.example.example2_pizza.empoyees import Server, PizzaRobot


class Customer:
    def __init__(self,name):
        self.name = name

    def order(self,server):
        print(self.name , "order from ",server)

    def pay(self,server):
        print(self.name ,"pay for order ", server)

class Oven:
    def bake(self):
        print("over is bake")

class PizzaShop:
    def __init__(self):
        self.server = Server('ServerName1')
        self.chef = PizzaRobot('Robert')
        self.over = Oven()

    def order(self,name):
        customer= Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.over.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order("Homer")
    print('....')
    scene.order('Bojack')