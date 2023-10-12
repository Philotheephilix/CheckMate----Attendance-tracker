import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["studentusercred"]
username=input()
password = int(input())
result = collection.find_one({"key": "value"})
query={"Roll No":username}
result=collection.find_one(query)
print(result["Reg No"])
if password==result["Reg No"]:
    print("login success")
print(result)