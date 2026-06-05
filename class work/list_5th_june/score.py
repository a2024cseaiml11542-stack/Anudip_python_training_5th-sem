# Collect scores for 11 players and determine the highest score.

# List to store each player's score
player_Score = []

# Prompt the user to enter scores for 11 players (player 1 through player 11)
for i in range(11):
    # Read input, convert to integer, and append to the list
    player_Score.append(int(input(f"Enter the score of player {i+1}: ")))

# Display all collected scores
print("Player Scores:", player_Score)

# Compute and print the maximum score safely using the built-in `max()`
if player_Score:
    max_score = max(player_Score)
    print("Maximum Score:", max_score)
else:
    print("No scores entered.")
