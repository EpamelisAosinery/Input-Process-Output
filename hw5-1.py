############################
# Author:   Epamelis Aosinery
# Date:     4/21/2020
# Desr:     Homework 5.1
############################

def getNum():
    while True:
        try:
            num = float(input("Enter a number to add: "))
        except ValueError:
            print("Invalid. This is not a number. Please re-enter.")

        else:
            print(num, "has been added to the total.")
            break
    return num

sum = 0
choice = "Y"
valid = ("YES", "Y", "N", "NO")
yeslist = ("YES", "Y")
while choice in yeslist:
    num = getNum()
    sum = sum + num
    choice = input("Would you like to add another numbers [Y or N]? ").upper()
    while choice not in valid:
        choice = input("Would you like to add another numbers [Y or N]? ").upper()

print("The sum of the numbers is", sum)









