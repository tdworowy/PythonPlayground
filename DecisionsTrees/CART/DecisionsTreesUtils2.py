from _csv import reader


class Utils:
    def __init__(self, ):
        print("")

    def ginit_index(self, groups, class_values):
        ginit = 0.0
        for class_value in class_values:
            for group in groups:
                size = len(group)
                if size == 0: continue
                proportion = [row[-1] for row in group].count(class_value) / float(size)
                ginit += (proportion * (1.0 - proportion))
        return ginit

    @staticmethod
    def test_split(index, value, data_set):
        left, right, = list(), list()
        for row in data_set:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def get_split(self, data_set):
        class_values = list(set(row[-1] for row in data_set))
        b_index, b_value, b_score, b_groups = 999, 999, 999, None
        for index in range(len(data_set[0]) - 1):
            for row in data_set:
                groups = self.test_split(index, row[index], data_set)
                gini = self.ginit_index(groups, class_values)
                print('X%d < %.3f Gini=%.3f' % ((index + 1), row[index], gini))
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        return {'index': b_index, 'value': b_value, 'groups': b_groups}

    @staticmethod
    def load_csv(filename):
        file = open(filename, "r")
        lines = reader(file)
        data_set = list(lines)
        return data_set

    @staticmethod
    def str_column_to_float(data_set, column):
        for row in data_set:
            row[column] = float(row[column].strip())


def test():
    utils_ = Utils()
    giniIndex1 = utils_.ginit_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1])
    giniIndex2 = utils_.ginit_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1])
    print(giniIndex1)
    print(giniIndex2)

    data_set = [[2.771244718, 1.784783929, 0],
               [1.728571309, 1.169761413, 0],
               [3.678319846, 2.81281357, 0],
               [3.961043357, 2.61995032, 0],
               [2.999208922, 2.209014212, 0],
               [7.497545867, 3.162953546, 1],
               [9.00220326, 3.339047188, 1],
               [7.444542326, 0.476683375, 1],
               [10.12493903, 3.234550982, 1],
               [6.642287351, 3.319983761, 1]]
    split = utils_.get_split(data_set)
    print('Split: [X%d < %.3f]' % ((split['index'] + 1), split['value']))


if __name__ == "__main__":
    test()
