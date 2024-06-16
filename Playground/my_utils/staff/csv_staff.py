import csv

from Playground.root_directory import get_root_directory


def get_first_column(file, sep=";"):
    f2 = open(get_root_directory() + "//file.csv", "w")
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=sep)
        for row in reader:
            print(row[0])
            f2.write(row[0] + ";")
