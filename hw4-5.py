############################
# Author:   Epamelis Aosinery
# Date:     4/3/2020
# Desr:     Homework 4.5
############################

def diagnosePower():
    input("\nDiagnose PC Power. This is stub. Press [Enter] to continue." + "\n")
    getInfor()

def diagnoseNetwork():
    input("\nDiagnose Network Problem. This is stub. Press [Enter] to continue." + "\n")
    getInfor()

def getInfor():
    while True:
        try:
            a = ("METOPOLITIAN MEDICAL CENTER \n"
                 " IT Services HelpDesk\n"
                 "  Diagnostic Utility\n"
                 "----------------------------\n"
                 "1.Diagnose PC Power Problem\n"
                 "2.Diagnose Network Problem\n"
                 "3.Exist\n")
            print(a)
            num = int( input("What would you like to do? "))
            if num not in (1,2,3):
                print("\nNot Valid Choice. Please Try again (1-3).\n")
                getInfor()
            elif num == 1:
                diagnosePower()
            elif num == 2:
                diagnoseNetwork()
            elif num == 3:
                print("\nGoodbye")

        except ValueError:
            print("\nNot Valid Choice. Please Try again (1-3).\n")
            continue
        else:
            break
getInfor()


