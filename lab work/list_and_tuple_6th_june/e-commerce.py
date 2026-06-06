""" E-Commerce Order Analysis
Problem Statement
An online store records orders as:
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
Write a program to:
• Display all products costing more than ₹1000. 
• Find the most expensive product. 
• Calculate the total order value. 
• Count products costing below ₹1000."""
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
# Task 1: Display all products costing more than ₹1000
print("Products costing more than ₹1000:")
for product, price in orders:
    if price > 1000:
        print(f"- {product}: {price}")

# Task 2: Find the most expensive product
most_expensive_product = orders[0]
for product, price in orders:
    if price > most_expensive_product[1]:
        most_expensive_product = (product, price)

print(f"Most expensive product: {most_expensive_product[0]} - {most_expensive_product[1]}")

# Task 3: Calculate the total order value
total = 0

for product, price in orders:
    total = total + price

print("\nTotal Order Value =", total)

# Count products costing below ₹1000
count = 0

for product, price in orders:
    if price < 1000:
        count = count + 1

print("\nProducts costing below ₹1000 =", count)