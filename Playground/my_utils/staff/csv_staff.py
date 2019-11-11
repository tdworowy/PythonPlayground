import csv

from Playground.rootDirectory import get_root_directory


def get_first_column(file,sep=';'):
    f2 = open(get_root_directory() + '//file.csv', 'w')
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=sep)
        for row in reader:
            print(row[0])
            f2.write(row[0] + ";")
if __name__ == '__main__':

    get_first_column("D:\Google_drive\Studia_magister\Semestr3\TextMining\dane\coffee_tweets.csv")
