import pandas as pd


# get the column names from the names file
with open ('C:\\Koulu\\Statistical Data Analysis\\allbp.names', 'r') as f:
    # read the file lines starting from the 11th line and only include the characters before the : sign
    names = [line.split(':')[0] for line in f.readlines()[10:]]
 
    names.append("Increased binding protein, decreased binding protein, negative.")

# load data from data file and use the names as column names    
data = pd.read_csv('C:\\Koulu\\Statistical Data Analysis\\allbp.data', names = names)

data.info()

#output the number of observations  
print("Number of observations: ", len(data))

#output the number of variables
print("Number of variables: ", len(data.columns))

#get variable names
print("Variable names: ", data.columns)

# Print the amount of missing values in each variable. Missing value is denoted by a question mark.
print("Missing values: \n", data.isin(['?']).sum())

# output the amount of missing values. 
print("Number of missing values: ", data[data == '?'].count().sum())

# find all columns where the possible values are either 't' or 'f'.
boolean_columns = []
for column in data.columns:
    if data[column].isin(['t', 'f']).all():
        boolean_columns.append(column)

#Calculate the number of yes values divided by the number of observations for each of these columns.
for i in boolean_columns:
    print("Number of true values in column:", i, "divided by the number of observations: ", data[i].isin(['t']).sum() / len(data))


def calculate(column):
    sum_of_squares = 0
    for i in data[column]:
        if i != '?':
            sum_of_squares += float(i)**2

    #check if all values are missing
    if sum_of_squares == 0:
        print("All values are missing in column: ", column)
    else:        
        print("Sum of squared values in column:" ,column, "divided by the number of not missing values: ", sum_of_squares / (len(data) - data[column].isin(['?']).sum()))

calculate('TSH')
calculate('T3')
calculate('TT4')
calculate('T4U')
calculate('FTI')
calculate('TBG')

def calculate_ratio(column):
    sum = 0 
    for i in data[column]:
        if i != '?':
            sum += float(i) 
    return sum / (len(data) - data[column].isin(['?']).sum()) 

#Calculate mean ratio between T3 and TT4
print("Mean ratio between T3 and TT4: ", (calculate_ratio('T3') + calculate_ratio('TT4')) / 2)