import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Manager0159"
)

mycursor = mydb.cursor()
#mycursor.execute("create database python_test_db")
# mycursor.execute("show databases")


# mycursor.execute("drop database python_test_db")

mycursor.execute("show databases")
for x in mycursor:
	print(x)