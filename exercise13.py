import pandas as pd
import numpy as N

df = pd.read_csv('C:\\Koulu\\Statistical Data Analysis\\13-data.csv')


df.loc[df.location == '33100', 'location'] = 'Tampere'
df.loc[df.location == '20100', 'location'] = 'Turku'

df['sex'] = df['sex'].str.replace('nale', 'male')

#convert retention_time data into flaot type 
df['retention_time'] = df['retention_time'].astype(float)

df.loc[df.retention_time < 0, 'retention_time'] = N.nan

#count all rows
print("Number of observations: ", len(df))


#replace all missing values with 0
df['purchases'] = df['purchases'].fillna(0)

grouped = df.groupby(['sex', 'location'])
for name, group in grouped:
    print(name)
    print(group)
#replace all NaN values in grouped retention data with median imputation 
df['retention_time'] = grouped['retention_time'].transform(lambda x: x.fillna(x.median()))

for name, group in grouped:
    print(name)
    print(group)


