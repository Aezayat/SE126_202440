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

        #adding data to lists -> .append()
        #device.append(rec[0])
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

        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_disks.append(int(rec[5]))

        if int(rec[5]) == 1:
            second_disk.append("---")
            os.append(rec[6])
            yr.append(rec[7])
        elif int(rec[5]) == 2:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
        else:
            second_disk.append("-ERROR-")
            os.append(" @ ")
            yr.append(f"rec# {records}-")
        

#process the liss(s) to view their storage 
for index in range(0, records):
    #'s for every index starting at 0 and up to the number of records"
    print(f"{device[index]:10}\t{brand[index]:10}\t...") #this line prints for every index found within the device list
    #found within the device list

#len() --> length functions; returns integer, num of items in list it is passed
desktops = 0
for i in range (0, len(device)):
    
    if device [1] =="Desktop":
        desktops += 1
    
print(f"There are {desktops} desktops in this file.")


laptops = 0
for value in device:
    if value =="Laptop":
        laptops += 1
print(f"There are {laptops} laptops in this file.")