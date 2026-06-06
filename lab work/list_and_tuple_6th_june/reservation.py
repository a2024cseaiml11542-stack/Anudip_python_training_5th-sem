"""..... Train Reservation Waiting List....

Passenger records:
passengers = [
 ("Anuj", "Confirmed"),
 ("Rahul", "Waiting"),
 ("Priya", "Confirmed"),
 ("Amit", "Waiting"),
 ("Neha", "Confirmed")
]
Write a program to:
• Display all waiting-list passengers. 
• Count confirmed and waiting passengers. 
• Find whether a specific passenger has a confirmed ticket. 
• Create separate lists for confirmed and waiting passengers."""
# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Counters for confirmed and waiting passengers
confirmed_count = 0
waiting_count = 0

# Separate lists for confirmed and waiting passengers
confirmed_list = []
waiting_list = []

# Display all waiting-list passengers
print("Waiting List Passengers:")

for name, status in passengers:

    # Check if passenger is in waiting list
    if status == "Waiting":
        print(name)
        waiting_count += 1
        waiting_list.append(name)

    # Otherwise passenger is confirmed
    else:
        confirmed_count += 1
        confirmed_list.append(name)

# Display counts
print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

# Search passenger name
search_name = input("\nEnter passenger name: ")

found = False

# Check whether passenger has a confirmed ticket
for name, status in passengers:

    # Compare names and check status
    if name.lower() == search_name.lower() and status == "Confirmed":
        found = True
        break

# Display result
if found:
    print("Confirmed Ticket Found")
else:
    print("Confirmed Ticket Not Found")

# Display separate lists
print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)