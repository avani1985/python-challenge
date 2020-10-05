import os
import csv

#define the locations of input and output files
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "Output.txt")

# Define the 'budgetData' parameters

totalmonths = 0
changemonths = []
netchangelist = []
increase = ["",0]
decrease = ["",9999999999999]
nettotal = 0

# Read the csv and header row
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    first_row = next(csvreader)
    totalmonths += 1
    nettotal += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        #totals
        totalmonths += 1
        nettotal += int(row[1])

        #changes
        netchange = int(row[1]) - prev_net
        prev_net = int(row[1])
        netchangelist += [netchange]

        #decrease
        if netchange < decrease[1]: 
            decrease[0] = row[0]
            decrease[1] = netchange

         #increase
        if netchange > increase[1]:
            increase[0] = row[0]
            increase[1] = netchange
     
        # Average Net Change  (IS THIS NOT SUPPOSED TO BE PART OF LOOP?- is this calculated correctly in the output to terminal?)
        monthly_avg = sum(netchangelist) / len(netchangelist)




# generate Output (THIS IS AFTER THE LOOP!!)
output = (
    f"Financial Analysis\n"
    f"-----------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${nettotal}\n"
    f"Average Change: $ {monthly_avg}\n"
    f"Greatest Increase in Profits: {increase[0]} ($ {increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} ($ {decrease[1]})\n")

# Print all of the results (to terminal)
print(output)

# Print the results to analysis text file (THIS HAS ERROR- does the file already needs to be created?)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
