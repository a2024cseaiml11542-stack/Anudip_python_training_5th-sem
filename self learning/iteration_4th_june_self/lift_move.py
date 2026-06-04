# Initialize current lift floor and total floors travelled
current_floor = 0
total_travel = 0

while True:

    # Read destination floor; -1 stops the input loop
    destination = int(input("Enter Destination (-1 to stop): "))

    if destination == -1:
        break

    # Distance travelled for this move is absolute difference in floors
    travelled = abs(destination - current_floor)

    # Show the floors moved for this single trip
    print("Travelled:", travelled, "floors")

    # Accumulate total travel and update current floor
    total_travel += travelled

    current_floor = destination

# Print total floors the lift moved during the session
print("Total Travelled:", total_travel, "floors")