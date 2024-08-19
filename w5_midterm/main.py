import csv
record = 0
records = 0
answer = 0
response = 0
#--create lists---------------------------------
modelYear = []
manufacturer = []
model = []
transmission = []
price = []
Mcars = []
#----------disconnect----------------------------


with open("w5_midterm/vehicles.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        # Append each field to the corresponding list
        modelYear.append(rec[0])
        manufacturer.append(rec[1])
        model.append(rec[2])
        transmission.append(rec[3])
        price.append(rec[4])
            
        # Increment the records counter
        record += 1



answer = "y"  # Assuming you want the loop to start by checking for user input

while answer == "y":
    # Ask the user for transmission type
    answer = input("Are you looking for an Automatic or Manual? ").lower()
    
    # Ask the user for vehicle type
    response = input("Are you looking for a Sedan or SUV? ").lower()
    
    # Check conditions for Automatic and Sedan
    if answer == "automatic" and response == "sedan":
        if answer.lower() == "automatic" and response.lower() == "sedan":
            for index in range(0, 2):
   
                print(f"{modelYear[index]:5}\t{manufacturer[index]:5}\t{model[index]:5}\t${price[index]:5}") #this line prints for every index found within the device list
 
            
    
    # Ask if the user wants to continue searching
   #print(f"{modelYear[i]:<10}\t{manufacturer[i]:<10}\t{model[i]}\t{transmission[i]}\t${price}")
    answer = input("Do you want to search again? (y/n): ").lower()

