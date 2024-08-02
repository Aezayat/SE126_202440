#Alex Zayat 7/29/24

#W3D2 Lab 3A
#Program Prompt: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops. Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#records
#laptop_replaced
#computer_replaced
#computer
#brand
#processor
#storage
#first_disk
#second_disk
#number_disk
#os
#year

#---- MAIN CODE------------------------------------

import csv

records = 0
laptop_replaced = 0
computer_replaced = 0

#Creating empty Lists-----

computer = []
brand = []
processor = []
storage = []
first_disk = []
second_disk = []
number_disk =[]
os = []
year = []


with open("week3/w3d2/lab3a/lab3a.csv") as csvfile: #transfering our data into our empty lists
    file = csv.reader(csvfile)  

    for rec in file:

        records += 1 #keeping count of how many records each time records is ran

        computer.append(rec[0])
        brand.append(rec[1])
        processor.append(rec[2])
        storage.append(rec[3])
        first_disk.append(rec[4])
        second_disk.append(rec[5])
        number_disk.append(rec[6])
        os.append(rec[7])
        year.append(rec[-1])


    for index in range (0, records): #Displaying our data from the list provided
        print(f"{computer[index]:10}\t{brand[index]:10}\t{processor[index]:10}\t{storage[index]:10}\t{first_disk[index]:10}\t{second_disk[index]:10}\t{number_disk[index]:10}\t{os[index]:10}\t{year[index]:10}")


    for i in range(len(year)): #Finding ammount of laptops that need to be replaced
        if computer[i] == "L" and int(year[i]) >= 16:
        
            laptop_replaced += 1
 
    for i in range(len(year)): #Finding the amount of computers that need to be replaced
        if computer[i] == "L" and int(year[i]) <= 16:

            computer_replaced += 1

            
#Printing our information to our display ----
print(f"\nTo replace {laptop_replaced} it will cost you $ 16000")
print(f"To replace {computer_replaced} it will cost you $ 3000") 
print(f"\nPress any key to continue . . .")