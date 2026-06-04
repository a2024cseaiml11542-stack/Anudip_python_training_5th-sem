# Student result calculator
# Reads marks for 5 subjects, computes total, percentage, grade,
# and counts how many subjects were failed (marks < 40).

# Accumulators for total marks and failed subject count
total = 0
fail_count = 0

# Collect marks for 5 subjects from the user
for i in range(1, 6):
    # Convert input to int; this will raise ValueError on invalid input
    marks = int(input(f"Enter marks of subject {i}: "))
    total += marks

    # Count a failed subject (threshold: 40)
    if marks < 40:
        fail_count += 1

# Compute percentage assuming each subject is out of 100
percentage = total / 5

# Assign grade based on percentage slabs
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Output results
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Subjects Failed:", fail_count)