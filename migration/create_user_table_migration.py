import sys
sys.path.append("..")
from database import Database

db = Database()

print(db.insert("CREATE TABLE users (username varchar(24), password varchar(255));"))
