import pandas as pd
import csv
from flask import Flask, request
import pymongo
import xlsxwriter


def process_csv(input_file, output_file, username):
    data = pd.read_excel(input_file)
    data = data.rename(columns=lambda x: x.replace('Unnamed:', '') if 'Unnamed:' in str(x) else x)
    data = data.dropna(axis=1, how='all')
    data = data[data['STUDENTS ATTENDANCE'] != 'DATE']
    data = data[data['STUDENTS ATTENDANCE'] != 'DAY ORDER']
    data = data.drop(['STUDENTS ATTENDANCE', 'DAY ORDER'], axis=1)
    data.to_csv('output.csv', index=False)
    
    with open("output.csv", mode='r') as file:
        csv_reader = csv.reader(file)
        output_rows = []
        for row in csv_reader:
            if username in row:
                output_rows.append(row[4:])
    
    fname = username + ".csv"
    with open(fname, "w") as file:
        writer = csv.writer(file)
        for i in output_rows:
            writer.writerow(i)

    data1 = pd.read_csv(username + ".csv")
    output_excel_file = output_file
    data1.to_excel(output_excel_file, index=False)

def process():
    input_excel_file = 'data/attendance.xlsx'
    username="22CS168"
    output_excel_file = 'modified_output.xlsx'
    process_csv(input_excel_file, output_excel_file, username)
    return 'Processing completed!'
process()
    

