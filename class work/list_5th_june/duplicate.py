# This simple script asks the user to enter 20 whole numbers
# and stores them in a list. Then it asks for a number `x`
# and removes every occurrence of `x` from the list.

# Create an empty list to hold the numbers
numbers = []

# Repeat 20 times and ask the user for a number each time
for i in range(20):
    # Read a number from the user, convert it to an integer, and add it to the list
    num = int(input("Enter a number: "))
    numbers.append(num)

# Show the list the user just entered
print("Original List:", numbers)

# Ask for the number to remove from the list

x = int(input("Enter the number to remove from the list: "))

# Remove all duplicatesof x except the first one from the list.
count = 0
# We will iterate through the list and count occurrences of `x`. If we find `x` more than once, we will remove it from the list.
i = 0

while i < len(numbers):
    if numbers[i] == x:
        count += 1

        if count > 1:
            # If we have already seen `x` once, we remove it from the list and do not increment `i` because the list has shifted left.
            numbers.pop(i)
            continue

    i += 1
# After the loop, we check how many times `x` was found and print the appropriate message.
if count == 0:
    print("Number not found in the list")
# If count is 1, it means `x` was found only once, so we inform the user that no duplicates were found.
elif count == 1:
    print("Number occurs only once, no duplicates found")
# If count is greater than 1, it means we removed duplicates, so we inform the user that duplicates were removed.
else:
    print("Duplicates removed")
print("Updated List:", numbers)