"""
Count transactions meeting thresholds and compute total.

Input: repeated integer transaction amounts. Enter -1 to stop.
Outputs:
- number of transactions > 50000
- number of transactions < 1000
- total sum of transactions
"""

# Counters for the required thresholds and running total
above_50000 = 0
below_1000 = 0
total = 0

while True:

    # Read next transaction amount; -1 is sentinel to stop
    amount = int(input("Enter transaction (-1 to stop): "))

    if amount == -1:
        break

    # Update running total with the entered amount
    total += amount

    # Increment counters when thresholds are met
    if amount > 50000:
        above_50000 += 1

    if amount < 1000:
        below_1000 += 1

# Print the summary results
print("Transactions above ₹50000 =", above_50000)
print("Transactions below ₹1000 =", below_1000)
print("Total Transaction Amount =", total)