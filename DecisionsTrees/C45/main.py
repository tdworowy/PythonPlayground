import csv

from DecisionsTrees.C45.c45 import c45Algorithm
from DecisionsTrees.data.dataUtils import getDataPath


def main():
    rows = []
    with open(getDataPath()+"\\exampleData.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)
            rows.append(row)
    c45 = c45Algorithm(rows,"atr3")
    c45.check()


if __name__ == "__main__":
    main()
