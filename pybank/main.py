import os
import csv
from pathlib import Path
# Path to collect data from the Resources folder
bank_csv = os.path.join("Resources", "budget_data.csv")

# Define variables
months = []
profit = []
profit_change = []


# Open the CSV and store the contents
with open(bank_csv) as bankfile:
    csvreader = csv.reader(bankfile, delimiter=",")

    # Skip the header
    header = next(csvreader)

    # Work through the rows
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))

    # Work through the profits to find the change
    for i in range(len(profit)-1):

        # Append the difference
        profit_change.append(profit[i+1]-profit[i])
# Find min and max
max_increase = max(profit_change)
max_decrease = min(profit_change)

# Find the months for min and max
max_month = profit_change.index(max(profit_change))+1
min_month = profit_change.index(min(profit_change))+1

# Print 
print("Total Months: " + str(len(months)))
print("Total: $" + str(sum(profit)))
print("Average Change: $" + str(round(sum(profit_change)/len(profit_change),2)))
print("Greatest Increase in Profits: " + months[max_month] + " (" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + months[min_month] + " (" + str(min_month) + ")")

#Output
output_file = Path("Bank_Analysis.csv")

with open(output_file,"w") as file:

    file.write("Total Months: " + str(len(months)))
    file.write("Total: $" + str(sum(profit)))
    file.write("Average Change: $" + str(round(sum(profit_change)/len(profit_change),2)))
    file.write("Greatest Increase in Profits: " + months[max_month] + " (" + str(max_increase) + ")")
    file.write("Greatest Decrease in Profits: " + months[min_month] + " (" + str(min_month) + ")")
