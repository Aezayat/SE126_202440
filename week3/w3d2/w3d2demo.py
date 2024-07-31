#W3D2- Data from a Text File to 1D Parallel Lists

import csv

records = 0

#create some empty lists to store file data to
names = []
ages = []
colors = []
animals = [] 

#connected to file-------------------
with open("week3/w3d2/classList_202140.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: #file is a 2d list! more on this in W4 :D
        #rec is a LIST of data which represents on entire record within the file
        #inside of this block everything happens for EACH record in the file!

        records += 1

        #print(rec[3][0])


        #add file data from the record to respective lists -->  .append()
        names.append(rec[0]) #adds to the end 
        ages.append(int(rec[1]))
        colors.append(rec[2])
        animals.append(rec[3])

       
#disconnected from file-----------

for i in range(0, records):
    #parallel lists are connected via same INDEX
    #i --> index

    #if my name is found in a certain record
    print(f"{names[i]}'s favorite anime is the {animals[i]}.")

for i in range(0, len(names)):
    print(f"{names[i]}'s favorite anime is the {colors[1].upper()}.")

#Don't do for 1D list-------------------- ? (what's under)
i = 0
for value in ages:
    
    print(f"{names[value]}'s favorite anime is the {animals[value]}.")
    i += 1

    