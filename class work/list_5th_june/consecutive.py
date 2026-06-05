# Number list
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

pairs = []

# Check consecutive numbers
for i in range(len(numbers) - 1):

  # Check if current number and next number are consecutive
    if numbers[i] + 1 == numbers[i + 1]:
# If they are consecutive, print the pair
        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store pair in new list
        pairs.append((numbers[i], numbers[i + 1]))

print("Consecutive Pairs:", pairs)