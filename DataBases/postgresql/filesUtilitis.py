import os
from os import listdir
from os.path import isfile, join

import psycopg2


class filesUtllitis():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + "\Data\\"
        self.pathNew = os.path.dirname(os.path.abspath(__file__)) + "\\newData\\"
        self.pathExp = os.path.dirname(os.path.abspath(__file__)) + "\ExportedData\\"


    def fileToStream(self, file,path):

        fullPath = path + file

        print("Full path:", fullPath)

        with open(fullPath, "rb") as imageFile:
            byte = psycopg2.Binary(imageFile.read())
        return byte

    def getFiles(self,path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles



    def removeFile(self, file):
        os.remove(self.path + file)

    def getPath(self):
        return  self.path

    def getPathNew(self):
        return self.pathNew

    def getPathExp(self):
        return self.pathExp