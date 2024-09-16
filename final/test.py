import csv

# Initialize empty lists for each part category
motherboard = []
cpu = []
cpu_fan = []
ram = []
gpu = []

# Load the CSV file
with open('final/parts.csv') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        motherboard.append(rec[0])
        cpu.append(rec[1])
        cpu_fan.append(rec[2])
        ram.append(rec[3])
        gpu.append(rec[4])

# Function to display parts alphabetically
def display_parts_alphabetically():
    categories = {'Motherboard': motherboard, 'CPU': cpu, 'CPU FAN': cpu_fan, 'RAM': ram, 'GPU': gpu}
    for category, parts in categories.items():
        print(f"\n{category}:")
        for part in sorted(parts):
            print(f" - {part}")

# Function to build a computer
def build_computer():
    categories = {'Motherboard': motherboard, 'CPU': cpu, 'CPU FAN': cpu_fan, 'RAM': ram, 'GPU': gpu}
    selected_parts = {}

    for category, parts in categories.items():
        print(f"\nSelect a {category}:")
        for idx, part in enumerate(parts, start=1):
            print(f"{idx}. {part}")
        choice = int(input(f"Enter the number of the {category} you want to select: ")) - 1
        selected_parts[category] = parts[choice]

    print("\nYou have built a computer with the following parts:")
    for category, part in selected_parts.items():
        print(f"{category}: {part}")

# Program logic starts directly here
choice = ""

while choice != '3':
    print("\nMenu:")
    print("1. Build a computer")
    print("2. Show computer parts alphabetically ordered by category")
    print("3. Quit Program")
    
    choice = input("\nEnter your choice: ")

    if choice == '1':
        build_computer()
    elif choice == '2':
        display_parts_alphabetically()
    elif choice == '3':
        print("Exiting program.")
    else:
        print("Invalid choice, please try again.")