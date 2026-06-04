# Read integer input from user
num = int(input("Enter a number: "))

# `temp` is used to iterate over digits without modifying `num`
temp = num
# Accumulate sum of factorials of each digit
sum1 = 0

while temp > 0:
    # Extract the last digit
    digit = temp % 10

    # Compute factorial of the current digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    # Add factorial to running total and remove last digit
    sum1 += fact
    temp //= 10

# A strong number equals the sum of factorials of its digits
if sum1 == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")