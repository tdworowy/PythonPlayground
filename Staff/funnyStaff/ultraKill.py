import csv
import os

#try kill all processes

def ultraKill():
    os.system("tasklist /FO CSV > taskList.csv")
    with open("taskList.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            os.system("TaskKill /PID " + str(row[1]))


if __name__ == "__main__":
    ultraKill()
