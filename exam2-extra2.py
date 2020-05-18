############################
# Author:   Epamelis Aosinery
# Date:     3/24/2020
# Desr:     Exam 2.2
############################

#Crust = 0 to 35 kilometers
#Upper Mantle = 36 to 660 kilometers
#Lower Mantle =  661 to 2890 kilometers
#Core = 2891 to 6360 kilometers

def getNum():
    if num <= 35:
        print("You are in the Earth's crust.")
    elif num <= 660:
        print("You are in the Earth's upper mantle.")
    elif num <= 2890:
        print("You are in the Earth's upper mantle.")
    else:
        print("You are in the Earth's core.")


while True:
     try:
         num = float(input("Please enter depth in Earth: "))
         while num <0 or num >6360:
             num = float(input("The depth in Earth can not be negative and larger than 6360.\n"
                             "Please enter depth in Earth again: "))
     except ValueError:
         print("Please only enter numbers.")
         continue
     else:
         break
getNum()
