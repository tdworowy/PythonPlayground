import time

from PIL import Image

from Data_bases.postgresql.filesUtilitis import FilesUtils
from Data_bases.postgresql.utils import random_string


class Display:
    def __init__(self):

        self.fu = FilesUtils()
        self.path = self.fu.get_path()

    def display_picture_from_db(self, memory_view):
        try:
            x = random_string(30)
            temp_file_name = 'tempFile' + x + '.jpg'
            temp_file_path = self.path + temp_file_name
            byte = bytes(memory_view[0][0])  # memoryView to lista krotek obiektów memoryview
            print(byte)
            open(temp_file_path, 'wb').write(byte)
            self.image = Image.open(temp_file_path).show()


        except Exception as ex:
            print(ex)

        finally:
            time.sleep(2)
            self.fu.remove_file(temp_file_name)

    def display_pictures_fom_db(self, memory_views):

        for view in memory_views:
            try:

                input("press any key to display next picture: ")
                self.display_picture_from_db(view)
                time.sleep(2)
                del self.image
            except Exception as ex:
                print(ex)

    def display_pictures_via_path(self, paths):
        for path in paths:
            try:
                input("press any key to display next picture: ")
                self.image = Image.open(path[0][0], 'r').show()
            except Exception as ex:
                print(ex)

            finally:
                time.sleep(2)
                del self.image
