import csv

from Decisions_Trees.C45.c45 import C45Algorithm
from Decisions_Trees.data.dataUtils import getDataPath


def main():
    rows = []
    with open(getDataPath()+"\\exampleData.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)
            rows.append(row)
    c45 = C45Algorithm(rows, "atr3")
    c45.check()


if __name__ == "__main__":
    main()
