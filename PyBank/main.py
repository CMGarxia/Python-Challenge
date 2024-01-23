#dependencies
import os 
import csv

#path to csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#csv_path = "/Users/rebelplanet/Desktop/Python-Challenge /PyBank/Resources/budget_data.csv"
#def financial_analysis(csv_path):

#list variables
previous_profit_losses = None
changes = []
total_profit_losses = 0 
total_months = 0 
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

    #read csv file in read mode
with open(budget_data_csv, 'r') as budget_csv:
        csv_reader = csv.reader(budget_csv)
        row_header = next(csv_reader, None) #store header
        # loop rows in csv
        for row in csv_reader:
            total_months += 1
            #print(f"Total Months: {total_months}")

with open(budget_data_csv, 'r') as budget_csv:    #read csv file in read mode
     csv_reader = csv.reader(budget_csv)
     next(csv_reader, None)       #store header
            

     for row in csv_reader:
            profit_losses = int(row[1])
            total_profit_losses += profit_losses

formatted_total = "${:.0f}".format(total_profit_losses)

#read csv file using module and create csv_reader obj.
with open(budget_data_csv, 'r') as budget_csv:     #open in readmode
      csv_reader = csv.reader(budget_csv)
      row_header = next(csv_reader, None)   #store header

      for row in csv_reader:
          current_profit_losses = int(row[1])
          if previous_profit_losses is not None:
                change = current_profit_losses - previous_profit_losses
                changes.append(change)
                previous_profit_losses = current_profit_losses
            
average_change = sum(changes)/len(changes)
formatted_average_change = "${:.2f}".format(average_change)

with open(budget_data_csv, 'r') as budget_csv:  #open in read mode
     csv_reader = csv.reader(budget_csv)
     next(csv_reader, None)   #store header


     for row in csv_reader:
           current_profit_losses = int(row[1])
           date = row[0]

           #conditional for Greatest Increase and Decrease in profits
           if previous_profit_losses is not None:
                 change = current_profit_losses - previous_profit_losses 

                 if change > greatest_increase:
                       greatest_increase = change
                       greatest_increase_date = date

                 if change < greatest_decrease: 
                       greatest_decrease = change
                       greatest_decrease_date = date

           previous_profit_losses = current_profit_losses
           
#print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")  

#print formatted outputs
print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {total_months}")

print("----------------------------")

print(f"Total: {formatted_total}")

print("----------------------------")

print(f"Average Change: {formatted_average_change}")

print("----------------------------")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

print("----------------------------")

print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
      
#output results to text file
output_file = os.path.join("analysis", "budget_data_results.txt")

with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total: {formatted_total}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Average Change: {formatted_average_change}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease}\n")        
    
