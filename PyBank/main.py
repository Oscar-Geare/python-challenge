import csv
import os
import sys

# Select file
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
budgetFile = os.path.join(THIS_FOLDER,'Resources','budget_data.csv')

#Set variables
goodProfLoss = 0
goodMonth = 'Null'
badProfLoss = 0
badMonth = 'Null'
monthlyChange = 0
sumMonthlyChange = []

#Open CSV
with open(budgetFile,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #Skip header
    header = next(csvreader)

    #Set up data
    firstRow = next(csvreader)
    monthCount = 1
    profLoss = float(firstRow[1])
    lastMonth = float(firstRow[1])

    #Check all rows
    for row in csvreader:
        #index to count the months
        monthCount = monthCount + 1

        #Calculate total profit/loss
        profLoss = profLoss + float(row[1])

        #Track monthly changes
        monthlyChange = float(row[1]) - lastMonth
        sumMonthlyChange.append(monthlyChange)
        lastMonth = float(row[1])

        #if profit/loss is greater/less than current greatest/worst then replace it and store the month
        if monthlyChange > goodProfLoss:
            goodProfLoss = monthlyChange
            goodMonth = row[0]
        if monthlyChange < badProfLoss:
            badProfLoss = monthlyChange
            badMonth = row[0]

#calculate average
# avProfLoss = profLoss / monthCount
avProfLoss = sum(sumMonthlyChange) / len(sumMonthlyChange)

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
