import time

from PIL import Image

from DataBases.postgresql.filesUtilitis import filesUtllitis
from DataBases.postgresql.utils import randomString


class display():
    def __init__(self):

        self.fu = filesUtllitis()
        self.path = self.fu.getPath()

    def diplayPictureFromDB(self, memoryView):
        try:
            x = randomString(30)
            tempFileName = 'tempFile' + x + '.jpg'
            tempFilePath = self.path + tempFileName
            byte = bytes(memoryView[0][0])  # memoryView to lista krotek obiektów memoryview
            print(byte)
            open(tempFilePath, 'wb').write(byte)
            self.image = Image.open(tempFilePath).show()


        except Exception as ex:
            print(ex)

        finally:
            time.sleep(2)
            self.fu.removeFile(tempFileName)

    def displayPicturesFomDB(self, memoryViews):

        for view in memoryViews:
            try:

                input("press any key to display next picture: ")
                self.diplayPictureFromDB(view)
                time.sleep(2)
                del self.image
            except Exception as ex:
                print(ex)

    def displayPicturesViaPath(self, paths):
        for path in paths:
            try:
                input("press any key to display next picture: ")
                self.image = Image.open(path[0][0], 'r').show()
            except Exception as ex:
                print(ex)

            finally:
                time.sleep(2)
                del self.image