a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("The sides form a triangle.")
    else:
        print("The sides do NOT form a triangle.")
else:
    print("Invalid input! Sides must be greater than 0.")