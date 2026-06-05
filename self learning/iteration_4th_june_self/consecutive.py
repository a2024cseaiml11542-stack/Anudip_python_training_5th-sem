# This program checks whether the digits of the entered number
# form a sequence of consecutive increasing digits.
# Examples: 1234 -> Consecutive, 135 -> Not a Consecutive

num = input("Enter a number: ")

# Assume the number is consecutive until we find evidence otherwise
flag = True

for i in range(len(num) - 1):
    # Compare each digit to the next one
    if int(num[i + 1]) != int(num[i]) + 1:
        flag = False
        break

if flag:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")