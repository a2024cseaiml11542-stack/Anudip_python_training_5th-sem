a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a > 0 and b > 0 and c > 0:

    if (a + b > c) and (a + c > b) and (b + c > a):

        print("The sides form a triangle.")

        if a == b == c:
            print("Type: Equilateral Triangle")

        elif a == b or b == c or a == c:
            print("Type: Isosceles Triangle")

        else:
            print("Type: Scalene Triangle")

    else:
        print("The sides do NOT form a triangle.")

else:
    print("Invalid input! Sides must be greater than 0.")