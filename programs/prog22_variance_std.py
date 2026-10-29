# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 22: Variance and Standard Deviation of the given data

import numpy as np

data = [33, 44, 55, 67, 54, 22, 33, 44, 56, 78,
        21, 31, 43, 90, 21, 33, 44, 55, 87]

variance = np.var(data)    # variance = average of squared differences from mean
std_dev = np.std(data)     # standard deviation = square root of variance

print("Data:", data)
print("Mean:", round(np.mean(data), 2))
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std_dev, 2))
