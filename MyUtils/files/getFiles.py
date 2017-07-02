import sys
from os import listdir
from os.path import isfile, join

from rootDirectory import getRootDirectory

sys.setrecursionlimit(10000)
def getAllFIles(paths):
       folders= []
       for path in paths:
            try:
                 onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
                 folders.extend([join(path,f) for f in listdir(path) if not isfile(join(path, f))])
                 print(str(onlyfiles))
                 temp = path.replace(":","_")
                 temp = temp.replace("\\", "_")
                 fout = open(getRootDirectory() + "\\files\\" + temp+".txt", "a")
                 fout.write(str(onlyfiles)+"\n")
                 fout.flush()

            except:
                continue
       getAllFIles(folders)

if __name__ == "__main__":
    getAllFIles([getRootDirectory(),"files"])


