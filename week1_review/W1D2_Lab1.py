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

#test for function

print(f"People: 30, Room Cap: 50, Diff: {difference(30, 50)}")
print(f"People: 33, Room Cap: 25, Diff: {difference(33,25)}") 
print(f"People: 200, Room Cap: 200, Diff: {difference(200,200)}")
#-----MAIN CODE---------------------