class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = 0

    def compute_difference(self):
        min_ = min(self.__elements)
        max_ = max(self.__elements)
        self.maximum_difference = abs(min_ - max_)