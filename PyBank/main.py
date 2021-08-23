#Week3 homework Py Bank
import os 
import csv
#find relative csv path ( compared with current main.py file)
csvpath = os.path.join('Resources', 'budget_data.csv')
#open csv file 
with open(csvpath) as budgetfile:
    # CSV reader to read the file with delimiter  (default delimiter is comma )
    budgetreader = csv.reader(budgetfile,delimiter=',')
    #Skip header 
    next(budgetreader)  
    #make the csv a list and name it as data 
    data=list(budgetreader)
    #list comprehension to exact each colomn, no specific type for date, hence set it as string 
    date = [str(row[0]) for row in data]
    profit_losses = [int(row[1]) for row in data]
    #The total number of months included in the dataset, use set to remove duplicates then use len function 
    total_month_count=len(set(date))
    #The net total amount of "Profit/Losses" over the entire period
    total_of_profit_losses =int(sum(profit_losses))
    #create new list for the changes in profit 
    change=[]
    for i in range(1,len(profit_losses)):
        change.append((int(profit_losses[i]) - int(profit_losses[i-1])))
    #using build function to calculate max, min, and average (round 2 decimal for average)
    average_change=round((sum(change)/len(change)),2)
    greatest_increase=max(change)
    greatest_decrease=min(change)

#Specify the file to write to
output_path = os.path.join("Analysis", "result.txt")
#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Reporting 
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months:"+str(total_month_count)])    
    csvwriter.writerow(["Total : $"+str(total_of_profit_losses)])
    csvwriter.writerow(["Average  Change: $"+str(average_change)])
    csvwriter.writerow(["Greatest Increase in Profits:"+str(date[change.index(max(change))+1]) + " " + "$" + str(greatest_increase)])
    csvwriter.writerow(["Greatest Decrease in Profits:"+str(date[change.index(min(change))+1]) + " " + "$" + str(greatest_decrease)])
# print readed csv 
with open(output_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row[0])
