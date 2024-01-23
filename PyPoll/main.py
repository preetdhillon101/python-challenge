#Challenge PyPoll

#Import modules os and csv
import os
import csv

#Set path for csv file in PyPoll_path
PyPoll_path = 'PyPoll/Resources/election_data.csv'

#Create list to store data 
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#open and read csv file
with open(PyPoll_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Count total votes
        count = count+1
        #Assign the names of candidates to candidatelist
        candidatelist.append(row[2])
        #Unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x) 
        #total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        #percent of total votes 
        z = (y/count)*100
        vote_percent.append(z)

    #Counting results
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print("Total votes: " + str(count))
    print("-------------------------")
    for i in range(len(unique_candidate)):
        print(unique_candidate[i] + ": " + str(round(vote_percent[i])) + "%(" + str(vote_count[i]) + ")")

    print("-------------------------")
    print("The winner is " + winner)
    print("-------------------------")

    #Print to a text file:
    with open('election_results.txt', 'w') as text:
        text.write("Election Results")
        text.write("-----------------------------------\n")
        text.write("Total votes: " + str(count) + "\n")
        text.write("-----------------------------------\n")
        for i in range(len(set(unique_candidate))):
          text.write(unique_candidate[i] + ": " + str(round(vote_percent[i])) + "%(" + str(vote_count[i]) + ")\n")
        text.write("-----------------------------------\n")
        text.write("The winner is " + winner + "\n")
        text.write("-----------------------------------\n")