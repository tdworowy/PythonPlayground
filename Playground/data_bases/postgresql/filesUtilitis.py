import os
from os import listdir
from os.path import isfile, join

import psycopg2


class FilesUtils:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + "\Data\\"
        self.new_path = os.path.dirname(os.path.abspath(__file__)) + "\\newData\\"
        self.export_path = (
            os.path.dirname(os.path.abspath(__file__)) + "\ExportedData\\"
        )

    def file_to_stream(self, file, path):
        full_path = path + file

        print("Full path:", full_path)

        with open(full_path, "rb") as imageFile:
            byte = psycopg2.Binary(imageFile.read())
        return byte

    def get_files(self, path):
        only_files = [f for f in listdir(path) if isfile(join(path, f))]
        return only_files

    def remove_file(self, file):
        os.remove(self.path + file)

    def get_path(self):
        return self.path

    def get_new_path(self):
        return self.new_path

    def get_path_exp(self):
        return self.export_path
