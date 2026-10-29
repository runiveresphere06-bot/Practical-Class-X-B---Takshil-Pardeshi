# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 5: Read a CSV file and display 10 rows
# Put your own CSV file in the 'data' folder and change the file name below.

import pandas as pd

df = pd.read_csv('../data/students.csv')   # read the CSV file

print("First 10 rows of the CSV file:")
print(df.head(10))                         # head(10) shows the first 10 rows
