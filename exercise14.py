import pandas as pd
import numpy as N

dfh = pd.read_csv('C:\\Koulu\\Statistical Data Analysis\\14-helsinki.csv')
dfe = pd.read_csv('C:\\Koulu\\Statistical Data Analysis\\14-espoo.csv')


df = dfh.merge(dfe, on='date', how='outer')


#print amount of days that the data covers
print("Amount of days: ", len(df))

#print amount of non missing values in each column but ignore the first column
print("Amount of observation days in each street: \n", df.count()[1:])

#output the amount of days that there are observations for more than 1 column
print("Amount of days that there are observations for more than 1 column: ", len(df[df.count(axis=1) > 2]))

sum = 0 
for i in df.columns[1:]:
    addition = df[i].sum()
    if addition > sum: 
        sum = addition
        street = i
print("Busiest street: ", street, "with ", sum, "observations")

#drop all rows that have missing values
df = df.dropna()

sum = 0 
for i in df.columns[1:]:
    addition = df[i].sum()
    if addition > sum: 
        sum = addition
        street = i
print("Busiest street: ", street, "with ", sum, "observations")

