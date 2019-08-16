import csv

from rootDirectory import getRootDirectory


def get_first_column(file,sep=';'):
    f2 = open(getRootDirectory() + '//file.csv', 'w')
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=sep)
        for row in reader:
            print(row[0])
            f2.write(row[0] + ";")


get_first_column("D:\Google_drive\Studia_magister\Semestr3\TextMining\dane\coffee_tweets.csv")
