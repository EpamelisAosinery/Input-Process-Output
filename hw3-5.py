############################
# Author:   Epamelis Aosinery
# Date:     2/27/2020
# Desr:     Homework 3.5
############################

yes_List = ("YES", "Y")
no_List = ("NO", "N")
yesno_list = ("YES", "Y", "NO", "N")
diagnosis = input("Is tooth tender to percussion?(Y/N) ").upper()
while diagnosis not in yesno_list:
        diagnosis = input("Is tooth tender to percussion?(Y/N) ").upper()
while diagnosis in yes_List:
        step2 = input("Is there swelling?(Y/N) ").upper()
        while step2 not in yesno_list:
                step2 = input("Is there swelling?(Y/N) ").upper()
        if step2 in yes_List:
                print("Diagnosis: Acute apical abscess.")
        else:
                print("Diagnosis: Symptomatic apical periodontitis.")
        break
else:
        step2 = input("Widened PDL or periapical radiolucency?(Y/N) ").upper()
        while step2 not in yesno_list:
                step2 = input("Widened PDL or periapical radiolucency?(Y/N) ").upper()
        if step2 in no_List:
                print("Diagnosis: Normal.")
        else:
                step3 = input("Is the tooth necrotic?(Y/N) ").upper()
                while step3 not in yesno_list:
                        step3 = input("Is the tooth necrotic?(Y/N) ").upper()
                if step3 in no_List:
                        print("Diagnosis: Lesion of non endodontic origin.")
                else:
                        step4 = input("Sirius tract present?(Y/N) ").upper()
                        while step4 not in yesno_list:
                                step4 = input("Sirius tract present?(Y/N) ").upper()
                        if step4 in no_List:
                                 print("Diagnosis: Chronic apical abscess.")
                        else:
                                print("Diagnosis: Asymptomatic apical periodontitis.")


