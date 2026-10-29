# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 18: Create a 3x3 matrix with values from 11 to 30
# A 3x3 matrix holds 9 values, so we take 9 numbers starting from 11
# (11, 12, ... 19). np.arange(start, stop) does not include 'stop'.

import numpy as np

matrix = np.arange(11, 20).reshape(3, 3)   # reshape(3,3) -> 3 rows, 3 columns

print("3x3 Matrix:")
print(matrix)
