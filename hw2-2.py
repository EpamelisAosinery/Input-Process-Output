############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 2.2
############################

def calcChange(owed, paid):  #process and output
    customer_receives = paid - owed
    print("Customer receives $%.2f" % customer_receives, "change" + ".")

owed = float(input("Please enter amount owed: "))
paid = float(input("Please enter amount paid: "))
calcChange(owed, paid)
