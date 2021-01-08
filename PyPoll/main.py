import csv
import os
import sys

# Select file
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
budgetFile = os.path.join(THIS_FOLDER,'Resources','election_data.csv')

#Set variables
voterCount = 0
counties = []
countiesVotes =[]
candidates = []
candidatesVotes = []
goodMonth = 'Null'
badProfLoss = 0
badMonth = 'Null'

#Open CSV
with open(budgetFile,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #Skip header
    header = next(csvreader)

    #Check all rows
    for row in csvreader:
        #index to count the votes
        voterCount = voterCount + 1

        #build list of counties (not required) and count votes
        if row[1] not in counties:
            counties.append(row[1])
            countiesVotes.append(1)
        else:
            index = counties.index(row[1])
            countiesVotes[index] = countiesVotes[index] + 1

        #build list of candidates and count votes
        if row[2] not in candidates:
            candidates.append(row[2])
            candidatesVotes.append(1)
        else:
            index = candidates.index(row[2])
            candidatesVotes[index] = candidatesVotes[index] + 1

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {voterCount}')
print(f'-------------------------')
count = 0
winnerVotes = 0
winner = 'None'
for run in candidates:
    percent = round((candidatesVotes[count] / voterCount) * 100,5)
    print(f'{run}: {candidatesVotes[count]} ({percent}%)')
    if candidatesVotes[count] > winnerVotes:
        winnerVotes = candidatesVotes[count]
        winner = run
    count = count + 1
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')


#because I can't think of a better method, change stdout to a file and printf again
outFolder = os.path.join(THIS_FOLDER,'output.txt')
outFile = open(outFolder,'w')
sys.stdout = outFile
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {voterCount}')
print(f'-------------------------')
count = 0
winnerVotes = 0
winner = 'None'
for run in candidates:
    percent = round((candidatesVotes[count] / voterCount) * 100,4)
    print(f'{run}: {candidatesVotes[count]} ({percent}%)')
    if candidatesVotes[count] > winnerVotes:
        winnerVotes = candidatesVotes[count]
        winner = run
    count = count + 1
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')
outFile.close()
#reset stdout
sys.stdout = sys.__stdout__
