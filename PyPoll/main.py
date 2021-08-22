#Week3 homework Py Poll 
print("Election Results")
print("----------------------------")
import os
from numpy import printoptions
import pandas as pd 
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
df=pd.read_csv(csvpath)
df.head()
totalvotes=len(df.index)
print("Total Votes:"+str(totalvotes))
candidatedetails=df.groupby('Candidate').count()['Voter ID']
print(candidatedetails)