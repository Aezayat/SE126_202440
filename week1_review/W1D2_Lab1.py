#W1D2 SE126 Lab #1 

#Alex Zayat 
#Lab #1
#July 17th [W1D2] 

#PROGRAM PROMPT : Build a function that is passed both the number of people attending the meeting, as well as the maximum room capacity. This function should determine the number of people over/under the capacity based on these two values, and return the difference value.

#Variable Dictionary 


#------FUNCTIONS-------------------
def difference(people, max_cap):
    diff = max_cap - people

    return diff

def decision(response):
    while response not in ("y", "n"):
        response = input("Invalid Entry. Please enter y or n :")
    return response
#test for function

print(f"People: 30, Room Cap: 50, Diff: {difference(30, 50)}")
print(f"People: 33, Room Cap: 25, Diff: {difference(33,25)}") 
print(f"People: 200, Room Cap: 200, Diff: {difference(200,200)}")
#-----MAIN CODE---------------------

continue_checking = "y"


while continue_checking:


    meeting_name = input("Please enter a meeting name: ")

    max_cap = int(input("Please enter the maximum room capacity: "))

    people = int(input("Please enter the number of people attending the meeting: "))

    diff = difference(people, max_cap)

    if diff >= 0:
        print(f"The meeting {meeting_name} is legal to hold.")
        print(f"{diff} people can be added to the meeting and still meet fire regulations.")


    else:
        print(f"The meeting {meeting_name} is illegal to hold")
        print(f"{diff} people must be removed from the meeting to meet fire regulations. ")

    response = input("Do you have another meeting to add (y / n) ")
    continue_checking = (decision(response) == 'y')