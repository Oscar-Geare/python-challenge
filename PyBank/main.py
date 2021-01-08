import csv
import os
import sys

# Select file
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
budgetFile = os.path.join(THIS_FOLDER,'Resources','budget_data.csv')

#Set variables
monthCount = 0
profLoss = 0
goodProfLoss = 0
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
        #index to count the months
        monthCount = monthCount + 1
        #Calculate total profit/loss
        profLoss = profLoss + float(row[1])

        #if profit/loss is greater/less than current greatest/worst then replace it and store the month
        if float(row[1]) > goodProfLoss:
            goodProfLoss = float(row[1])
            goodMonth = row[0]
        if float(row[1]) < badProfLoss:
            badProfLoss = float(row[1])
            badMonth = row[0]

#calculate average
avProfLoss = profLoss / monthCount

#Print to terminal
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {monthCount}')
print(f'Total: ${profLoss}')
print(f'Average Change: {avProfLoss}')
print(f'Greatest Increase: {goodMonth} (${goodProfLoss})')
print(f'Greatest Loss: {badMonth} (${badProfLoss})\n')

#because I can't think of a better method, change stdout to a file and printf again
outFolder = os.path.join(THIS_FOLDER,'output.txt')
outFile = open(outFolder,'w')
sys.stdout = outFile
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {monthCount}')
print(f'Total: ${profLoss}')
print(f'Average Change: {avProfLoss}')
print(f'Greatest Increase: {goodMonth} (${goodProfLoss})')
print(f'Greatest Loss: {badMonth} (${badProfLoss})\n')
outFile.close()
#reset stdout
sys.stdout = sys.__stdout__
