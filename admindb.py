import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Project-X"]
query = { "username": "maintainer@philix" }
update = { "$set": {"username":"maintainer@philix","password":"dev_door@philix"} }
collection = db['admin']
while 1:
    choice=int(input("ADMIN USER MANAGEMENT CONSOLE\n1.View users\n2.Add users\n3.Delete users\n4.Exit\nEnter your choice:"))
    if choice==1:
        for document in collection.find():
            if document==collection.find_one(query):
                continue
            print(document)
    elif choice==2:
        username=input("Enter Admin user name:")
        password=input("Enter password for "+username+":")
        collection.insert_one({"username":username,"password":password})
    elif choice==3:
        for document in collection.find():
            print(document)
        username=input("Enter Username to delete:")
        exist=collection.delete_one({"username": username})
    elif choice==4:
        break
    else:
        print("Enter valid Choice")
collection.update_one(query, update, upsert=True)


    

