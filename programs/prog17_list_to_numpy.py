# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 17: Convert a Python list to a NumPy array

import numpy as np

my_list = [10, 20, 30, 40, 50]          # a normal Python list
print("Python list:", my_list)
print("Type:", type(my_list))

arr = np.array(my_list)                 # np.array() converts list -> NumPy array
print("\nNumPy array:", arr)
print("Type:", type(arr))
