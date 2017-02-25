
from Staff.C4_5.c45Utils import c45U


class c45Algorithm:
    def __init__(self,data, class_):
        self.data = data
        self.class_ = class_
        self.c45Util = c45U(data)

    def check(self):
        print("Attributes: ",self.c45Util .getAttributes())
        print("Class: ",self.class_)
        print(self.c45Util.checkClass(self.class_))
        print("Possible values: ")
        print(self.c45Util.getValuesPerAttribute())
        self.c45Util.displayValues()
        print("Values count: ", self.c45Util.getValueCount())
        print("Values to numeric")
        self.c45Util.prettyList(list(self.c45Util.convertValuesToNumeric()))
#TODO lot of work