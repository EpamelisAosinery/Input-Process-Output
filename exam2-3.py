############################
# Author:   Epamelis Aosinery
# Date:     3/24/2020
# Desr:     Exam 2.3
############################

while True:
     try:
        num = int(input("Please enter an integer number value: "))
     except ValueError:
         print("Please only enter integer value.")
         continue
     else:
         break

if (num % 2) == 0 and num > 0:
   print("This number is even and positive.")
elif (num % 2) == 0 and num < 0:
   print("This number is even and negative.")
elif (num % 2) != 0 and num > 0:
   print("This number is odd and positive.")
elif (num % 2) != 0 and num < 0:
   print("This number is odd and negative.")
else:
   print("0 is an even number")