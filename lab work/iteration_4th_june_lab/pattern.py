# Read number of rows to generate the numeric patterns
rows = int(input("Enter number of rows: "))

# Print forward numeric triangle pattern
print("Pattern:")
for i in range(1, rows + 1):
    # Print numbers from 1 to i on the current line
    for j in range(1, i + 1):
        print(j, end="")
    # Move to next line after each row
    print()

# Print reverse numeric triangle pattern
print("\nReverse Pattern:")
for i in range(rows, 0, -1):
    # Print numbers from 1 to i on the current line (decreasing rows)
    for j in range(1, i + 1):
        print(j, end="")
    print()