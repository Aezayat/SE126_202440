#Alex Zayat 9/1/24
#W7D2 Lab #5 Individual
#Program Prompt : n this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file



import csv

# Initialize empty lists to store student data
ids = []
last_names = []
first_names = []
class1 = []
class2 = []
class3 = []

def menu():
    print("\nMenu:")
    print("1. See All Student Report")
    print("2. Search for a Student [ID]")
    print("3. Search for a Student [Last]")
    print("4. View a Class Roster [class1, class2, and class3]")
    print("5. Exit/Quit Program")
    
    choice = input("Enter your choice: ")
    return choice

def classSearch(class_name, ids, last_names, first_names, class1, class2, class3):
    found_class = []
    class_name = class_name.lower()

    for i in range(len(ids)):
        if class_name == class1[i].lower() or class_name == class2[i].lower() or class_name == class3[i].lower():
            found_class.append((ids[i], first_names[i], last_names[i]))

    if found_class:
        print("\nStudents enrolled in", class_name)
        for student in found_class:
            print(f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}")
    else:
        print(f"\nNo students found enrolled in {class_name.capitalize()}.")

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid].lower() < target:
            low = mid + 1
        elif arr[mid].lower() > target:
            high = mid - 1
        else:
            return mid
    return -1

def searchID(id, ids, last_names, first_names, class1, class2, class3):
    index = binary_search(ids, id)
    
    if index != -1:
        print(f"\nStudent found:\nID: {ids[index]}, First Name: {first_names[index]}, Last Name: {last_names[index]}, Class1: {class1[index]}, Class2: {class2[index]}, Class3: {class3[index]}")
    else:
        print(f"\nStudent ID {id} not found.")

def search_LName(last_name, ids, last_names, first_names, class1, class2, class3):
    index = binary_search(last_names, last_name)
    
    if index != -1:
        print(f"\nStudent found:\nID: {ids[index]}, First Name: {first_names[index]}, Last Name: {last_names[index]}, Class1: {class1[index]}, Class2: {class2[index]}, Class3: {class3[index]}")
    else:
        print(f"\nStudent Last Name {last_name} not found.")

# Read file data into lists
with open("week7/lab5_students.txt") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        # Ensure each record has 6 elements to avoid index error
        if len(rec) == 6:
            ids.append(rec[0])
            last_names.append(rec[1])
            first_names.append(rec[2])
            class1.append(rec[3])
            class2.append(rec[4])
            class3.append(rec[5])

# Main loop
answer = "y"
while answer.lower() == "y":
    user_choice = menu()
    
    if user_choice == '1':
        print("\nAll Student Report:")
        for i in range(len(ids)):
            print(f"ID: {ids[i]}, First Name: {first_names[i]}, Last Name: {last_names[i]}, Class1: {class1[i]}, Class2: {class2[i]}, Class3: {class3[i]}")
    
    elif user_choice == '2':
        id = input("\nEnter Student ID to search: ")
        searchID(id, ids, last_names, first_names, class1, class2, class3)
    
    elif user_choice == '3':
        last_name = input("\nEnter Student Last Name to search: ")
        search_LName(last_name, ids, last_names, first_names, class1, class2, class3)
    
    elif user_choice == '4':
        class_name = input("\nEnter class name (class1, class2, class3) to view roster: ")
        classSearch(class_name, ids, last_names, first_names, class1, class2, class3)
    
    elif user_choice == '5':
        print("\nGoodbye!")
        
    
    else:
        print("\nInvalid choice, please try again.")
    
    # Ask the user if they want to continue
    answer = input("\nWould you like to perform another action? (y/n): ")