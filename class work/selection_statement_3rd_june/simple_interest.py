p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

if p > 0 and r > 0 and t > 0:
    si = (p * r * t) / 100
    print("Simple Interest =", si)
else:
    print("Invalid Input! Values must be greater than 0.")