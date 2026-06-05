#ATM Transaction History Analysis
# # Transaction list
transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0

deposits = []      # Store deposits
withdrawals = []   # Store withdrawals

# Initial values
largest_deposit = transactions[0]
largest_withdrawal = transactions[1]

for amount in transactions:

    # Calculate balance
    balance += amount

    # Deposit
    if amount > 0:

        deposits.append(amount)

        # Find largest deposit
        if amount > largest_deposit:
            largest_deposit = amount

    # Withdrawal
    else:

        withdrawals.append(amount)

        # Find largest withdrawal
        if amount < largest_withdrawal:
            largest_withdrawal = amount

print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)