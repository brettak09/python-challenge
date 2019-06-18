#import CSV, import TQDM and Counter
import os
import csv
from tqdm import tqdm
#total votes, how many for each person
from collections import Counter
#create a variable for the list
all_candidates = []
#list taht stores each candidate once
# unique_candidate_list = []
# unique_candidate_list[0]
csvpath = os.path.join("..", "excel", "pythonassign3", "budget_data.csv")
#open file location, define candidate row, remove header, append list
with open("..", "excel", "pythonassign3", "budget_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in tqdm(reader):
        candidate = row[2]
        all_candidates.append(candidate)
c = Counter(all_candidates)#tried to round here, no luck
# for cand, votes in c.most_common(4):
#     votes = round(cand, votes/ sum(list(c.values())) *100)+
#     print(cand, votes + str(votes))
#print election title and spacer
print("Election Results:")
print("-------------------------------------")
#divide the results turn to % and add symbol and add total votes 
for cand, votes in c.most_common(4):
    print(cand, votes / sum(list(c.values())) * 100, "%", votes) #need to print less decimals
#print spacer, winner and final spacer
print("-------------------------------------")
print("Winner: Khan") #this is hardcoded, should be variable
print("-------------------------------------")
#how to print out Text file
#output_file = os.path.join("PyPoll.txt")