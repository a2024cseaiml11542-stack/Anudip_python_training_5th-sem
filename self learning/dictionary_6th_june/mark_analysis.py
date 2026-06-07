"""  Student Marks Analysis
Sample Data
marks = {
 "Aarav": 78,
 "Diya": 92,
 "Rohan": 45,
 "Ishita": 88,
 "Kabir": 56,
 "Meera": 39,
 "Arjun": 95,
 "Saanvi": 67,
 "Vivaan": 82,
 "Anaya": 51
}
Tasks
• Display students scoring 80 or above. 
• Count the number of students who failed (marks < 40). 
• Find the highest scorer. 
• Create a list of students scoring between 60 and 75. 
• Assign grades: 
o A: ≥ 90 
o B: 75–89 
o C: 50–74 
o F: < 50"""
#
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Students scoring 80 or above
print("Students scoring 80 or above:")
for name, score in marks.items():
    if score >= 80:
        print(name, score)

# Count failed students
fail_count = 0
for score in marks.values():
    if score < 40:
        fail_count += 1

print("Failed Students =", fail_count)

# Highest scorer
highest_student = max(marks, key=marks.get)
print("Highest Scorer =", highest_student, marks[highest_student])

# Students scoring between 60 and 75
students = []

for name, score in marks.items():
    if 60 <= score <= 75:
        students.append(name)

print("Students scoring between 60 and 75 =", students)

# Grades
print("\nGrades:")

for name, score in marks.items():

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 50:
        grade = "C"

    else:
        grade = "F"

    print(name, ":", grade)