attendance = {}

# Input attendance of 30 students
for i in range(31):
    roll_no = int(input("Enter Roll Number: "))
    status = input("Enter Attendance (P/A): ").upper()

    attendance[roll_no] = status

# Display Present Students
print("\nStudents Present:")


for roll_no in attendance:
    if attendance[roll_no] == "P":
        print(roll_no)
# Display Absent Students
print("\nStudents Absent:") 
for roll_no in attendance:
    if attendance[roll_no] == "A":
        print(roll_no)
