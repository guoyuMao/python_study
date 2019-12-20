import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["runoobdb"]
mycol = mydb["sites"]
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
x = mycol.insert_one(mydict)
print(x)