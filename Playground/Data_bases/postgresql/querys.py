import os

from Data_bases.postgresql.filesUtilitis import FilesUtils

path = os.path.dirname(os.path.abspath(__file__)) + "\Dane\\"


class Query():
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def custom_query(self, query):
        try:
            print(query)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            print(result)
            return result
        except Exception as ex:
            print(ex)

    def add_Itree_extension(self):
        self.custom_query("CREATE EXTENSION ltree;")

    def create_table(self):
        sql = """CREATE TABLE workers(
                                       id SERIAL,
                                       first_name varchar,
                                       last_name varchar,
                                       picture bytea,
                                       Link_to_picture varchar,
                                       hierarchy ltree,
                                       XML xml,
                                       PRIMARY KEY(id)
                                       );"""

        self.custom_query(sql.strip())
        print("Table Workers created correctly")

    def insert_data(self):
        sql = """INSERT INTO workers (id,first_name,last_name,hierarchy)
                  VALUES (1,'Rick','Sanchez','BOSS'),
                   (2,'Sterling','Archer','BOSS.AGENT'),
                   (3,'William','Murderface','BOSS.DRUMER'),
                   (4,'BoJack','Horseman','BOSS.AGENT.HORSMAN'),
                   (5,'Homer ','Simpson','BOSS.AGENT.HORSMAN.HOMER');"""
        self.custom_query(sql.strip())

    def insertNewWorker(self, id, firstName, lastName, hierarchy):
        sql = "INSERT INTO workers (id,first_name,last_name,hierarchy) VALUES('{x}','{x1}','{x2}','{x3}')".format(x=id,x1=firstName,x2=lastName, x3=hierarchy)
        self.custom_query(sql.strip())
        self.connection.commit()

    def insertPictures(self):
        fs = FilesUtils()
        i = 1
        for file in fs.get_files(fs.get_path()):
            sql = """update workers
            set picture = {x}
            WHERE id = {y}""".format(x=str(fs.file_to_stream(file, fs.get_path())), y=str(i))
            i += 1

            self.custom_query(sql.strip())

    def insert_new_pictures(self, id, fileName):
        fs = FilesUtils()
        sql = """update workers
                set picture = {x}
                WHERE id = {y}""".format(x=str(fs.file_to_stream(fileName, fs.get_new_path())), y=id)
        self.custom_query(sql.strip())
        self.connection.commit()

    def insertPicturesLinks(self):
        fs = FilesUtils()
        i = 1
        for file in fs.get_files(fs.get_path()):
            path = "'" + str(fs.get_path() + file).replace("\\", "\\\\") + "'"
            sql = """update workers
                  set Link_to_picture = {x}
                  WHERE id = {y}""".format(x=path, y=str(i))
            i += 1
            self.custom_query(sql.strip())

    def insertNewPicturesLinks(self, picture, id):
        fs = FilesUtils()
        path = "'" + str(fs.get_new_path() + picture).replace("\\", "\\\\") + "'"
        sql = """update workers
                     set Link_to_picture = {x}
                     WHERE id = {y}""".format(x=path, y=id)

        self.custom_query(sql.strip())
        self.connection.commit()

    def get_picture(self, id):
        sql = "SELECT picture FROM workers WHERE id=" + str(id)
        result = self.custom_query(sql.strip())
        return result

    def get_picture_path(self, id):
        sql = "SELECT Link_to_picture FROM workers WHERE id=" + str(id)
        result = self.custom_query(sql.strip())
        return result

    def get_hierarchy_from(self, root):
        sql = "SELECT * FROM workers where hierarchy ~ '*." + str(root) + ".*\'"
        print("Match any label path containing the label: " + root)
        self.custom_query(sql.strip())

    def get_hierarchy_last(self, last):
        sql = "SELECT * FROM workers where hierarchy ~ '*." + str(last) + "\'"
        print("Match any label path whose last label is: " + last)
        self.custom_query(sql.strip())

    def get_hierarchy_exa(self, exa):
        sql = "SELECT * FROM workers where hierarchy ~ '" + str(exa) + "\'"
        print("Match the exact label path: " + exa)
        self.custom_query(sql.strip())

    def get_genre_from_xml_be_id(self, id):
        sql = "SELECT  xpath('/INFO/Genre/text()',xml) from workers  where id ="+id
        print("Get genre be id: ")
        self.custom_query(sql.strip())

    def get_genre_from_xml(self):
        sql = "SELECT  xpath('/INFO/Genre/text()',xml) from workers"
        print("Get all genres")
        self.custom_query(sql.strip())



    def insert_xml(self, xmlFileName, id):
        fs = FilesUtils()
        xml_file = open(fs.get_new_path() + xmlFileName + ".xml")
        xml_data =xml_file.read()

        sql = """update workers
                   set XML = '{x}'
                   WHERE id = {y}""".format(x=xml_data, y=id)
        self.custom_query(sql.strip())
        self.connection.commit()


    def init_load(self):
        print("***Start initial data Load***")
        try:
            self.add_Itree_extension() #need to be run only onece
            self.create_table()
            self.insert_data()
            self.insertPicturesLinks()
            self.insertPictures()
            self.connection.commit()
            print("***initial data Load Completed***")
        except Exception as ex:
            print(ex)
            print("***initial data Load failed***")

    def drop_table(self):
        try:
            self.custom_query("DROP TABLE workers")
            self.connection.commit()
        except Exception as ex:
            print(ex)
