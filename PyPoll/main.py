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

    
    'Declares empty list that receives csv data'
    votes = []
    'Declares empty list that receives candidate names'
    candidates= []
    'This is a dictionary that will have candidate names as keys and their respective vote totals as values'
    candidate_counter = {}
    'Declares var for total votes in election'
    total = 0
    'Declares empty list that receives lines of text to be printed at the end of the script'
    text = []
    'This is a list used to find the winner of the election'
    vote_tally= []

    'Opens csv file and appends csv data to votes list'
    with open(f, newline ='') as csvfile:
        vote_data = csv.reader(csvfile)
        for row in vote_data:
            votes.append(row)

    'Loops through csv data and add all unique candidate names to candidates'
    for i in range(1, len(votes)):
        if votes[i][2] not in candidates:
            candidates.append(votes[i][2])

    'Sets candidate names as dictionary keys'
    for candidate in candidates:
        candidate_counter[candidate] = 0

    'Loops through csv data and tallies votes for each candidate'
    for i in range(1, len(votes)):
        candidate_counter[votes[i][2]] += 1

    'Adds first three lines of text to text list'
    text.append('CVS filename : %s' %(f))
    text.append("\nElection Results")
    text.append("--------------------------")

    'This loops does two things. It sums up all of the votes to find total votes and it add each candidates total votes to a list'
    for values in candidate_counter.values():
        total += values
        vote_tally.append(values)
    'This loop searches for the key / value pair in the candidate_counter dict that had the max # of votes.'
    for candidate, votes in candidate_counter.items():
        if votes == max(vote_tally):
            winner = candidate
        

    text.append("Total Votes: %s" %(str(total)))

    'This loops through candidate dict to add a line to text list about each candidate'
    for person, value in candidate_counter.items():
        percent = (value / total) * 100 
        text.append("%s : %s%% (%s)" %(person, str("{0:.2f}".format(percent)), str(value) ))

    'Last append to text list'
    text.append("--------------------------\nWinner : %s\n--------------------------" %(winner))

    'Prints election results to terminal'
    for line in text:
        print(line)

    "Creates name for .txt file where the election results will be written"
    textf = f[:-3] + 'txt'

    'Writes election results to .txt file'
    with open(textf, 'w') as textfile:
        for line in text:
            textfile.write(line + '\n')
        