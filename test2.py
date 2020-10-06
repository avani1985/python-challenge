import os
import csv

#define the locations of input and output files
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "Output.txt")

totalvotes = 0
C1total =0
C2total =0
C3total =0
C4total =0

with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        
        #total votes cast
        totalvotes += 1

        #getting the individual votes
        if(len(row[2]) > len(first_row[2]):
            C1total += 1
            C1= row[2]

            elif (len(row[2]) > len(first_row[2]):
                C2total += 1
                C2= row[2]
            elif (len(row[2]) > len(first_row[2]):
                C3total += 1
                C3= row[2]
            elif (len(row[2]) > len(first_row[2]):
                C4total += 1
                C4= row[2]

print(totalvotes)


# generate Output
#output = (

    #f"Election Results\n"
    #f"-----------------\n"
    #f"Total Votes: {totalvotes}\n"
    #f"-----------------\n"
    #f"Khan: {((C1total/totalvotes)*100)}:.3f% ({C1total}) \n" 

    #f"Correy: {((C2total/totalvotes)*100)}:.3f% ({C2total}) \n" 

    #f"Li: {((C3total/totalvotes)*100)}:.3f% ({C3total}) \n" 

    #f"OTooley: {((C4total/totalvotes)*100)}.3f% ({C4total}) \n" 

    #f"-----------------\n"
    #f"Winner: {Winner}\n)"


# Print results (to terminal)
# #print(output)

# Print the results to analysis text file
#with open(file_to_output, "w") as txt_file:
    #txt_file.write(output)
