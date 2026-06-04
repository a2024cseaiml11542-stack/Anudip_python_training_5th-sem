# Read an integer from the user
num = int(input("Enter a number: "))

# Collect all factors of `num` in a list
factors = []

# Check divisibility for each integer from 1 to num
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

# A prime number has exactly two factors: 1 and itself
if len(factors) == 2:
    print(num, "is a Prime Number")
else:
    # Print the factors and indicate non-prime
    print("Factors:", *factors)
    print(num, "is not a Prime Number")