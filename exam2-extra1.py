############################
# Author:   Epamelis Aosinery
# Date:     3/24/2020
# Desr:     Extra credit 1
############################

def getInformation():
    if get == "GA":
        print ("Georgia has 16 electoral votes.")
    elif get == "KY":
        print("Kentucky has 8 electoral votes.")
    elif get == "CA":
        print("California has 55 electoral votes.")
    elif get == "FL":
        print("Florida has 29 electoral votes.")
    elif get == "AR":
        print("Arkansas has 6 electoral votes.")
    else:
        print("New Jersey has 14 electoral votes.")

print("States:")
print("----------------------------------------")
print("Georgia (GA)\t\t\t", "Florida (FL)" )
print("Kentucky (KY)\t\t\t", "Arkansas (AR)")
print("California (CA)\t\t\t", "New Jersey (NJ)")

get = input("Please enter your state abbreviation from above: ").upper()
while get not in ("GA", "KY", "CA", "FL", "AR", "NJ"):
    get = input("Incorrect. Please enter your state abbreviation: ").upper()
getInformation()