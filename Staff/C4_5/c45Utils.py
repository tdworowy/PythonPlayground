

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

    def getValues(self):
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

    def displayValues(self):
        values = self.getValues()
        for atr in self.attributes:
            print(atr, ":")
            for dictionary in  values:
               try:
                 print(dictionary[atr])
               except  KeyError:
                   continue


