import os

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__)) + "\\script.py"
    path2 = os.path.dirname(os.path.abspath(__file__)) + "\\iteration.txt"
    f2 = open(path2, 'r+')
    i = f2.read()
    i = int(i)
    print("HAHA", i)
    i += 1
    f2.seek(0)
    f2.truncate()

    f2.write(str(i))
    f2.flush()

    os.system("python < " + path)
