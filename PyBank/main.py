import csv
import os 

'files is list of all directories and files within current directory'
files = os.listdir()
'csv_list is used to capture the names of cvs files in the directory'
csv_list = []

'This loop adds only the csv file names to csv_list'
for item in files:
    if item[-3:] == 'csv':
        csv_list.append(item)

'This loops through all csv files in the directory'
for f in csv_list:

    'Resets Revenue var'
    Revenue = 0 
    'Declares empty list that receives csv data'
    budget = []
    'Declares empty list that receives lines of text to be printed at the end of the script'
    text = []

    'Opens csv file and appends csv data to budget list'
    with open(f, newline ='') as csvfile:
        budget_data = csv.reader(csvfile)
        for row in budget_data:
            budget.append(row)

    'Max and Min are lists used to capture the month with greatest revenue and the one with smallest revenue'
    'First element of list is the month string, second element is the revenue int'
    'They are set equal to the date and revenue from the first month'
    Max = [budget[1][0], int(budget[1][1])]
    Min = [budget[1][0], int(budget[1][1])]

    'Loops through all revenues in csv file and finds the Max and Min revenue and the corresponding months'
    for i in range(1, len(budget)-1):    
        if int(budget[i+1][1]) > Max[1]:
            Max[1] = int(budget[i+1][1])
            Max[0] = budget[i+1][0]
        if int(budget[i+1][1]) < Min[1]:
            Min[1] = int(budget[i+1][1])
            Min[0] = budget[i+1][0]

    'Loops through csv to calculate the total revenue'
    for i in range(1, len(budget)):
        Revenue += int(budget[i][1])

    "Appending text lines of the budget csv analysis to a list"
    text.append("Financial Analysis")
    text.append("--------------------------")
    text.append("\nFilename: %s" %(f))
    text.append("Total Months: %a" %(len(budget) -1 ))
    text.append("Total Revenue: $%s" %(Revenue))
    text.append("Average Revenue Change: $%s" %("{0:.2f}".format(Revenue / (len(budget)-1))))
    text.append("Greatest Increase in Revenue: %s ($%s)" %(Max[0], Max[1]))
    text.append("Greatest Decrease in Revenue: %s ($%s)\n" %(Min[0], Min[1]))

    "Prints financial analysis to terminal"
    for line in text:
        print(line)
    
    "Creates name for .txt file where the financial analysis will be written"
    textf = f[:-3] + 'txt'

    'Writes financial analysis to .txt file'
    with open(textf, 'w') as textfile:
        for line in text:
            textfile.write(line + '\n')