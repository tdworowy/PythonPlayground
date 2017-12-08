
from DecisionsTrees.C45.DecisionsTreesUtils import DTUtils


class C45Algorithm:
    def __init__(self,data, class_):
        self.data = data
        self.class_ = class_
        self.dtUtils = DTUtils(data)

    def check(self):
        print("Attributes: ", self.dtUtils .get_attributes())
        print("Class: ",self.class_)
        print(self.dtUtils.check_class(self.class_))
        print("Possible values: ")
        print(self.dtUtils.get_values_per_attribute())
        self.dtUtils.display_values()
        print("Values count: ", self.dtUtils.get_value_count())
        print("Values to numeric")
        self.dtUtils.pretty_list(list(self.dtUtils.convert_values_to_numeric()))
#TODO lot of work