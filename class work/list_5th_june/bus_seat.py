"""Simple bus seat utilities.

This module demonstrates basic operations on a small list of seats:
- count booked and available seats
- find the first available seat
- list all available seat numbers (1-based)
- compute occupancy percentage and show a status message

Seat representation: 1 == booked, 0 == available
"""

# Current seat statuses in the bus (1=booked, 0=available)
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Counters and storage for derived information
booked = 0
available = 0
available_seats = []

# Count booked and available seats
for seat in seats:
    # seat == 1 means this seat is booked
    if seat == 1:
        booked += 1
    else:
        # any other value (here 0) is treated as available
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)

# Find the first available seat (1-based index)
seat_no = 1
for seat in seats:
    if seat == 0:
        # Found the first available seat; report and stop searching
        print("First Available Seat:", seat_no)
        break
    seat_no += 1

# Collect all available seat numbers (1-based)
seat_no = 1
for seat in seats:
    if seat == 0:
        # Append this seat number to the list of available seats
        available_seats.append(seat_no)
    seat_no += 1

print("Available Seat Numbers:", available_seats)

# Calculate and display occupancy percentage
occupancy = (booked / len(seats)) * 100
print("Bus Occupancy:", occupancy, "%")

if occupancy > 70:
    # Status threshold can be adjusted as needed
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")