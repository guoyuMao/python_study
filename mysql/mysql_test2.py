import pymysql

db = pymysql.connect("localhost","root","Manager0159","test")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Database version : {0}".format(data))
db.close()
