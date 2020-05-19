############################
# Author:   Epamelis Aosinery
# Date:     3/3/2020
# Desr:     Homework 3.extra1
############################

while True:
     try:
        number1 = float(input("Please enter the first number: "))
        number2 = float(input("Please enter the second number: "))
     except ValueError:
         print("Please only enter numbers.")
         continue
     else:
         break
if number1 < number2:
    print("The second number is larger than the first number.")
elif number1 > number2:
    print("The first number is larger than the second number.")

else:
    print("The first number and the second number are equal.")