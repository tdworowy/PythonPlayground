import os


def get_root_directory():
    return os.path.dirname(os.path.abspath(__file__))


print(get_root_directory())
