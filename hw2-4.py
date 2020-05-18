############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 2.4
############################

def getSide():
    side = float(input("Please enter the length of rectangle:\t "))
    return side


def calarearectangle(side1, side2):
    area = side1 * side2
    print("The area of the rectangle is:\t\t\t", area)


#Main
side1 = getSide()
side2 = getSide()

again = input("Would you like to enter another side (y/n): ").upper()
while again not in ("N", "NO", "YES", "Y"):
    again = input("Invalid.  Please enter Y or N: ").upper()
calarearectangle(side1, side2)

