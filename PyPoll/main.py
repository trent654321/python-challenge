'''
PyPoll/main.py
Written by Trent McNabb for Assignment 3 for Data analytics and visualization bootcamp.
Created May 23 2021
Last modified May 23 2021
'''
import os
import csv

candidates = {}
totalVotes = 0
maxVotes = 0
csvFile = os.path.join(".", "Resources", "election_data.csv" )
with open(csvFile, 'r') as file:
    csvReader = csv.reader(file,delimiter=',')
    csvHeader = next(csvReader)
    for row in csvReader:
        totalVotes = totalVotes+1
        #if the candidates name is a key in the dictionary, increment the value by one. If not, insert the key with the value of 1
        if row[2] in candidates:
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1


output = "Election Results\n------------------------\nTotal Votes: {:d}\n------------------------\n".format(totalVotes)
for candidate in candidates:
    votes = candidates[candidate]
    output += "{:s}: {:.3%} ({:d})\n".format(candidate, votes/totalVotes, totalVotes)
    if votes > maxVotes:
        maxVotes = votes
        winner = candidate
output += "------------------------\nWinner: {:s}\n------------------------\n".format(winner)
print(output)

#output the string to a file
outputFile = open("output.txt","w+")
outputFile.write(output)
outputFile.close()