# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 4: Scatter chart for (2,5), (9,10), (8,3), (5,7), (6,18)

import matplotlib.pyplot as plt

x = [2, 9, 8, 5, 6]
y = [5, 10, 3, 7, 18]

plt.scatter(x, y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Chart')
plt.show()
