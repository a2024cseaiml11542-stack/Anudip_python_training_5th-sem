""" Employee Salary Processing......

Employee data is stored as tuples:
employees = [
 ("Rahul", 35000),
 ("Priya", 55000),
 ("Amit", 42000),
 ("Neha", 65000)
]
Write a program to:
• Display employees earning above ₹50,000. 
• Find the highest-paid employee. 
• Calculate total salary expenditure. 
• Count employees earning below ₹40,000."""

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Employees earning above ₹50,000
print("Employees earning above 50,000:")

for name, salary in employees:
    if salary > 50000:
        print(name, "-", salary)

# Find highest-paid employee
highest_paid = employees[0]

for employee in employees:
    if employee[1] > highest_paid[1]:
        highest_paid = employee

print("\nHighest Paid Employee:")
print(highest_paid[0], "-", highest_paid[1])

# Calculate total salary expenditure
total_salary = 0

for name, salary in employees:
    total_salary = total_salary + salary

print("\nTotal Salary Expenditure =", total_salary)

# Count employees earning below ₹40,000
count = 0

for name, salary in employees:
    if salary < 40000:
        count = count + 1

print("\nEmployees earning below 40,000 =", count)