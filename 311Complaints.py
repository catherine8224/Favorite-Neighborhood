import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("311_Service_Requests_from_2010_to_Present.csv")

##Count = df.groupby(['Complaint Type']).size().reset_index(name='counts')
##poop = Count.sort_values('counts', ascending=False)
##print(poop.head(10))

##df = df.groupby(['Complaint Type']).size().rename(columns={'Complaint Type': 'count'})
###df = df.sort_values('count', ascending=False)
##print(df)

top311 = df['Complaint Type'].value_counts()[:10]
print("The 10 most pressing complaints to the 311 in my neighborhood last year:")
print(top311)

agency = df['Agency Name'].value_counts()
print(agency)
