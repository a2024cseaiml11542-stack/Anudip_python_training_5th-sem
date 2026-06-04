correct_password = "admin123"

password = input("Enter Password: ")

while password != correct_password:
    print("Invalid Password.")
    password = input("Enter Password: ")

print("Login Successful!")