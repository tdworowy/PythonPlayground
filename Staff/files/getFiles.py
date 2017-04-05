from os import listdir
from os.path import isfile, join

from Staff.rootDirectory import getRootDirectory


def getAllFIles(paths):
        fout = open(getRootDirectory() + "\\files.txt", "a")

        folders= []
        for path in paths:
            try:
                 onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
                 folders.extend([join(path,f) for f in listdir(path) if not isfile(join(path, f))])
                 print(str(onlyfiles))
                 print(str(folders))
                 fout.write(str(onlyfiles)+"\n")
                 fout.flush()

            except:
                continue
        getAllFIles(folders)

getAllFIles(["D:\Google_drive\\"])