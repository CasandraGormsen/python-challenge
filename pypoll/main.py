import os
import csv
from pathlib import Path
# Path to collect data from the Resources folder
poll_csv = os.path.join("Resources", "election_data.csv")

# Define variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open the CSV and store the contents
with open(poll_csv) as pollfile:
    csvreader = csv.reader(pollfile, delimiter=",")

    # Skip the header
    header = next(csvreader)

    # Work through the rows
    for row in csvreader:
        total_votes +=1

        # run through candidates
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] =="Correy":
            correy_votes +=1
        elif row[2] =="Li":
            li_votes +=1
        elif row[2] =="O'Tooley":
            otooley_votes +=1


print("Total Votes: "+str(total_votes))
print("Khan: " + str(khan_votes))
print("Correy: " + str(correy_votes))
print("Li: " + str(li_votes))
print("O'Tooley: " + str(otooley_votes))