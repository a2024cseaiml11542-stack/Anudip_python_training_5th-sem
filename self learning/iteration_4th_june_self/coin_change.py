# Read the amount to change (integer rupee amount)
amount = int(input("Enter amount: "))

# Available note denominations (largest to smallest) for a greedy algorithm
notes = [500, 200, 100, 50, 20, 10]

# For each denomination, determine how many notes of that value are needed
for note in notes:
    count = amount // note

    # Print only denominations that are used
    if count > 0:
        print(note, "x", count)

    # Reduce the remaining amount by the value covered
    amount = amount % note