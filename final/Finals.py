#Alex Zayat 9/16/24
#Final 
#Variable Dictionary
#compatible_parts
#categories
#motherboard_choice
#selected_platform
#cpu
#cpuFan
#ram
#gpu


import csv

# Create Empty Lists
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

# Compatibility lists
compatible_parts = {
    'AMD AM5 DDR5': {
        'motherboards': ['Gigabyte Aorus Elite AX B650', 'MSI PRO X670-P WiFi ProSeries'],
        'cpus': ['AMD Ryzen 7 7800X3D', 'AMD Ryzen 9 7900'],
        'cpu_fans': ['Noctua NH-D15', 'Deepcool AK620'],
        'ram': ['G.Skill Flare X5 Series 6000MHz 32GB'],
        'gpus': ['NVIDIA GeForce RTX 4090', 'EVGA GeForce RTX 3080']
    },
    'Intel LGA1700 DDR5': {
        'motherboards': ['ASUS ROG Maximus Z790 Hero', 'MSI MEG Z790 ACE'],
        'cpus': ['Intel Core i9-14900K', 'Intel Core i7-14700K'],
        'cpu_fans': ['Corsair H150i ELITE LCD XT', 'Noctua NH-D15'],
        'ram': ['Corsair VENGEANCE DDR5 32GB'],
        'gpus': ['NVIDIA GeForce RTX 4090', 'RTX 4070 Super']
    }
}

# Function to display parts alphabetically
def display_parts_alphabetically():
    categories = {'Motherboard': motherboard, 'CPU': cpu, 'CPU FAN': cpu_fan, 'RAM': ram, 'GPU': gpu}
    for category, parts in categories.items():
        print(f"\n{category}:")
        for part in sorted(parts):
            print(f" - {part}")

# Function to build a computer 
def build_computer():

    # Step 1: Select Motherboard
    print("\nChoose your motherboard platform from the available options.")
    motherboard_options = {
        '1': 'AMD AM5 DDR5',
        '2': 'Intel LGA1700 DDR5'
    }
    
    for key, value in motherboard_options.items():
        print(f"{key}. {value}")
    
    motherboard_choice = input("\nEnter the number corresponding to your choice of motherboard platform: ")

    selected_platform = motherboard_options[motherboard_choice]
    
    # Step 2: Select Motherboard
    motherboard = select_part(compatible_parts[selected_platform]['motherboards'], 'Motherboard')
    
    # Step 3: Select CPU
    cpu = select_part(compatible_parts[selected_platform]['cpus'], 'CPU')

    # Step 4: Select CPU Fan
    cpu_fan = select_part(compatible_parts[selected_platform]['cpu_fans'], 'CPU Fan')

    # Step 5: Select RAM
    ram = select_part(compatible_parts[selected_platform]['ram'], 'RAM')

    # Step 6: Select GPU
    gpu = select_part(compatible_parts[selected_platform]['gpus'], 'GPU')

    # Display the built computer
    print("\nYou have built a computer with the following components:")
    print(f"Motherboard: {motherboard}")
    print(f"CPU: {cpu}")
    print(f"CPU Fan: {cpu_fan}")
    print(f"RAM: {ram}")
    print(f"GPU: {gpu}")

# Helper function to select part from a list
def select_part(options, part_type):
    print(f"\nSelect a {part_type}:")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    choice = int(input(f"Enter the number of the {part_type} you want to select: ")) - 1
    return options[choice]

#----MAIN CODE ----------------------------------------------------
choice = ""

while choice != '3': #Menu shown to user
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