#Alex Zayat    8/5/24
#W4D1 - 1D parallel list review + making new lists and starts to seq. search

#Variable Dictionary
#gradeTotal
#classAvg
#avg

import csv
#create empty lists - one for EACH potentional field
firstNames = []
lastNames = []
test1 = []
test2 = []
test3 = []

#we will also create data and append to these bellow
numAvg = []
letAvg = []

#connected to file--------------------------------------------
with open ("week4/listPractice1.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #'s file' is an example of a 2D list
        firstNames.append(rec[0])
        lastNames.append(rec[1])
        #will be mathematically processing test data -- > cast int()
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#Disconnected to file-----------------------------------------


print(f"{"FIRST":10}\t{"LAST":10}\t{"T#1":3}\t{"T#2":3}\t{"T#3":3}\t{"T#1":3}\t{"T#2":3}\t{"T#3":3}")
#process list ..> FOR LOOP!
for i in range(0,len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{test1[i]:3}\t{test2[i]:3}\t{test3[i]:3}")
print("--------------------------------------------------------")

#process lists to find numeric and letter grade equivalent for each student
for i in range(0, len(firstNames)):
    avg = (test1[i] + test2[i] + test3[i]) / 3

    if avg >= 90:
        letter = "A"

    elif avg >= 80:
        letter = "B"

    elif avg >= 70:
        letter = "C"

    elif avg >= 60:
        letter = "D"
    #finish the grade equivalents for HW
    else: 
        letter = "F"

    #adding num and let avg to respective lists; these remain PARALLEL with starting data
    numAvg.append(avg)
    letAvg.append(letter)

print(f"{"FIRST":10}\t{"LAST":10}\t{"T#1":3}\t{"T#2":3}\t{"T#3":3}\t{"T#1":3}\t{"T#2":3}\t{"T#3":3}\t{"AVG.":5}\t{"LETTER":3}")
#process list ..> FOR LOOP!
for i in range(0,len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{test1[i]:3}\t{test2[i]:3}\t{test3[i]:3}\t{numAvg[i]:5.1f}\t{letAvg[i]:3}")
print("--------------------------------------------------------")
#process lists to find the numAVg
gradeTotal = 0

for i in range(0, len(numAvg)):
    #add each student's numAvg to gradeTotal variable
    gradeTotal += numAvg[i]

classAvg = gradeTotal / len(numAvg)

print(f"\nThere are {len(numAvg)} students in the class\nThe class Average is:{classAvg:.1f}\n\n")