############################
# Author:   Epamelis Aosinery
# Date:     4/19/2020
# Desr:     exam 3.3
############################

import time
def getInfor():
    while True:
        try:
            a = ("\tMAIN MENU\n"
                 "----------------------------\n"
                 "1.Review your policy\n"
                 "2.File a claim\n"
                 "3.Exist\n")
            print(a)
            num = int( input("Please enter menu choice [1-3]: "))
            if num not in (1,2,3):
                print("\nInvalid menu choice. Please re-enter.\n")
                time.sleep(1)
                getInfor()
            if num == 1:
                input("\nReview policy stub.\n"
                      "\n[Enter to continue]")
                getInfor()
            elif num == 2:
                input("\nReview file stub.\n"
                      "\n[Enter to continue]")
                getInfor()
            else:
                print("\nGoodbye")

        except ValueError:
            print("\nInvalid menu Choice. Please re-enter [1-3].\n")
            time.sleep(1)
            continue
        else:
            break
getInfor()