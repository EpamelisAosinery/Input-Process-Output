############################
# Author:   Epamelis Aosinery
# Date:     2/18/2020
# Desr:     Homework 3.2
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

print("1- In-District.")
print("2- Out-of-District.")
print("3- Out-of-State/International.\n")
residency = input("Please chose 1-3: ")
while residency not in ("1", "2", "3"):
    residency = input("Invalid.  Please choose 1-3: ")
    if residency in ("1", "2", "3"):
        break

credit1 = int(input("How many credits of 100 to 200 level credits you plan to take? "))
credit2 = int(input("How many credits of 300 to 400 level credits you plan to take? "))
tuition = calTuition(residency, credit1, credit2)
print("Your tuition is: $%.2f" % tuition)