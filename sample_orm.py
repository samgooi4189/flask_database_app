import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host="127.0.0.1", user="root", \
        passwd="example", db="flask_example_app", \
        cursorclass=MySQLdb.cursors.DictCursor)

cur = db.cursor()

cur.execute("SELECT * FROM examples")

for row in cur.fetchall():
        print(row['id'], ":", row['description'])
