import csv
import os


# try kill all processes

def ultra_kill():
    os.system("tasklist /FO CSV > taskList.csv")
    with open("taskList.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            x = "TaskKill /PID " + str(row[1]) + " /F"
            print(x)
            os.system(x)


if __name__ == "__main__":
    ultra_kill()
