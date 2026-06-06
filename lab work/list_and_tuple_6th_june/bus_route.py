"""...... Bus Route Monitoring.....

Passenger count at each stop:
passengers = [12, 18, 25, 30, 28, 15, 8]
Write a program to:
• Find the busiest stop. 
• Display stops with fewer than 10 passengers. 
• Calculate average passengers. 
• Determine whether any stop exceeded 25 passengers."""
passengers = [12, 18, 25, 30, 28, 15, 8]
# Task 1: Find the busiest stop
busiest = max(passengers)

print("Busiest Stop Passengers:", busiest)
# Task 2: Display stops with fewer than 10 passengers

print("Stops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Task 3: Calculate average passengers
total = 0

for p in passengers:
    total += p

average = total / len(passengers)

print("Average Passengers:", average)
# Task 4: Determine whether any stop exceeded 25 passengers

found = False

for p in passengers:
    if p > 25:
        found = True
        break

if found:
    print("A stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")