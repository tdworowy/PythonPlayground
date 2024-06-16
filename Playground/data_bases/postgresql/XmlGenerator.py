from Data_bases.postgresql.filesUtilitis import FilesUtils
from Data_bases.postgresql.querys import Query


class XmlGenerator:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.qu = Query(self.connection)
        self.fu = FilesUtils()

    def export_to_xml(self, id):
        try:
            result = self.qu.custom_query("select * from workers where id=" + str(id))
            result = list(result[0])
            first_name = result[2]
            print("Start generating xml file: " + first_name + ".xml")
            xml_file = open(self.fu.get_path_exp() + first_name + ".xml", "w")
            xml_file.write('<?xml version="1.0" ?>\n')
            xml_file.write("<workers>\n")
            xml_file.write("<first name>%s</first name>\n" % result[1])
            xml_file.write("<last name>%s</last name>\n" % result[2])
            xml_file.write("<Picture>%s</Picture>\n" % result[3])
            xml_file.write("<hierarchy>%s</hierarchy>\n" % result[5])
            xml_file.write("</workers>\n")
            xml_file.flush()
            xml_file.close()
            print("XML generated correctly")

        except Exception as ex:
            print(ex)
            print("XML generation failed")

    def generate_xml(self, last_name, *args):
        try:

            print("Start generating xml file: " + last_name + ".xml")
            xml_file = open(self.fu.get_new_path() + last_name + ".xml", "w")
            xml_file.write('<?xml version="1.0" ?>\n')
            xml_file.write("<INFO>\n")
            for arg in args:
                xml_file.write("<{x}>{y}</{x}>\n".format(x=arg[0], y=arg[1]))

            xml_file.write("</INFO>\n")
            xml_file.flush()
            xml_file.close()
            print("XML generated correctly")

        except Exception as ex:
            print(ex)
            print("XML generation failed")
