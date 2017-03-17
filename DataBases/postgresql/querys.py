import os

from DataBases.postgresql.filesUtilitis import filesUtllitis

path = os.path.dirname(os.path.abspath(__file__)) + "\Dane\\"


class query():
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def customQuery(self, query):
        try:
            print(query)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            print(result)
            return result
        except Exception as ex:
            print(ex)

    def addItreeExtension(self):
        self.customQuery("CREATE EXTENSION ltree;")

    def createTable(self):
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

        self.customQuery(sql.strip())
        print("Table Workers created correctly")

    def insertData(self):
        sql = """INSERT INTO workers (id,first_name,last_name,hierarchy)
                  VALUES (1,'Rick','Sanchez','BOSS'),
                   (2,'Sterling','Archer','BOSS.AGENT'),
                   (3,'William','Murderface','BOSS.DRUMER'),
                   (4,'BoJack','Horseman','BOSS.AGENT.HORSMAN'),
                   (5,'Homer ','Simpson','BOSS.AGENT.HORSMAN.HOMER');"""
        self.customQuery(sql.strip())

    def insertNewWorker(self, id, firstName, lastName, hierarchy):
        sql = "INSERT INTO workers (id,first_name,last_name,hierarchy) VALUES('{x}','{x1}','{x2}','{x3}')".format(x=id,x1=firstName,x2=lastName, x3=hierarchy)
        self.customQuery(sql.strip())
        self.connection.commit()

    def insertPictures(self):
        fs = filesUtllitis()
        i = 1
        for file in fs.getFiles(fs.getPath()):
            sql = """update workers
            set picture = {x}
            WHERE id = {y}""".format(x=str(fs.fileToStream(file,fs.getPath())), y=str(i))
            i += 1

            self.customQuery(sql.strip())

    def insertNewPictures(self, id,fileName):
        fs = filesUtllitis()
        sql = """update workers
                set picture = {x}
                WHERE id = {y}""".format(x=str(fs.fileToStream(fileName,fs.getPathNew())), y=id)
        self.customQuery(sql.strip())
        self.connection.commit()

    def insertPicturesLinks(self):
        fs = filesUtllitis()
        i = 1
        for file in fs.getFiles(fs.getPath()):
            path = "'" + str(fs.getPath() + file).replace("\\", "\\\\") + "'"
            sql = """update workers
                  set Link_to_picture = {x}
                  WHERE id = {y}""".format(x=path, y=str(i))
            i += 1
            self.customQuery(sql.strip())

    def insertNewPicturesLinks(self, picture, id):
        fs = filesUtllitis()
        path = "'" + str(fs.getPathNew() + picture).replace("\\", "\\\\") + "'"
        sql = """update workers
                     set Link_to_picture = {x}
                     WHERE id = {y}""".format(x=path, y=id)

        self.customQuery(sql.strip())
        self.connection.commit()

    def getPicture(self, id):
        sql = "SELECT picture FROM workers WHERE id=" + str(id)
        result = self.customQuery(sql.strip())
        return result

    def getPicturePath(self, id):
        sql = "SELECT Link_to_picture FROM workers WHERE id=" + str(id)
        result = self.customQuery(sql.strip())
        return result

    def getHierarchyFrom(self, root):
        sql = "SELECT * FROM workers where hierarchy ~ '*." + str(root) + ".*\'"
        print("Match any label path containing the label: " + root)
        self.customQuery(sql.strip())

    def getHierarchyLast(self, last):
        sql = "SELECT * FROM workers where hierarchy ~ '*." + str(last) + "\'"
        print("Match any label path whose last label is: " + last)
        self.customQuery(sql.strip())

    def getHierarchyExa(self, exa):
        sql = "SELECT * FROM workers where hierarchy ~ '" + str(exa) + "\'"
        print("Match the exact label path: " + exa)
        self.customQuery(sql.strip())

    def getGenreFromXMLBeID(self, id):
        sql = "SELECT  xpath('/INFO/Genre/text()',xml) from workers  where id ="+id
        print("Get genre be id: ")
        self.customQuery(sql.strip())

    def getGenreFromXML(self):
        sql = "SELECT  xpath('/INFO/Genre/text()',xml) from workers"
        print("Get all genres")
        self.customQuery(sql.strip())



    def insertXML(self, xmlFileName, id):
        fs = filesUtllitis()
        xmlFile = open(fs.getPathNew() + xmlFileName+".xml")
        xmlData =xmlFile.read()

        sql = """update workers
                   set XML = '{x}'
                   WHERE id = {y}""".format(x=xmlData, y=id)
        self.customQuery(sql.strip())
        self.connection.commit()


    def initLoad(self):
        print("***Start initial data Load***")
        try:
            self.addItreeExtension() #need to be run only onece
            self.createTable()
            self.insertData()
            self.insertPicturesLinks()
            self.insertPictures()
            self.connection.commit()
            print("***initial data Load Completed***")
        except Exception as ex:
            print(ex)
            print("***initial data Load failed***")

    def dropTable(self):
        try:
            self.customQuery("DROP TABLE workers")
            self.connection.commit()
        except Exception as ex:
            print(ex)
