############################
# Author:   Epamelis Aosinery
# Date:     4/22/2020
# Desr:     Homework 5.6
############################


def calcTuition(credits1,credits2,type):
     if type == 1:
        tuition = (credits1 * 101.5) + (credits2 * 200) + ((credits1 + credits2) *  23)+50+60
     elif type == 2:
        tuition = (credits1 * 177) + (credits2 * 265) + ((credits1 + credits2) * 23)+50+60
     elif type == 3:
        tuition = (credits1 * 257) + (credits2 * 350) + ((credits1 + credits2) * 23)+50+60
     return tuition


def getInfo():
    while True:
        try:
            print("\n1 - In District")
            print("2 - Out of District Student")
            print("3 - Out of State / International Student")
            type = int(input("\nChoose one of the above [1-3]:"))
            while type not in range(1, 4):
                print("Value not in range [1-3]. Try again. ")
                type = int(input("Choose one of the above [1-3]:"))

            credits1 = int(input("How many 100-200 level credits do you plan to register for [0-25]?"))
            credits2 = int(input("How many 300-400 level credits do you plan to register for [0-25]?"))
            while credits1 and credits2 not in range(0, 26):
                print("Either value of both credit levels is not in range [0-25]. Try again. \n")
                credits1 = int(input("How many 100-200 level credits do you plan to register for [0-25]?"))
                credits2 = int(input("How many 300-400 level credits do you plan to register for [0-25]?"))

        except ValueError:
            print("Invalid respond. This is not integer. Please re-enter correctly.")
            continue
        else:
            break
    return type, credits1, credits2


type, credits1, credits2 = getInfo()
tuition = calcTuition(credits1,credits2,type)

print ("Your tuition cost will be $%.2f" % tuition)
again = input("\nWould you like to calculate another tuition cost? (Y/N): ").upper()
while again not in ("Y","YES", "N", "NO"):
    again = input("Invalid valid response. Would you like to calculate another tuition cost? (Y/N): ").upper()

for x in again:
    if again in ("N", "NO"):
        break
else:
    type, credits1, credits2 = getInfo()

