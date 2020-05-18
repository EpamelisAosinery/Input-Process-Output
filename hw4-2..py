############################
# Author:   Epamelis Aosinery
# Date:     3/30/2020
# Desr:     Homework 4.2
############################

def getNum():
    while True:
        try:
            mph = float(input("Enter MPH: "))
            print(mph, "MPH = %.0f" % (mph * 1.60934), "KPH")
            again = input("Would you like to make another MPH calculation(Y/N)?").upper()
            while again not in ("Y", "YES", "N", "NO"):
                again = input("Error #2. Would you like to make another MPH calculation(Y/N)?").upper()
            if again in ("Y", "YES"):
                getNum()
            else:
                break
        except ValueError:
            print("Error #1. Can't contain any characters. Please enter again. ")
            continue

        else:
            break

getNum()






