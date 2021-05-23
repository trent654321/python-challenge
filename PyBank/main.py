'''
PyBank/main.py
Written by Trent McNabb for Assignment 3 for Data analytics and visualization bootcamp.
Created May 23 2021
Last modified May 23 2021
'''
import os
import csv

csv_file = os.path.join(".", "Resources", "budget_data.csv" )
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file,delimiter=',')
    csv_header = next(csv_reader)
    print(csv_header)
