#import python tools
import os
import csv
from tqdm import tqdm
from collections import Counter
#create list
months =[]
revenue = []
#open budget_data.csv
csvpath = os.path.join("..", "excel", "pythonassign3", "budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in tqdm(csvreader):
        months.append(row[0])
        revenue.append(int(row[1]))
#Count all the months, basically counting rows and skipping the header per above.
total_months = len(months)
#create greatest increase, decrease variable and set them equal to the first revenue entery
#set total revenue = 0
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]
#calculate average_change enter this in to PyPoll to round
average_change = round(total_revenue/total_months, 2)
#print(results_print)
print("Financial Analysis:")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue: " + great_inc_month + " ($" + str(greatest_inc) +")")
print("Greatest Decrease in Revenue: " + great_dec_month + " ($" + str(greatest_dec)+ ")")
#create the text file
output_file = os.path.join("PyBank.txt")
#write to file
with open(output_file, "w") as txt_file:
    #trying to add space with the \n, but getting syntax error. 
    txt_file.write("Financial Analysis \n")
    txt_file.write("--------------------------------------- \n")
    txt_file.write("Total Months: "  + str(total_months) + "\n")
    txt_file.write("Total Revenue: " + "($" + str(total_revenue) +") \n" )
    txt_file.write("Average Revenue Change: " + "($" + str(average_change) +") \n")
    txt_file.write("Greatest Increase in Revenue: "  + great_inc_month + " ($" + str(greatest_inc) +") \n")
    txt_file.write("Greatest Decrease in Revenue: " + great_dec_month + " ($" + str(greatest_dec)+ ")")