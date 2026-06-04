# Read integer input from the user
num = int(input("Enter a number: "))

# Use a copy of `num` for digit extraction so original stays intact
temp = num

# Number of digits in `num` determines the power used
digits = len(str(num))
# Accumulate sum of each digit raised to `digits`
sum1 = 0

while temp > 0:
    # Extract last digit
    digit = temp % 10
    # Add digit**digits to running total
    sum1 += digit ** digits
    # Remove last digit
    temp //= 10

# If sum equals the original number it's an Armstrong number
if sum1 == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")