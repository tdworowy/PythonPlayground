
from DecisionsTrees.C45.DecisionsTreesUtils import dtUtils


class c45Algorithm:
    def __init__(self,data, class_):
        self.data = data
        self.class_ = class_
        self.dtUtils = dtUtils(data)

    def check(self):
        print("Attributes: ",self.dtUtils .getAttributes())
        print("Class: ",self.class_)
        print(self.dtUtils.checkClass(self.class_))
        print("Possible values: ")
        print(self.dtUtils.getValuesPerAttribute())
        self.dtUtils.displayValues()
        print("Values count: ", self.dtUtils.getValueCount())
        print("Values to numeric")
        self.dtUtils.prettyList(list(self.dtUtils.convertValuesToNumeric()))
#TODO lot of work