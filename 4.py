#!/usr/bin/python3
# import random
# list = []
# for i in range(0,200):
#     list.append({"id":i,"shopcard":''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))})
# for j in list:
#     print(j.get("id"), j.get("shopcard"))
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
mycol = mydb["card"]
# x = mycol.insert_one(mydict)
# x = mycol.insert_many(list)
for y in mycol.find():
  print(y)
# print(x)

if "runoobdb" in dblist:
  print("数据库已存在！")