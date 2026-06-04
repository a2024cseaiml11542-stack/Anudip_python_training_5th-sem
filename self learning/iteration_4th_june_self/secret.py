code = input("Enter 6 digit code: ")

# Ensure code is exactly 6 digits and numeric
if len(code) == 6 and code.isdigit():

    # Sum first three digits and last three digits
    first = int(code[0]) + int(code[1]) + int(code[2])
    last = int(code[3]) + int(code[4]) + int(code[5])

    # If sums match, the code is considered valid (simple checksum)
    if first == last:
        print("Valid Code")
    else:
        print("Invalid Code")

else:
    # Input was not a 6-digit numeric string
    print("Invalid Code")