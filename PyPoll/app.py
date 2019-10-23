#import CSV, import TQDM and Counter
import os
import csv
from tqdm import tqdm
#total votes, how many for each person
from collections import Counter
csvpath = os.path.join("..", "Data", "election_data.csv")
#Creates dictionary to be used for candidate name and vote count.
poll = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

#open file location, define candidate row, remove header, append list
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in tqdm(csvreader):
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] +1
        else:
            poll[row[2]] = 1
#create empty list for candidates and his/her vote count
candidates = []
num_votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))
# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints to file
output_file = os.path.join("PyPoll.txt")

with open(output_file, "w") as txt_file:
    txt_file.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txt_file.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txt_file.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')
with open(output_file, 'r') as readfile:
    print(readfile.read())