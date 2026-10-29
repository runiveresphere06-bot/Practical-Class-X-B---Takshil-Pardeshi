# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 19: DataFrame of candidates who appeared in interviews
# Columns: name, score, attempts, qualify (Yes/No)
# Row index: C001, C002, ...

import pandas as pd   # pandas is used to create DataFrames (tables)

data = {
    'name': ['Aarav', 'Diya', 'Rohan', 'Sneha', 'Kabir',
             'Meera', 'Arjun', 'Isha', 'Vivaan', 'Anaya'],
    'score': [12.5, 9.0, 16.5, 9.0, 20.0, 14.5, 8.0, 19.0, 11.5, 15.0],
    'attempts': [1, 3, 2, 3, 3, 1, 2, 1, 2, 1],
    'qualify': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
}

# Custom row labels C001, C002, ...
labels = ['C001', 'C002', 'C003', 'C004', 'C005',
          'C006', 'C007', 'C008', 'C009', 'C010']

df = pd.DataFrame(data, index=labels)

print("Candidates DataFrame:")
print(df)
