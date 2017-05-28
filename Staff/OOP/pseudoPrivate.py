class c1:
    def __init__(self,x):
        self.__X = x

class c2:
    def __init__(self,x):
        self.__X = x


class c3(c1,c2):
  def  __init__(self,x,y):
      c1.__init__(self,x)
      c2.__init__(self,y)

if __name__ == "__main__":
    y = c3(1,2)
    print(y.__dict__)