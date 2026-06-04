# Read how many numbers will be provided
n = int(input("How many numbers: "))

# `current` tracks length of current strictly increasing run
current = 1
# `longest` stores maximum run length seen so far
longest = 1

# Read the first number to initialize comparisons
prev = int(input("Enter number: "))

# Iterate over the remaining n-1 numbers
for i in range(n - 1):
    num = int(input("Enter number: "))

    # If the sequence is increasing, extend current run
    if num > prev:
        current += 1
    else:
        # Reset current run when sequence is not increasing
        current = 1

    # Update longest if current run exceeded it
    if current > longest:
        longest = current

    # Prepare for next iteration
    prev = num

# Print the length of the longest strictly increasing contiguous subsequence
print("Longest Sequence Length =", longest)