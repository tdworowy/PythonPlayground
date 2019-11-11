class Class:
    def method(self):
        print("I'm a method")
if __name__ == '__main__':

    obj = Class()

    x = obj.method
    x()

    Class.method(obj)