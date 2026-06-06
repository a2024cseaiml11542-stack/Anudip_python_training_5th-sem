'''A flight reservation system stores passenger records as tuples:
bookings = (
 ("P101", "Delhi", "Confirmed"),
 ("P102", "Mumbai", "Waiting"),
 ("P103", "Delhi", "Confirmed"),
 ("P104", "Chennai", "Cancelled"),
 ("P105", "Mumbai", "Confirmed"),
 ("P106", "Delhi", "Waiting")
)
Where:
• Passenger ID 
• Destination 
• Booking Status 
Tasks
Write a Python program to:
1. Display all passengers whose booking status is Confirmed. 
2. Count the number of passengers travelling to Delhi. 
3. Count Confirmed, Waiting, and Cancelled bookings separately. 
4. Create a list containing passenger IDs with Waiting status. 
5. Determine which destination has the highest number of bookings.'''
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# --------------------------------------------------
# Task 1: Display all passengers whose booking is Confirmed

print("Confirmed Passengers:")

for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0], booking[1])

# --------------------------------------------------
# Task 2: Count passengers travelling to Delhi

delhi_count = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

# --------------------------------------------------
# Task 3: Count Confirmed, Waiting and Cancelled bookings

confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:

    if booking[2] == "Confirmed":
        confirmed += 1

    elif booking[2] == "Waiting":
        waiting += 1

    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# --------------------------------------------------
# Task 4: Create a list of passenger IDs having Waiting status

waiting_list = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_list.append(booking[0])

print("\nWaiting List:")
print(waiting_list)

# --------------------------------------------------
# Task 5: Find the destination with the highest bookings

# Counters for each destination
delhi = 0
mumbai = 0
chennai = 0

# Count bookings destination-wise
for booking in bookings:

    if booking[1] == "Delhi":
        delhi += 1

    elif booking[1] == "Mumbai":
        mumbai += 1

    elif booking[1] == "Chennai":
        chennai += 1

# Assume Delhi has highest bookings initially
highest = delhi
destination = "Delhi"

# Compare with Mumbai count
if mumbai > highest:
    highest = mumbai
    destination = "Mumbai"

# Compare with Chennai count
if chennai > highest:
    highest = chennai
    destination = "Chennai"

print("\nMost Booked Destination:")
print(destination)