import psycopg2


class PostgresConnection():
    def __init__(self, db, user, password):
        self.connect(db, user, password)

    def connect(self, db, user, password):
        con_string = "host='localhost' dbname=" + db + " user=" + user  + " password=" + password
        print(con_string)
        try:
            self.conn = psycopg2.connect(con_string)
        except Exception as ex:
            print(ex)
            print("connection Error")

    @property
    def get_connection(self):
            return self.conn

    def commit(self):
         self.conn.commit()