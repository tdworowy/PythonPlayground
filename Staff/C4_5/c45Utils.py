import pandas as pd

class c45U:
    def __init__(self, data):
        self.data = data
        self.attributes = self.data[0]
        self.rawData = self.data[1:]

    def getAttributes(self):
         return self.attributes

    def checkClass(self,class_):
        if(class_ in self.getAttributes()) : return "Correct class"
        else: return "incorrect Class"

    def getValuesPerAttribute(self):
        valuesPerAttribute = []
        index =0
        for atr in self.attributes:
             for row in self.rawData:
                 value = row[index]
                 dic = dict([(atr, value)])
                 if(dic not in valuesPerAttribute):
                     valuesPerAttribute.append(dic)
             index +=1
        return valuesPerAttribute

    def getValuese(self):
        values = []
        index = len(self.getAttributes())
        for i in range(index):
            for row in self.rawData:
                    value = row[i]
                    if (value not in values):
                      values.append(value)

        return values

    def displayValues(self):
        values = self.getValuesPerAttribute()
        for atr in self.attributes:
            print(atr, ":")
            for dictionary in  values:
               try:
                 print(dictionary[atr])
               except  KeyError:
                   continue

    def getValueCount(self):
        values = self.getValuese()
        valuesCount = []
        for v in values:
            valueCount = sum(x.count(v) for x in self.rawData)
            valuesCount.append((v,valueCount))
        return valuesCount


    def getDumies(self):
        s= map(pd.Series,self.rawData)
        return  map( pd.get_dummies,s)


