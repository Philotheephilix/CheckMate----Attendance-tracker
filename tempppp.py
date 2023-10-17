import pandas as pd
import csv
from flask import Flask, render_template, request, redirect, url_for
import pymongo
import xlsxwriter
app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Project-X"]
collection = db["studentDet"]
input_excel_file = 'data/attendance.xlsx'
data = pd.read_excel(input_excel_file)
data.to_csv('output.csv', index=False)
username = '22CS168'
with open("output.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    list=[]
    for row in csv_reader:
        if "STUDENTS ATTENDANCE" in row:
            i=row.index("STUDENTS ATTENDANCE")
            row[i]=""
        if "DATE" in row:
            list.append(row[4:])
        if "DAY ORDER" in row:
            i=row.index("DAY ORDER")
            row[i]="DAY"
            list.append(row[4:])
        if username in row:
            list.append(row[4:])
fname=username+".csv"
with open(fname,"w") as file:
    writer=csv.writer(file)
    for i in list:
        writer.writerow(i)
data1 = pd.read_csv(username+".csv")
for i in range(54):
    a="Unnamed: "+str(i)
    data1.rename({a:i}, axis="columns", inplace=True)
data1 = data1.dropna(axis=1, how='all')
data1.at[3, data1.columns[1]] = None
output_excel_file = 'modified_output.xlsx'
with pd.ExcelWriter(output_excel_file, engine='xlsxwriter') as writer:
    data1.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    for idx, col in enumerate(data1.columns):
        max_length = max(data1[col].astype(str).apply(len).max(), len(str(col)))
        worksheet.set_column(idx, idx, max_length)
