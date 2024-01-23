#dependencies
import os
import csv

#path to data csv file
election_data_csv = os.path.join("Resources","election_data.csv")

#define variables, dictionaries, lists
candidate_votes = {}
results = []

#read csv file using module and create csv_reader obj.

with open(election_data_csv, 'r') as election_csv:     #open in read mode 
    csv_reader = csv.reader(election_csv)
    next(csv_reader, None)       #skip header

    #rows for candidate names and calculating candidate vote counts

    for row in csv_reader:
        candidate = row[2]  
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#add total votes 
            
total_votes_cast = sum(candidate_votes.values())

#calculate vote percentage and format 
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes_cast) * 100
    candidate_results = f"{candidate}: {percentage:.3f}% ({votes})"
    results.append(candidate_results)     #append format string to a list

#determine winner by popular votes
winner = max(candidate_votes, key=candidate_votes.get)


##print outputs and format
print("Election Results")

print("-------------------------")

print("Total Votes: " + str(total_votes_cast))

print("-------------------------")

for candidate_results in results:
    print(candidate_results)

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#output to a text file
output_file = os.path.join("analysis", "election_results.txt")

with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes_cast}\n")
    txtfile.write("-------------------------\n")
    for candidate_results in results:
        txtfile.write(candidate_results + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
