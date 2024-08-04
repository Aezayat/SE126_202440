#Alex Zayat       8/2/24
#W3D2             Lab #3 Homework Assingment
#Program Prompt: Find :
# Number of individuals not eligible to register.
# Number of individuals who are old enough to vote but have not registered.
# Number of individuals who are eligible to vote but did not vote.
# Number of individuals who did vote.
# Number of records processed.



#Variable Dictionary
#records
#age
#not_eligible_count
#voter_eligible_count
#eligible_to_vote_but_did_not
#vote_count

#----MAIN CODE--------------------------------------------

import csv

records = 0
age = 0
not_eligible_count = 0
voter_eligible_count = 0
not_registered_count = 0
eligible_to_vote_but_did_not = 0
vote_count = 0

#--empty lists---------------
voter_id = []
voter_age = []
not_eligible = []
not_registered = []
voter_eligible = []
voters = []
registered_votedN = []

with open("week3/w3d2/lab3-homework/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        records += 1  # Keeps track of each record processed

        
        voter_id.append(rec[0])
        voter_age.append(rec[1])
        age = int(rec[1])
        not_registered.append(rec[2])


        if age < 18:  #Checks eligibility to vote by age 
            not_eligible_count += 1  # Counts not eligible voters
        else:
            voter_eligible.append(rec[0])  # Stores eligible voter ID


        if rec[2] == "N": #Checks how many people are not registered to vote
            not_registered.append("Not registered")
            not_registered_count += 1 #counts voters not registered
        

        if rec[2] =="Y" and rec[3] == "N": # Checks to see if voter is eligible to vote, and if they did vote. Then keeps track of result
            registered_votedN.append("Registered to vote but did not")
            eligible_to_vote_but_did_not += 1 


        if rec[2] == "Y" and rec[3] == "Y": #Checks how many voters are registered and did vote. Then keeps track of result
            voters.append("Total number of voters")
            vote_count += 1 #Counts total number of voters


             

        

        

print(f"Number of not eligible voters: {not_eligible_count}")
print(f"Number of voters eligble that did not vote: {not_registered_count}")
print(f"Number of voters eligible, but did not vote: {eligible_to_vote_but_did_not}")
print(f"Number of total voters: {vote_count}")
print(f"Total number of records processed: {records}")