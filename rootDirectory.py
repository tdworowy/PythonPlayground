import os


def getRootDirectory():
    return  os.path.dirname(os.path.abspath(__file__))

print(getRootDirectory())