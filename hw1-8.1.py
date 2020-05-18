############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 1-8.2
############################

TAX = 0.06

item1 = float(input("Please enter the price for item 1:\t "))
item2 = float(input("Please enter the price for item 2:\t "))
item3 = float(input("Please enter the price for item 3:\t "))

subtotal = item1 + item2 + item3
sales_tax = subtotal * TAX
total = subtotal + sales_tax
print("-"*41)
print("Subtotal:\t\t\t\t\t\t\t$" + "{:,.2f}".format(subtotal))
print("Sales Tax:\t\t\t\t\t\t\t$" + "{:,.2f}".format(sales_tax))
print("The total are:\t\t\t\t\t\t$" + "{:,.2f}".format(total))
