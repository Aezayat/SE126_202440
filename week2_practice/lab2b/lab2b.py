#Alex Zayat

#w2d2 lab 2b

#Program Prompt : You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file.Organization of the csv file:

#Variable Dictionary:
#device
#brand
#cpu
#ram
#first_disk
#second_disk
#num_disks
#os
#yr

import csv

records = 0

#create some empty lists - one list for every possible field in the file 
device = []
brand = []
cpu = []
ram = []
first_disk = []
second_disk = []
num_disks = []
os = []
yr = []

with open("week3/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #update the records value
        records += 1


        if rec[0] == "D":
            device.append("Desktop")
        elif rec[0] == "L":
            device.append("Laptop")
        else:
            device.append("-ERROR-")

        if rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        elif rec[1] == ("DL"):
            brand.append("Del")
        else:
            brand.append("-ERROR-")

for index in range(0, records):
    #'s for every index starting at 0 and up to the number of records"
    print(f"{device[index]:10}\t{brand[index]:10}\t...")