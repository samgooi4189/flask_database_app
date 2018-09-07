import MySQLdb
import MySQLdb.cursors

class Database:

    host = '127.0.0.1'
    user = 'root'
    password = 'example'
    db = 'flask_example_app'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db, cursorclass=MySQLdb.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()


    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


