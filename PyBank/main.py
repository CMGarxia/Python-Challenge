#import pandas as pd
import os 
import csv
#from pathlib import Path
#print(os.getcwd())
#budget_csv = Path("/Users/rebelplanet/Desktop/Python-Challenge /PyBank/Resources/budget_data.csv")
#budget_df = pd.read_csv(budget_csv)
#budget_df.head()

#budget_csv = os.path.join ("..", "Resources", "budget_data.csv")
budget_csv = os.path.join ("/Users/rebelplanet/Desktop/Python-Challenge /PyBank/Resources/budget_data.csv")
#List data
dates = []
changes = []
#net_profit_losses = 0 
#total_months = 0
net_profit_losses = [] 
total_months = []

#with open(budget_csv) as budget_data:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#csvreader = csv.reader(budget_csv, delimiter=",")
#next(csvreader)  # Skip the header row
 #Loop thru rows in CSV file
    for row in csvreader:
    #extract data
    #date = row[0]
    #profit_loss = int(row[1])
        #dates.append(row,[0])
        dates.append([0])
        #changes.append(row,[1])
        changes.append([1])
        #net_profit_losses.append(row[2])
        net_profit_losses.append([2])
        #total_months.append(row[3])
        total_months.append([3])

    #calculate metrics
        #total_months += 1
        total_months += ([3])
        net_profit_losses += ([2])

#store data for calculating 
dates.append([0])
changes.append([1]) 

 #Calculate Average Change
average_change = sum(changes) / len(changes)

#find the greatest increase/decrease
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

#Print results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


#csv_header = next(csvreader)
#print(f"CSV Header: {csv_header}")

#for row in csvreader:
#    print(row)