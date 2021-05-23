'''
PyBank/main.py
Written by Trent McNabb for Assignment 3 for Data analytics and visualization bootcamp.
Created May 23 2021
Last modified May 23 2021
'''
import os
import csv

csvFile = os.path.join(".", "Resources", "budget_data.csv" )
totalMonths = 1
total = 0
biggestGainMonth= 'test 123'
biggestGain = 0
biggestLossMonth = 'test 123'
biggestLoss = 0

with open(csvFile, 'r') as file:
    csvReader = csv.reader(file,delimiter=',')
    csvHeader = next(csvReader)

#create output string
output = "Total Months: {:d}\nTotal : ${:d}\nAverageChange: {:f}\nGreatest increase in profits: {:s} ({:d})\nGreatest decrease in profits: {:s} ({:d})".format(totalMonths,total,total/totalMonths,biggestGainMonth,biggestGain,biggestLossMonth,biggestLoss)

print(output)

#output the string to a file
outputFile = open("output.txt","w+")
outputFile.write(output)
outputFile.close()