#W5D2 - Comparing Searching Methods: Sequential vs Binary

import csv

#create mepty lists
id_student = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("week5/w5_demoFile.txt") as csvfile:
    file =csv.reader(csvfile)

    for rec in file:

       
     id_student.append(rec[0])
     lname.append(rec[1])
     fname.append(rec[2])
     class1.append(rec[3])
     class2.append(rec[4])
     class3.append(rec[5])

print(f"{"ID$":5}\t{"LAST"}\t{"FIRST":15}")
print("-------------------")

for i in range(0, len(id_student)):
    print(f"{id_student[i]:5}\t{lname[i]:15}\t{fname[i]:15}")
print("-------------------")
    
#SEARCHING: always get the search item (quary) FIRST
#SEQUENTIAL SEARCH -- "searching in sequence" (from beginning through the end)

search_name = input("Enter the LAST NAME you are looking for: ")
found = -1
seq_count = 0

#for loop allow review of each value in list (sequence)
for i in range (0,len(lname)):
    seq_count += 1
    #ask if search value matches current value in list (search)
    if search_name.lower() == lname[i].lower():
        #store the found value's LOCATION [index]
        found = i
print(f"\n\tSequential Search Complete. Loop ran {seq_count} iterations.")

if found != -1: 
   print(f"\n\tWe found {search_name} at index position {found}")
   print(f"\tHere is their info.")
   
   print(f"{id_student[found]:5}\t{lname[found]:15}\t{fname[found]:15}")
else:
   print(f"\n\tWe could not find {search_name}")
   print("\tPlease check your spelling and try again.")


#BINARY SEARCH -- take an ORDERED list and divided into 2 sections (high, low) and based on a middle POINT will continually halve the search pool with a UNIQUE value is found(or isn't)

min = 0
max = len(lname) - 1
mid = int((min + max)/2)

bin_count = 0

#here is the algorithim for INCREASING (ascending) 
while (min < max and search_name.lower() != lname[mid].lower()):
   #both of these must be true in order for search to continue: min index is still less than the max index and the query has not been found 
    bin_count += 1
    if search_name.lower() < lname[mid].lower():
        #revalue hte max to be the middle
        max = mid - 1

    else:
       #revalue the min to be the middle
       min = max + 1

    mid = int((min + max) /2)

print(f"\n\tSequential Search Complete. Loop ran {bin_count} iterations.")

if search_name.lower() == lname [mid].lower():
   print(f"\n\tWe found {search_name} at index position {mid}")
   print(f"\tHere is their info.")
   
   print(f"{id_student[mid]:5}\t{lname[mid]:15}\t{fname[mid]:15}")
else:
   print(f"\n\tWe could not find {search_name}")
   print("\tPlease check your spelling and try again.")

