import pandas as pd


class DTUtils:
    def __init__(self, data):
        self.data = data
        self.attributes = self.data[0]
        self.rawData = self.data[1:]

    def get_attributes(self):
        return self.attributes

    def check_class(self, class_):
        if class_ in self.get_attributes():
            return "Correct class"
        else:
            return "incorrect Class"

    def get_values_per_attribute(self):
        values_per_attribute = []
        index = 0
        for atr in self.attributes:
            for row in self.rawData:
                value = row[index]
                dic = dict([(atr, value)])
                if dic not in values_per_attribute:
                    values_per_attribute.append(dic)
            index += 1
        return values_per_attribute

    def get_valuese(self):
        values = []
        index = len(self.get_attributes())
        for i in range(index):
            for row in self.rawData:
                value = row[i]
                if value not in values:
                    values.append(value)

        return values

    def display_values(self):
        values = self.get_values_per_attribute()
        for atr in self.attributes:
            print(atr, ":")
            for dictionary in values:
                try:
                    print(dictionary[atr])
                except KeyError:
                    continue

    def get_value_count(self):
        values = self.get_valuese()
        values_count = []
        for v in values:
            value_count = sum(x.count(v) for x in self.rawData)
            values_count.append((v, value_count))
        return values_count

    def convert_values_to_numeric(self):
        s = map(pd.Series, self.rawData)
        return map(pd.get_dummies, s)

    def pretty_list(self, list_):
        for item in list_:
            print(item)
