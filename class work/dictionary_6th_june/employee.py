# Employee Salary Management
employees ={}
# Input employee details (ID and Salary) for 10 employees
for i in range(11):
    emp_id = int(input("Enter Employee ID: "))
    emp_salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {"Salary": emp_salary}
    #Display total no. of employees whose salary is above 30000
print("\n No. Employees with Salary above 30000:")
count = 0
for emp_id in employees:
    if employees[emp_id]["Salary"] > 30000:
         break
    count += 1
print(count)
#Display the  list if the employees whose salary is<20000
print("\n Employees with Salary below 20000:")
list_below_20000 = []
for emp_id in employees:    
    if employees[emp_id]["Salary"] < 20000:
        list_below_20000.append(emp_id)

print("Employee ID:", list_below_20000)
