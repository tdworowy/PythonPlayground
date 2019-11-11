import sys
from os import listdir

from os.path import isfile, join

from rootDirectory import get_root_directory

sys.setrecursionlimit(10000)


def get_all_files(paths):
    folders = []
    for path in paths:
        try:
            only_files = [f for f in listdir(path) if isfile(join(path, f))]
            folders.extend([join(path, f) for f in listdir(path) if not isfile(join(path, f))])
            print(str(only_files))
            temp = path.replace(":", "_")
            temp = temp.replace("\\", "_")
            found = open(get_root_directory() + "\\files\\" + temp + ".txt", "a")
            found.write(str(only_files) + "\n")
            found.flush()

        except Exception:
            continue
    get_all_files(folders)


if __name__ == "__main__":
    get_all_files([get_root_directory(), "files"])
