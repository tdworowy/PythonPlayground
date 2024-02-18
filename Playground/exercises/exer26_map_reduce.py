from collections import OrderedDict


class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value)

    def execute(self, data):
        for record in data:
            self.mapper(record)

        for key in self.intermediate:
            self.reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print("{\"key\":\"" + item[0] + "\",\"value\":\"" + str(item[1]) + "\"}")

    def mapper(self, record):
        v1, v2 = record.split()
        self.emit_intermediate(v1, v2)
        mapReducer.emit_intermediate(v2, v1)

    def reducer(self, key, list_of_values):
        self.emit([key, len(list_of_values)])


if __name__ == '__main__':
    inputData = ["Joe Sue", "Sue Phi", "Phi Joe", "Phi Alice"]
    mapReducer = MapReduce()
    mapReducer.execute(inputData)
