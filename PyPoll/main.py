#Week3 homework Py Poll 
import os
import pandas as pd 
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
df=pd.read_csv(csvpath)
df.head()
#calculate total votes from the counts of rows 
totalvotes=len(df.index)
#group cadidates 
votes_per_candidate=df.groupby('Candidate').count()
#adding a new column in the new dataframe to show the percentage 
votes_per_candidate['percentage']=votes_per_candidate['Voter ID']/totalvotes


#Specify the file to write to
output_path = os.path.join("Analysis", "result.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(["Total Votes:"+str(totalvotes)])
    csvwriter.writerow(['----------------------------'])
    for x,row in votes_per_candidate.iterrows():
        csvwriter.writerow([f"{x}: {row['percentage']:2.3%} ({row['Voter ID']})"])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f"Winner: {votes_per_candidate['Voter ID'].idxmax(axis=0)}"])
    csvwriter.writerow(['----------------------------'])

# print readed csv 
with open(output_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row[0])
    




