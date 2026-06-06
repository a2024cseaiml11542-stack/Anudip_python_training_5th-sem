"""..... Online Quiz Evaluation.......

Correct answers:
correct = ['A', 'C', 'B', 'D', 'A']
Student answers:
student = ['A', 'B', 'B', 'D', 'C']
Write a program to:
• Calculate score. 
• Display incorrectly answered question numbers. 
• Count correct and wrong answers. 
• Determine pass/fail (minimum 60%)."""

correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']
# Task 1: Calculate score
score = 0
for i in range(len(correct)):
    if student[i] == correct[i]:
        score += 1
print("Score:", score)
# Task 2: Display incorrectly answered question numbers
print("Incorrectly answered question numbers:")
for i in range(len(correct)):
    if student[i] != correct[i]:
        print(i + 1)
# Task 3: Count correct and wrong answers
correct_count = 0
wrong_count = 0
for i in range(len(correct)):
    if student[i] == correct[i]:
        correct_count += 1
    else:
        wrong_count += 1
print("Correct answers:", correct_count)
print("Wrong answers:", wrong_count)
# Task 4: Determine pass/fail (minimum 60%)
total_questions = len(correct)
percentage = (score / total_questions) * 100
if percentage >= 60:
    print("Pass")
else:
    print("Fail")
    