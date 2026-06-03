length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

if length > 0 and breadth > 0:
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area =", area)
    print("Perimeter =", perimeter)
else:
    print("Invalid Input! Length and Breadth must be greater than 0.")