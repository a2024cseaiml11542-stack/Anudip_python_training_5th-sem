# Read electricity units consumed from user
units = int(input("Enter units consumed: "))

# Compute bill using slab rates:
# - First 100 units: ₹5 per unit
# - Next 100 units (101-200): ₹7 per unit
# - Above 200 units: ₹10 per unit
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Apply a 10% surcharge if bill exceeds ₹5000
if bill > 5000:
    bill = bill + (bill * 0.10)

# Print the final bill amount
print("Final Bill = ₹", bill)