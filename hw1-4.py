############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 1-4
############################

eggs = int(input("How many eggs does the restaurant use last month? "))
carton = float(eggs/12)

print("Order" , carton, "cartons of eggs next month.")

import math
carton = math.ceil(eggs/12)

print("Order" , carton, "cartons of eggs next month.")
print("Order" , -(-eggs//12), "cartons of eggs next month.")
