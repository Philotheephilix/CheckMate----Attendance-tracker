import pandas as pd
import csv
from flask import Flask, render_template, request, redirect, url_for
import pymongo
import xlsxwriter
username = '22CS155'

with open("output.csv", mode='r') as file:
    csv_reader = csv.reader(file)
        
    list=[]
    for row in csv_reader:
        for i in range(54):
            for j in range (55):
                if row[j].startswith("Unna"):
                    row[j].replace("Unnamed:","")
        if not "Unnamed" in row:
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
                # If the username is found, print the row
                list.append(row[4:])
        # If the username is not found in the entire CSV file
fname=username+".csv"
with open(fname,"w") as file:
    writer=csv.writer(file)
    for i in list:
        print(i)
        writer.writerow(i)