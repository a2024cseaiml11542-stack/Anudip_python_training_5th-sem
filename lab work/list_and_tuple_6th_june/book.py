'''....Library Book Search.....

Books available in a library:
books = [
 ("Python Basics", 5),
 ("Data Science", 0),
 ("Java Programming", 3),
 ("Machine Learning", 0)
]
Write a program to:
• Display unavailable books. 
• Find all books with more than 2 copies. 
• Count available books. 
• Stop searching once a requested book is found.'''
books = [
    ("Python Basics", 5), 
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]
# Task 1: Display unavailable books
print("Unavailable Books:")
for title, copies in books:
    if copies == 0:
        print(title)
# Task 2: Find all books with more than 2 copies
print("\nBooks with more than 2 copies:")
for title, copies in books:
    if copies > 2:
        print(title)
# Task 3: Count available books
available_count = 0
for title, copies in books:
    if copies > 0:
        available_count += 1
print("\nAvailable Books:", available_count)
# Task 4: Stop searching once a requested book is found
requested_book = input("Enter the book name: ")

found = False

for title, copies in books:
    if title.lower() == requested_book.lower():
        print(f"\nRequested Book Found: {title} ({copies} copies available)")
        found = True
        break

if not found:
    print(f"\nRequested Book Not Found: {requested_book}")