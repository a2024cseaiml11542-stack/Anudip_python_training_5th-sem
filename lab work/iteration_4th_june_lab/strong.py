num = int(input("Enter a number: "))
temp = num
sum1 = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum1 += fact
    temp //= 10

if sum1 == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")