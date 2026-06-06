"""Smart Parking System.....

Parking slots are represented as:
slots = [1, 0, 1, 1, 0, 0, 1, 0]
Where:
• 1 = Occupied 
• 0 = Available 
Write a program to:
• Count occupied and available slots. 
• Find the first available slot. 
• Display all available slot numbers. 
• Check whether parking occupancy exceeds 75%."""
slots = [1, 0, 1, 1, 0, 0, 1, 0]
# Task 1: Count occupied and available slots
occupied = 0
available = 0
for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied slots:", occupied)
print("Available slots:", available)
# Task 2: Find the first available slot (1-based index)
slot_no = 1
for slot in slots:      
    if slot == 0:
        print("First available slot:", slot_no)
        break
    slot_no += 1
# Task 3: Display all available slot numbers (1-based)
available_slots = []
slot_no = 1
for slot in slots:
    if slot == 0:
        available_slots.append(slot_no)
    slot_no += 1

print("Available slot numbers:", available_slots)

# Task 4: Check whether parking occupancy exceeds 75%
occupancy_rate = (occupied / len(slots)) * 100
if occupancy_rate > 75:
    print("Parking occupancy exceeds 75%.")
else:
    print("Parking occupancy does not exceed 75%.")