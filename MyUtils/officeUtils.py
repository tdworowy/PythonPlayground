from odf.opendocument import load


def getODTXML(path):
    doc = load(path)
    return doc.xml()


if __name__ == '__main__':
    with open("temp.xml",'w') as f:
        f.write(getODTXML("D:\Google_drive\Studia_magister\Magisterka\Praca\mgr_v51.odt").decode("utf-8") )
