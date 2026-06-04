# Read number of racers
n = int(input("Enter number of racers: "))

# Collect lap times (float) for each racer
times = []

for i in range(n):
    t = float(input(f"Lap time of racer {i+1}: "))
    times.append(t)

# Determine fastest and slowest times
fastest = min(times)
slowest = max(times)

# Print positions (1-based) and time difference
print("Fastest Racer Position =", times.index(fastest) + 1)
print("Slowest Racer Position =", times.index(slowest) + 1)
print("Difference =", slowest - fastest)