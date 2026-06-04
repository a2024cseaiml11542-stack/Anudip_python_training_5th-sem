# Read input as a string so we can compare characters/digits
num = input("Enter a number: ")

# Find the index where the sequence stops increasing (the peak)
# Initialize to -1 meaning 'no peak found yet'
peak = -1

for i in range(1, len(num)):
    # If current digit is not greater than previous, we've reached the peak
    if num[i] <= num[i - 1]:
        peak = i
        break

# If no peak was found, the sequence never decreased — not a mountain
if peak == -1:
    print("Not a Mountain Number")
else:
    # Verify strictly increasing up to peak and strictly decreasing after peak
    flag = True

    # Check strictly increasing property before the peak
    for i in range(1, peak):
        if num[i] <= num[i - 1]:
            flag = False

    # Check strictly decreasing property after the peak
    for i in range(peak + 1, len(num)):
        if num[i] >= num[i - 1]:
            flag = False

    # Final result based on both checks
    if flag:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")