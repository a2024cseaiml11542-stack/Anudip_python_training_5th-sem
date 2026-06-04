# Read the number as a string so we can slice its digits
num = input("Enter a number: ")

# Split the string into two halves at the middle index
# For odd-length strings the middle digit goes to the right half
mid = len(num) // 2

left = num[:mid]
right = num[mid:]

# If left and right halves are identical it's considered a mirror number
if left == right:
    print("Mirror Number")
else:
    print("Not a Mirror Number")