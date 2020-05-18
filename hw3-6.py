############################
# Author:   Epamelis Aosinery
# Date:     2/27/2020
# Desr:     Homework 3.6
############################

def calTuition(residency, credit1, credit2):
    if residency == "1":
        tuition = (credit1 * 101.5) + (credit2 * 200) + 50 + 60 + (23*(credit1 + credit2))
        return tuition
    elif residency == "2":
        tuition = (credit1 * 117) + (credit2 * 265) + 50 + 60 + (23 * (credit1 + credit2))
        return tuition
    else:
        tuition = (credit1 * 257) + (credit2 * 350) + 50 + 60 + (23 * (credit1 + credit2))
        return tuition


def getCredits():
    while True:
        try:
            credits = float(input("Please enter number of 100-200 or 300-400 level credit hours (0-90): "))
            if credits in range (0,91):
                return credits
            else:
                print("Invalid number. Enter value 0 to 90.")
        except ValueError:
                print("Error 1.  Please choose 1-3: ")


#MAIN
print("1- In-District.")
print("2- Out-of-District.")
print("3- Out-of-State/International.\n")

residency = input("Please chose 1-3: ")
while residency not in ("1", "2", "3"):
    residency = input("Please chose 1-3: ")
credit1 = getCredits()
credit2 = getCredits()

#while True:
#     try:
#         credit1 = float(input("How many credits of 100 to 200 level credits you plan to take? "))
#         credit2 = float(input("How many credits of 300 to 400 level credits you plan to take? "))
#     except ValueError:
#         print("Please only enter numbers.")
#         continue
#     else:
#         break

while credit1 < 0 or credit2 < 0:
    print("Error2. Total credit hours can not be negative. Please re-run program.")
    credit1 = float(input("How many credits of 100 to 200 level credits you plan to take? "))
    credit2 = float(input("How many credits of 300 to 400 level credits you plan to take? "))

while credit1 == 0 and credit2 == 0:
    print("Error2. Total credit hours (lower plus upper) must be greater than 0. Please re-run program.")
    credit1 = float(input("How many credits of 100 to 200 level credits you plan to take? "))
    credit2 = float(input("How many credits of 300 to 400 level credits you plan to take? "))

while credit1 >= 90 or credit2 >= 90:
    print("Invalid")
    credit1 = float(input("How many credits of 100 to 200 level credits you plan to take? "))
    credit2 = float(input("How many credits of 300 to 400 level credits you plan to take? "))

tuition = calTuition(residency, credit1, credit2)
print("Your tuition is: $%.2f" % tuition)
