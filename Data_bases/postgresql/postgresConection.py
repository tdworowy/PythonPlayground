import psycopg2


class postgresConection():
    def __init__(self, db, user, password):
        self.conect(db, user, password)

    def conect(self, db, user, password):
        conString = "host='localhost' dbname=" + db + " user=" + user  + " password=" + password
        print(conString)
        try:
            self.conn = psycopg2.connect(conString)
        except Exception as ex:
            print(ex)
            print("connection Error")

    @property
    def getConection(self):
            return self.conn

    def commit(self):
         self.conn.commit()