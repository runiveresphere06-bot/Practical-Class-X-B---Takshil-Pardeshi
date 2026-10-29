# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 2: Mean, median and mode using NumPy
# NumPy has mean() and median(), but no mode(), so we find the mode
# with np.unique() (counts how many times each value appears).

import numpy as np

data = np.array([4, 7, 2, 9, 7, 5, 7, 3, 2, 8])

mean = np.mean(data)
median = np.median(data)

values, counts = np.unique(data, return_counts=True)
mode = values[np.argmax(counts)]     # value with the highest count

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
