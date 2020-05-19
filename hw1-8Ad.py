############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 1-8 Advance
############################

watch1 = 659
iPhone1 = 14449
Laptop1 = 841.56
total = 0
TAX = 0.06

while True:
    item = input("Please enter the items you looking for:\t ").upper()
    if item == "WATCH":
        print("Apple watch series 4 has a price of:\t $%.2f " % watch1)
        total += watch1
    elif item == "IPHONE":
        print("iPhone XS MAX has a price of:\t\t\t $%.2f " % iPhone1)
        total += iPhone1
    elif item == "LAPTOP":
        print("Laptop has a price of:\t\t\t\t\t$%.2f " % Laptop1)
        total += Laptop1
    else:
        print("Error. Can't define the items you want. Please type again.")
    again = input("Would you like to make another purchase (y/n): ").upper()
    while again not in ("N", "NO", "YES", "Y"):
        again = input("Invalid.  Please enter Y or N: ").upper()
    if again in ("N", "NO"):
        break
sales_tax = total * TAX
total_price = sales_tax + total
print("-"*48)
print("Subtotal:\t\t\t\t\t\t\t\t$" + "{:,.2f}".format(total))
print("Sales Tax:\t\t\t\t\t\t\t\t$" + "{:,.2f}".format(sales_tax))
print("Your total are: \t\t\t\t\t\t$" + "{:,.2f}".format(total_price))