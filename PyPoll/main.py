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

#reporting
print("Election Results")
print("----------------------------")
print("Total Votes:"+str(totalvotes))
print("----------------------------")
for x,row in votes_per_candidate.iterrows():
    print(f"{x}: {row['percentage']:2.3%} ({row['Voter ID']})")
print("----------------------------")
print(f"Winner: {votes_per_candidate['Voter ID'].idxmax(axis=0)}")
print("----------------------------")

