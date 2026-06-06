'''A company stores employee details in a tuple. Each employee record contains:
employees = (
 ("E101", "Anuj", 92),
 ("E102", "Rahul", 76),
 ("E103", "Priya", 58),
 ("E104", "Neha", 88),
 ("E105", "Amit", 45)
)
Where:
• First value = Employee ID 
• Second value = Employee Name 
• Third value = Performance Score 
Tasks
Write a Python program to:
1. Display details of employees scoring 80 or above. 
2. Count the number of employees who need improvement (score below 60). 
3. Find the employee with the highest score. 
4. Create a list containing the names of all employees scoring above 75. 
5. Display the performance category for each employee: 
o 90 and above → Excellent 
o 75 to 89 → Good 
o 60 to 74 → Average 
o Below 60 → Needs Improvement'''
employees = (
 ("E101", "Anuj", 92),
 ("E102", "Rahul", 76),
 ("E103", "Priya", 58),
 ("E104", "Neha", 88),
 ("E105", "Amit", 45)
)
# The `employees` tuple holds records of the form:
# (Employee ID, Employee Name, Performance Score)

# Task 1: Display details of employees scoring 80 or above
# We also count employees who need improvement (score below 60)
improvement_count = 0
for detail in employees:
    # `detail` is a tuple like ("E101", "Anuj", 92)
    # detail[2] is the performance score
    if detail[2] >= 80:
        # Print the full employee record when score is 80 or more
        print(detail)
    if detail[2] < 60:
        # Increment the counter for low-performing employees
        improvement_count += 1

print("Number of employees who need improvement:", improvement_count)

# Task 3: Find the employee with the highest score
# We keep track of the highest score seen and the corresponding name
highest_score = 0
employee_name = ""
for detail in employees:
    if detail[2] > highest_score:
        highest_score = detail[2]
        employee_name = detail[1]

print("Employee with highest score:", employee_name, "-", highest_score)

# Task 4: Create a list of names for employees scoring above 75
names_above_75 = []
for detail in employees:
    if detail[2] > 75:
        # Append only the employee's name (detail[1])
        names_above_75.append(detail[1])

print("Names of employees scoring above 75:", names_above_75)

# Task 5: Determine performance category for each employee
# We classify each score into a category and store (name, category) pairs
performance_category = []
for detail in employees:
    score = detail[2]
    name = detail[1]
    if score >= 90:
        performance_category.append((name, "Excellent"))
    elif score >= 75:
        performance_category.append((name, "Good"))
    elif score >= 60:
        performance_category.append((name, "Average"))
    else:
        performance_category.append((name, "Needs Improvement"))

print("Performance category for each employee:")
for category in performance_category:
    # category is a tuple like ("Anuj", "Excellent")
    print(category[0], ":", category[1])
