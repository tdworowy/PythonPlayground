
from Staff.C4_5.c45Utils import c45U


class c45Algorithm:
    def __init__(self,data, calss_):
        self.data = data
        self.calss_ = calss_
        self.c45Util = c45U(data)

    def check(self):
        print("Attributes: ",self.c45Util .getAttributes())
        print("Class: ",self.calss_)
        print(self.c45Util.checkClass(self.calss_))
        print("Possible values: ",self.c45Util.getValues())

