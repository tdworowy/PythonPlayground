import os


def rootDirectory():
    return  os.path.dirname(os.path.abspath(__file__))

print(rootDirectory())