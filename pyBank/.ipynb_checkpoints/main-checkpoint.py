# importing the necessary libraries
import os
import csv
import numpy as np

## set/ define file path
pyBank_path = os.path.join(os.getcwd(), 'Resources', 'budget_data.csv')

pyBank_path

# reading the data from the csv file
data = []
with open(pyBank_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            data.append(row)
        line_count += 1

# converting the data list into numpy array
data = np.array(data) 

 # calculating the total number of months in the dataset
total_months = data.shape[0]

# getting the profits/losses from the dataset
profits_losses = data[:, 1].astype('int64') 
 # getting the sum of all profits/losses from the dataset
total_profit_loss = profits_losses.sum() 

# getting the change in profits/losses
changes = [profits_losses[i + 1] - profits_losses[i] for i in range(total_months - 1)] 
# getting the average of all the changes in profits/losses
average_change = round(sum(changes)/len(changes), 2) 

# getting the maximum change in profits
max_change = max(changes) 
max_change_index = changes.index(max_change)
# getting date of maxmimun increase in profit
max_change_date = data[max_change_index + 1, 0] 

# getting the maximum change in losses
min_change = min(changes) 
min_change_index = changes.index(min_change)
# getting date of maxmimun increase in loss
min_change_date = data[min_change_index + 1, 0] 

# final output
output_report = "Financial Analysis\n----------------------------\nTotal Months: " + str(total_months) + "\nTotal: $" + str(total_profit_loss) + "\nAverage  Change: $" + str(average_change) + "\nGreatest Increase in Profits: " + str(max_change_date) + " ($" + str(max_change) + ")\nGreatest Decrease in Profits: " + str(min_change_date) + " ($" + str(min_change) + ")"

print(output_report)

f = open('Analysis/analysis.txt', 'w')
f.write(output_report)
f.close()