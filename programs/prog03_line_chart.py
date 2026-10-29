# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 3: Line chart from (2,5) to (9,10)

import matplotlib.pyplot as plt

x = [2, 9]       # x-coordinates of the two points
y = [5, 10]      # y-coordinates of the two points

plt.plot(x, y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart from (2,5) to (9,10)')
plt.show()
