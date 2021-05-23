'''
PyBank/main.py
Written by Trent McNabb for Assignment 3 for Data analytics and visualization bootcamp.
Created May 23 2021
Last modified May 23 2021
'''
import os
import csv

csvFile = os.path.join(".", "Resources", "budget_data.csv" )
totalMonths = 0
total = 0
totalChanges = 0
biggestGainMonth= ''
biggestGain = -1000000
biggestLossMonth = ''
biggestLoss = 1000000

with open(csvFile, 'r') as file:
    csvReader = csv.reader(file,delimiter=',')
    csvHeader = next(csvReader)
    for row in csvReader:
        #for the first entry, set a value to compare against. For all subsequent entries. add the change to the total changes, compare the previous max and min changes, and decide if it is the new max or min change 
        if totalMonths > 0:
            currentChange = 0
            thisMonthProfit = int(row[1])
            change = thisMonthProfit - lastMonthProfit
            totalChanges = totalChanges + change
            if change > biggestGain:
                biggestGain = change
                biggestGainMonth = row[0]
            if change < biggestLoss:
                biggestLoss = change
                biggestLossMonth = row[0]
            lastMonthProfit = thisMonthProfit
        else:
            lastMonthProfit = int(row[1])
        #count the number of months, add the current total to the overall total
        totalMonths = totalMonths+1
        total = total+int(row[1])

#create output string
output = "Total Months: {:d}\nTotal : ${:d}\nAverageChange: {:.2f}\nGreatest increase in profits: {:s} ({:d})\nGreatest decrease in profits: {:s} ({:d})".format(totalMonths,total,totalChanges/(totalMonths-1),biggestGainMonth,biggestGain,biggestLossMonth,biggestLoss)

print(output)

#output the string to a file
outputFile = open("output.txt","w+")
outputFile.write(output)
outputFile.close()