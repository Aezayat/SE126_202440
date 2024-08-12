#Alex Zayat 8/12/24 
#w4d2 lab #4
#Program Prompt: print list as appears, re-print lists add the House Motto, print the total number of people in the list, print the average age - rounded to a whole number {:.0f}, print tallies/final counts for each allegiance (Field4)

#variable dictionary:
#people
#allegiance
#records
#first_name
#last_name
#age
#nickname
#allegiance
#house_mottos
#average_age
#--------Code---------------------------------------------------------------------------------------------------------------------------
import csv

#Create Empty Lists
people = 0
allegiance = 0
records = 0
first_name = []
last_name = []
age = []
nickname = []
allegiance = []
house_mottos = [
    "Winter is Coming", 
    "Ours is the Fury", 
    "Family. Duty. Honor", 
    "And now my watch begins", 
    "Hear me roar!", 
    "Fire & Blood"
    ]

#-------------------------------------------
# Open and read the CSV file
with open("week4\lab#4\lab4A_GOT_NEW.txt") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        records += 1
        first_name.append(rec[0])
        last_name.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        allegiance.append(rec[4])

# Print all the names and allegiances
for i in range(0, records):
    print(f"{first_name[i]}, {last_name[i]}, {age[i]}, {nickname[i]}, {allegiance[i]}")

print("--------------------------------------------------")

# Loop to print each record with its house motto
for i in range(0, records):
    if allegiance[i] == "House Stark":
        motto = house_mottos[0]
    elif allegiance[i] == "House Baratheon":
        motto = house_mottos[1]
    elif allegiance[i] == "House Tully":
        motto = house_mottos[2]
    elif allegiance[i] == "Night's Watch":
        motto = house_mottos[3]
    elif allegiance[i] == "House Lannister":
        motto = house_mottos[4]
    elif allegiance[i] == "House Targaryen":
        motto = house_mottos[5]
    else:
        motto = "n/a"  

    print(f"{first_name[i]}, {last_name[i]}, {age[i]}, {nickname[i]}, {allegiance[i]}, {motto}")
print("----------------------------------------------------")
print(f"Total number of people: {records}")

# Calculate and print the average age, rounded to the nearest whole number
average_age = sum(age) / records
print(f"Average age: {average_age:.0f}")


# Calculate and print tallies for each allegiance
allegiance_counts = {}
for count in allegiance:
    if count in allegiance_counts:
        allegiance_counts[count] += 1
    else:
        allegiance_counts[count] = 1

print("--------------------------------------------------")
print("Allegiance Counts:")
for key, value in allegiance_counts.items():
    print(f"{key}: {value}")