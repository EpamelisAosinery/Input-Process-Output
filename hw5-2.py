############################
# Author:   Epamelis Aosinery
# Date:     4/21/2020
# Desr:     Homework 5.2
############################


nums = []
def getNum():
    while True:
        try:
            num = (float(input("Enter a number to add: ")))
        except ValueError:
            print("Invalid. This is not a number. Please re-enter.")
            continue
        else:
            print(num, "has been added to the total.")
            return num


choice = "Y"
valid = ("YES", "Y", "N", "NO")
yeslist = ("YES", "Y")
while choice in yeslist:
    num = getNum()
    nums += [num]

    choice = input("\nWould you like to add another numbers [Y or N]? ").upper()
    while choice not in valid:
        print("Invalid respond. Please enter Y or N")
        choice = input("\nWould you like to add another numbers [Y or N]? ").upper()


print("Total numbers entered:\t\t\t\t\t", len(nums))
print("The smallest numbers entered:\t\t\t", min(nums))
print("The largest numbers entered:\t\t\t", max(nums))
average = sum(nums) / len(nums)
print("The average of the numbers is:\t\t\t", average)
print("The sum of the numbers is:\t\t\t\t", sum(nums) )









