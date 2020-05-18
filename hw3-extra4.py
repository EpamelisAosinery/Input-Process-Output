############################
# Author:   Epamelis Aosinery
# Date:     3/27/2020
# Desr:     Homework 3.ec4
############################

while True:
    try:
        year = int(input("Enter a year to check if a leap year: "))
    except ValueError:
        print("Please only enter inter numbers. ")
        continue
    else:
        break
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))



