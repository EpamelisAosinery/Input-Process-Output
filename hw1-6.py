############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 1-6
############################

e1 = float(input("Enter your score for Exam #1:\t\t "))
e2 = float(input("Enter your score for Exam #2:\t\t "))
h1 = float(input("Enter your score for Homework #1:\t "))
h2 = float(input("Enter your score for Homework #2:\t "))

averagee = ((e1 + e2) / 2)*0.7
averageh = ((h1 + h2) / 2)*0.3
total = (averagee + averageh)

print("\t\t\t\t\t\t\t\t\t-----")

if total >=90:
    print("Your grade in this class is:\t\t" + "{:.0f}".format(total) + "%" +"(A)")
elif total >=80:
    print("Your grade in this class is:\t\t" + "{:.0f}".format(total) + "%" +"(B)")
elif total >= 70:
    print("Your grade in this class is:\t\t" + "{:.0f}".format(total) + "%" +"(C)")
elif total >= 60:
    print("Your grade in this class is:\t\t" + "{:.0f}".format(total) + "%" +"(D)")
else:
    print("Your grade in this class is:\t\t" + "{:.0f}".format(total) + "%" +"(E)")

# 90-100 %      A
# 80-89 %       B
# 70-79 %       C
# 60-69 %       D
# Below 60%     E