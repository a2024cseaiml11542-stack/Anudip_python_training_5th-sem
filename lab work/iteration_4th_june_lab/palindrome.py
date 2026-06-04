# Palindrome checker for integers
# Reads an integer, computes its reverse, and compares to original.

# Read number from user (int conversion will raise on invalid input)
num = int(input("Enter a number: "))

# Make a copy to manipulate while preserving the original `num`
temp = num
# `reverse` will hold the reversed digits
reverse = 0

# Build the reversed number digit by digit
while temp > 0:
    # Extract the last digit
    digit = temp % 10
    # Append digit to the reversed number
    reverse = reverse * 10 + digit
    # Remove the last digit from temp (integer division)
    temp //= 10

# Show the reversed number
print("Reverse:", reverse)

# If reversed equals original, it's a palindrome
if reverse == num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")