# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

passed = []      # Passed students
failed = 0       # Failed student count
merit = []       # Marks above 75

# Assume first mark is highest and lowest
highest = marks[0]
lowest = marks[0]

for mark in marks:

    # Check pass or fail
    if mark >= 40:
        passed.append(mark)
    else:
        failed += 1

    # Find highest mark
    if mark > highest:
        highest = mark

    # Find lowest mark
    if mark < lowest:
        lowest = mark

    # Add marks above 75 to merit list
    if mark > 75:
        merit.append(mark)

print("Passed Students:", passed)
print("Failed Count:", failed)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit)