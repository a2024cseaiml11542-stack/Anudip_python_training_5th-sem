"""A batsman's scores in different matches are stored in a list.
scores = [45, 78, 12, 100, 67, 8, 90, 55]
Write a program to:
• Count half-centuries and centuries. 
• Find the highest score. 
• Display all scores below 20. 
• Calculate the average score."""
scores = [45, 78, 12, 100, 67, 8, 90, 55]
# Task 1: Count half-centuries and centuries
half_centuries = 0  
centuries = 0
# A half-century is a score between 50 and 99, while a century is 100 or more.
for score in scores:
    if score >= 50 and score < 100:
        half_centuries += 1
    elif score >= 100:
        centuries += 1

print("Half-centuries:", half_centuries)
print("Centuries:", centuries)

# Task 2: Find the highest score
highest_score = max(scores)
print("Highest score:", highest_score)

# Task 3: Display all scores below 20
print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score)

# Task 4: Calculate the average score
average_score = sum(scores) / len(scores)
print("Average score:", average_score)