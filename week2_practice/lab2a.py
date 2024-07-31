#Alex Zayat 7/28/24
#Lab 2A
#Program Prompt: Write aprogram that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit

#Variable Dictionary
#processed_records
#over_limit_count
#rooms

#------MAIN CODE------------------------------------------------------------------

import csv


rooms = [
    {"name": "Captain's Quarters", "max": 300, "current": 350},
    {"name": "Federation", "max": 375, "current": 425},
    {"name": "Voyager", "max": 100, "current": 102},
]


processed_records = len(rooms)
over_limit_count = 0

# Print header
print("Room                  Max    Min    Over")


# Process each room
for room in rooms:
    over = room["current"] - room["max"]
    if over > 0:
        over_limit_count += 1
    print(f"{room['name']:20} {room['max']:5} {room['current']:5} {over:5}")

# Print footer
print(f"\nProcessed  {processed_records}  records")
print(f"There are {over_limit_count} rooms over the limit.\n")