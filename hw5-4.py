############################
# Author:   Epamelis Aosinery
# Date:     4/22/2020
# Desr:     Homework 5.4
############################

employeenames = ["Jim Bailey", "Amy Dillon", "Ali Nassar", "Jose Martinez", "Lenard Phillips"]
name = input("Enter employee name: ")
if name in employeenames:
    print("Valid employee name.")
else:
    print("Invalid employee name.")