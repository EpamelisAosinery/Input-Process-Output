############################
# Author:   Hoa Ho
# Date:     1/17/2020
# Desr:     Homework 1-2
############################

owed = float(input("Please enter amount owed: "))
paid = float(input("Please enter amount paid: "))

customer_receives = (paid - owed)

print("Customer receives $%.2f" % customer_receives , "change" + ".")