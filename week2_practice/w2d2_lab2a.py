import csv

num_rooms = 0

max_room = 0

current_people = 0

total_records = 0

print(f"ROOM\t\t\t MAX\t\t\tMIN\t\t\tOVER")

with open("week2_practice/lab2a.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        total_records += 1
        if record[2] > record[1]:

            print(f"{record[0]}\t\t{record[2]}\t\t{record[1]}")
            
