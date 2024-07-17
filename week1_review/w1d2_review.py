#W1D2 SE116 Review Demo - split into parts in Canvas

#Alex Zayat 
#Practice 1
#July 17th [W1D2] 

#PROGRAM PROMPT : This is tempF to tempC conversion program that averages all temps entered 

#Variable Dictionary 


#-----FUNCTIONS-------------------------------------------
def converter(f): 

    '''this function is passed a temp F value, converts to C, and returns said value'''
    c = (f - 32) * (5 / 9 )

    return c #literally returns to the point of function call 

#-----MAIN CODE--------------------------------------------

#initializing known or needed values
tempCount = 0
tempSum = 0 

degree = u'\N{degree sign}' 


answer = "y" 

while answer == "y" or answer == "yes":

    tempF = float(input("\t\tEnter temperature in Fahrenheit: "))

    tempCount += 1       #tempCount = tempCount + 1
    tempSum += tempF     #tempSum = tempSum = tempF

    #convert F to C --> use a function which returns a value
    #tempC = (tempF - 32) * (5 / 9)
    tempC = converter(tempF)  

    print(f"\tTemperature: {tempF:.1f}{degree} | {tempC:.1f}") 


    #build a way out!
    answer = input("\t\tWould you like to enter another temp? [y/n]: ").lower() 

    #error trap
    while answer.lower() != "y" and answer != "n" and answer != "yes" and answer != "no": 
        print("\t\t***INVALID ENTRY***") 
        answer = input("\t\tWould you like to enter another temp? [y/n]: ")



if tempCount != 0: 
    avgTemp = tempSum / tempCount
    avgC = converter(avgTemp) 

    print(f"\n\nYou have entered {tempCount} temperatures for an average of {avgTemp:.1f} {degree}F  |  {avgC:.1f}{degree}C")

    print("\n\n\tThank You & Goodbye.\n\n") 

else:
    print("\n\n\tOkay, goodbye!\n\n") 
