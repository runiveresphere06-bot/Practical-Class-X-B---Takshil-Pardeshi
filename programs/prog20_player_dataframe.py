# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 20: DataFrame named 'player'
# Columns: team, matches, runs, average. Row index = player name.
# Display only the players whose runs are more than 1000.

import pandas as pd

data = {
    'team': ['India', 'India', 'Australia', 'England', 'South Africa'],
    'matches': [254, 190, 168, 210, 120],
    'runs': [12169, 9115, 5400, 800, 950],
    'average': [59.1, 48.5, 34.2, 28.0, 31.5]
}

player_names = ['Virat', 'Rohit', 'Smith', 'Root', 'De Kock']

player = pd.DataFrame(data, index=player_names)

print("All players:")
print(player)

# Filter: keep only rows where runs > 1000
print("\nPlayers with runs more than 1000:")
print(player[player['runs'] > 1000])
