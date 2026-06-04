# Simple ATM simulator
# - Shows a menu repeatedly
# - Allows checking balance, depositing, withdrawing, or exiting

# Initial account balance (in rupees)
balance = 10000

while True:
    # Display menu options to the user
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Read user's menu choice. Note: converting directly with int()
    # will raise ValueError if the input is not an integer.
    choice = int(input("Enter choice: "))

    if choice == 1:
        # Option 1: display current balance
        print("Balance: ₹", balance)

    elif choice == 2:
        # Option 2: deposit money into the account
        # Convert input to int; no validation for negative amounts here.
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 3:
        # Option 3: withdraw money from the account
        amount = int(input("Enter amount to withdraw: "))

        # Check if sufficient funds are available
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        # Option 4: exit the loop and end the program
        print("Thank You")
        break

    else:
        # Any other numeric choice is invalid
        print("Invalid Choice")