# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 21: Bar chart of mobile game ratings

import matplotlib.pyplot as plt   # matplotlib is used to draw graphs

games = ['Pubg', 'FreeFire', 'MineCraft', 'GTA-V', 'Call of Duty', 'FIFA 22']
rating = [4.5, 4.8, 4.7, 4.6, 4.1, 4.3]

plt.bar(games, rating, color='skyblue')

plt.xlabel('Games')                 # label for x-axis
plt.ylabel('Rating')                # label for y-axis
plt.title('Ratings of Mobile Games')
plt.xticks(rotation=20)             # tilt names so they don't overlap

plt.show()
