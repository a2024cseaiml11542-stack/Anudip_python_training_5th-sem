# Electricity bill calculator
# Reads the number of units consumed and computes the total bill
# according to slabbed rates. Finally, prints the bill and category.

# NOTE: `int()` will raise ValueError for non-integer input.
units = int(input("Enter units consumed: "))

# Determine bill and category using consumption slabs:
# - 0..100 units:      ₹5 per unit
# - 101..200 units:    first 100 at ₹5, remaining at ₹7
# - 201+ units:        first 100 at ₹5, next 100 at ₹7, remaining at ₹10
if units <= 100:
    # All units charged at ₹5
    bill = units * 5
    category = "Low Consumption"

elif units <= 200:
    # First 100 @ ₹5, remaining (units-100) @ ₹7
    bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium Consumption"

else:
    # First 100 @ ₹5, next 100 @ ₹7, remaining (units-200) @ ₹10
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High Consumption"

# Output the results
print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Category:", category)