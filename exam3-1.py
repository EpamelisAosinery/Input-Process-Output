############################
# Author:   Epamelis Aosinery
# Date:     4/19/2020
# Desr:     exam 3.1
############################


def numLoop(max, step):
    for x in range (0, max+1, step):
        print("Numnber:" , x )


while True:
    try:
        max = int(input("Enter max value: "))
        step = int(input("Enter step value: "))
        while max > 0 and step == 0 or max == 0 and step == 0:
            print("Error. Please try different number for the max and the step value.")
            max = int(input("Enter max value: "))
            step = int(input("Enter step value: "))

    except ValueError:
        print("Invalid. Can not contain any character and only integer number only.")
        continue
    else:
        break

numLoop(max, step)