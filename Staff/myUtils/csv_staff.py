import csv

from Staff.Utils import rootDirectory


def getFirstColumn(sep,file):
    f2 =open(rootDirectory()+'//file.csv','w')
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(row[0])
            f2.write(row[0]+";")

getFirstColumn(";","D:\Google_drive\Studia_magister\Semestr3\TextMining\dane\coffee_tweets.csv")