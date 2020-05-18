############################
# Author:   Epamelis Aosinery
# Date:     4/19/2020
# Desr:     exam 3.2
############################

while True:
    try:
        num = float(input("Enter meters to covert to inches (enter zero or negative number to stop): "))
        while num > 0:
            result = num * 39.3701
            print(num , " meters is equal to %.2f"% result , "inches")
            num = float(input("Enter meters to covert to inches (enter zero or negative number to stop): "))
        else:
            print("\nGoodbye.")
            break
    except ValueError:
        print("Invalid. Please only enter number only.")
        continue
    else:
        break





