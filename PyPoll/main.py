'''
PyPoll/main.py
Written by Trent McNabb for Assignment 3 for Data analytics and visualization bootcamp.
Created May 23 2021
Last modified May 23 2021
'''
import os
import csv

csvFile = os.path.join(".", "Resources", "election_data.csv" )
with open(csvFile, 'r') as file:
    csvReader = csv.reader(file,delimiter=',')
    csvHeader = next(csvReader)
    print(csvHeader)


output = "test"

print(output)

#output the string to a file
outputFile = open("output.txt","w+")
outputFile.write(output)
outputFile.close()