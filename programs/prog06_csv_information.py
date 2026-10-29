# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 6: Read a CSV file and display its information

import pandas as pd

df = pd.read_csv('../data/students.csv')

print("Information about the CSV file:")
df.info()                                  # columns, data types, non-null counts

print("\nShape (rows, columns):", df.shape)
print("\nStatistical summary:")
print(df.describe())
