import os
import csv

#define the locations of input and output files
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "Output.txt")

# Define the 'electionData' parameters

Candidates_options =["Khan", "Correy", "Li", "O'Tooley"]
Votes = []
Candidate_Votes = []

totalvotes = 0
Khantotal = 0
Correytotal = 0
Litotal = 0
Tooleytotal = 0


with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        
        #total votes cast
        totalvotes += 1
         #get a list of candidates
        candidateName = row[2]
         #get candidate votes   
        Candidate_Votes[candidateName] = 0
        Candidate_Votes[candidateName] += 1



# generate Output
output = (

    f"Election Results\n"
    f"-----------------\n"
    f"Total Votes: {totalvotes}\n"
    f"----------------------------------\n"
    f"Khan: {((Khantotal/totalvotes)*100)}:.3f% ({Khantotal}) \n" 
    f"Correy: {((Correytotal/totalvotes)*100)}:.3f}% ({Correytotal}) \n" 
    f"Li: {((Litotal/totalvotes)*100)}:.3f}% ({Litotal}) \n" 
    f"OTooley: {((Tooleytotal/totalvotes)*100)}:.3f}% ({Tooleytotal}) \n" 
    f"-----------------\n"
    f"Winner: {Winner}\n")

# Print results (to terminal)
print(output)

#Print the results to analysis text file
with open(file_to_output, "w") as txt_file:
    #txt_file.write(output)