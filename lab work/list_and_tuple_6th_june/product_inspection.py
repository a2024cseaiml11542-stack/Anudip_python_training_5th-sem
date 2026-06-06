""".....Warehouse Product Inspection.....

Problem Statement
Product IDs and quality status:
products = [
 (101, "Pass"),
 (102, "Fail"),
 (103, "Pass"),
 (104, "Fail"),
 (105, "Pass")
]
Write a program to:
• Display failed product IDs. 
• Count passed and failed products. 
• Calculate pass percentage. 
• Stop checking if 3 failures are found."""
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0
# Task 1: Display failed product IDs

print("Failed Product IDs:")

# Task 2: Count passed and failed products
for pid, status in products:

    if status == "Fail":
        print(pid)
        fail_count += 1
    else:
        pass_count += 1

print("Passed Products:", pass_count)
print("Failed Products:", fail_count)
# Task 3: Calculate pass percentage
percentage = (pass_count / len(products)) * 100

print("Pass Percentage:", percentage)

# Task 4: Stop checking if 3 failures are found

failures = 0

for pid, status in products:

    if status == "Fail":
        failures += 1

    if failures == 3:
        print("3 failures found. Stopping...")
        break