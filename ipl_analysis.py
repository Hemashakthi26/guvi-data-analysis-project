# IPL Analysis Project

import pandas as pd
import matplotlib.pyplot as plt

print("=== IPL Analysis Started ===\n")

#Loading data
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print("Data Loaded Successfully!")
print("Matches shape:", matches.shape)
print("Deliveries shape:", deliveries.shape)
print("\nFirst 5 rows of matches:\n", matches.head())

#Team win counts
print("\nTop 5 Winning Teams:")
top_teams = matches['winner'].value_counts().head(5)
print(top_teams)

# Plot top 5 winning teams
top_teams.plot(kind='bar', color='skyblue')
plt.title("Top 5 Winning Teams")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.show()

#Top run scorers
print("\nTop 5 Batsmen by Total Runs:")
batsman_runs = deliveries.groupby('batsman')['batsman_runs'].sum()
top_batsmen = batsman_runs.sort_values(ascending=False).head(5)
print(top_batsmen)

# Plot top 5 batsmen
top_batsmen.plot(kind='bar', color='orange')
plt.title("Top 5 Batsmen")
plt.xlabel("Batsman")
plt.ylabel("Total Runs")
plt.show()

# Top wicket takers
print("\nTop 5 Bowlers by Wickets:")
# Wickets are counted as non-zero dismissal types except 'run out'
wickets = deliveries[deliveries['dismissal_kind'].notna()]
wickets = wickets[wickets['dismissal_kind'] != 'run out']
top_bowlers = wickets['bowler'].value_counts().head(5)
print(top_bowlers)

# Ploting top 5 bowlers
top_bowlers.plot(kind='bar', color='green')
plt.title("Top 5 Bowlers")
plt.xlabel("Bowler")
plt.ylabel("Wickets")
plt.show()

#Matches per season
print("\n Matches Played Per Season:")
matches_per_season = matches['season'].value_counts().sort_index()
print(matches_per_season)

# Ploting matches per season
matches_per_season.plot(kind='bar', color='purple')
plt.title("Matches Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.show()

# Match Winner Prediction
#Team with most wins in history is predicted as winner
def predict_winner(team1, team2):
    wins = matches['winner'].value_counts()
    if wins.get(team1,0) > wins.get(team2,0):
        return team1
    elif wins.get(team2,0) > wins.get(team1,0):
        return team2
    else:
        return "Draw or Toss Factor"

print("\nSample Winner Prediction:")
sample_team1 = "Mumbai Indians"
sample_team2 = "Chennai Super Kings"
predicted_winner = predict_winner(sample_team1, sample_team2)
print(f"Predicted Winner between {sample_team1} and {sample_team2}: {predicted_winner}")

print("\n=== IPL Analysis Finished ===")
