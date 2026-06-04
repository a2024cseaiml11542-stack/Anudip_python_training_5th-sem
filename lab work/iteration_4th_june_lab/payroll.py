# Read employee details
name = input("Enter Employee Name: ")
# Basic salary is required as a numeric value
basic = float(input("Enter Basic Salary: "))

# Calculate allowances and deductions
# House Rent Allowance (HRA) = 20% of basic
hra = basic * 0.20
# Dearness Allowance (DA) = 10% of basic
da = basic * 0.10
# Provident Fund (PF) deduction = 12% of basic
pf = basic * 0.12

# Compute gross and net salary
gross_salary = basic + hra + da
net_salary = gross_salary - pf

# Determine grade based on net salary
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Output results (rounded for readability)
print("\nEmployee Name:", name)
print("Gross Salary:", round(gross_salary, 2))
print("Net Salary:", round(net_salary, 2))
print("Grade:", grade)