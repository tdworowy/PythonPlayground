class Class:
    def method(self):
        print("I'm a method")


obj = Class()

x = obj.method
x()

Class.method(obj)