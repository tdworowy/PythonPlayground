class Squares:
    def __init__(self,start,stop):
        if self.check(start):
            self.value = start -1
            self.stop = stop
        else:
            self.value = 0
            self.stop = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value +=1
        return self.value ** 2

    def check(self,value):
        flag = value >0
        if not flag:
            print("\nstart value must be >0")
        return flag


if __name__ == "__main__":
    for i in Squares(1,20):
        print(i,end=" ")

    for i in Squares(0,20):
        print(i,end=" ")

    for i in Squares(-1, 20):
        print(i, end=" ")