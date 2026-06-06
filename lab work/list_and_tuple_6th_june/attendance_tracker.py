'''..... Student Attendance Tracker......

Attendance for 15 days is recorded as:
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
Write a program to:
• Count present and absent days. 
• Calculate attendance percentage. 
• Determine eligibility (minimum 75% attendance). 
• Display positions where the student was absent.'''
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
# Task 1: Count present and absent days 
present = 0
absent = 0
for day in attendance:
    if day == 'P':
        present += 1
    elif day == 'A':
        absent += 1
print("Present days:", present)
print("Absent days:", absent)
# Task 2: Calculate attendance percentage

percentage = (present / len(attendance)) * 100
print("Attendance Percentage:", percentage)
# Task 3: Determine eligibility (minimum 75% attendance)
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")
# Task 4: Display positions where the student was absent 

print("Absent Positions:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)