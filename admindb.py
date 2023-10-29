import pymongo
import openpyxl as xl
xlsx=xl.load_workbook("data/attendance.xlsx",data_only=True)
sheet=xlsx["I_CSE-B"]
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Project-X"]
collection = db['admin']
