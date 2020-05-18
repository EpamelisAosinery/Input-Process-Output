############################
# Author:   Epamelis Aosinery
# Date:     3/30/2020
# Desr:     Homework 4.1
############################

while True:
    try:
        num = int(input("Pleas enter number of times to loops: "))
    except ValueError:
        print("Please only enter integer number. Please re-enter. ")
        continue
    else:
        break

for num in range (1,num):
    if num % 3 == 0:
        print(num , "is divisible by 3")
    else:
        pass





