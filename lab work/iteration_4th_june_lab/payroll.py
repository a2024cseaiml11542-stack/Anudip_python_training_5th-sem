name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

gross_salary = basic + hra + da
net_salary = gross_salary - pf

if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

print("\nEmployee Name:", name)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)
print("Grade:", grade)