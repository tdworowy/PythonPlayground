

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
        values = []
        for row in self.rawData:
            for data in row:
                if(data not in values): values.append(data)
        return values