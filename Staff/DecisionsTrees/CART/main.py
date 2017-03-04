import csv

from Staff.DecisionsTrees.CART.DecisionsTreesUtils2 import utils
from Staff.DecisionsTrees.CART.tree import cart
from Staff.DecisionsTrees.data.dataUtils import getDataPath


def test():
    cart_ = cart()
    utils_=utils()
    rows = []
    with open(getDataPath() + "\\exampleData.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)
            rows.append(row)
    tree = cart_.build_tree(utils_.convertValuesToNumeric(rows), 1, 1) #wont work becouse of  convertValuesToNumeric output
    cart_.print_tree(tree)


if __name__ == "__main__":
    test()