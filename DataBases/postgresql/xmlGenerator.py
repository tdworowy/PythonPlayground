from filesUtilitis import filesUtllitis
from querys import query


class xmlGenerator():
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.qu = query(self.connection)
        self.fu = filesUtllitis()

    def exportToXML(self, id):
        try:
            resoult = self.qu.customQuery("select * from workers where id="+ str(id))
            resoult = list(resoult[0])
            firstName = resoult[2]
            print("Start generating xml file: "+firstName + ".xml")
            xmlFile = open(self.fu.getPathExp()+firstName + ".xml", 'w')
            xmlFile.write('<?xml version="1.0" ?>\n')
            xmlFile.write('<workers>\n')
            xmlFile.write('<first name>%s</first name>\n' % resoult[1])
            xmlFile.write('<last name>%s</last name>\n' % resoult[2])
            xmlFile.write('<Picture>%s</Picture>\n' % resoult[3])
            xmlFile.write('<hierarchy>%s</hierarchy>\n' % resoult[5])
            xmlFile.write('</workers>\n')
            xmlFile.flush()
            xmlFile.close()
            print("XML generated correctly")

        except Exception as ex:
            print(ex)
            print("XML generation failed")

    def generateXML(self, lastName,*args):
        try:

            print("Start generating xml file: " + lastName + ".xml")
            xmlFile = open(self.fu.getPathNew() + lastName + ".xml", 'w')
            xmlFile.write('<?xml version="1.0" ?>\n')
            xmlFile.write('<INFO>\n')
            for arg in args:
                xmlFile.write('<{x}>{y}</{x}>\n'.format(x=arg[0], y=arg[1]))

            xmlFile.write('</INFO>\n')
            xmlFile.flush()
            xmlFile.close()
            print("XML generated correctly")

        except Exception as ex:
            print(ex)
            print("XML generation failed")

