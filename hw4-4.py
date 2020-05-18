############################
# Author:   Epamelis Aosinery
# Date:     4/3/2020
# Desr:     Homework 4.4
############################

def getValue(columns, rows):
    for x in range(1, rows + 1):
        for y in range(1, columns + 1):
            print("Row", x, end="")
            print(" Column", y, end="" "\t\t" )

        print()

while True:
    try:
        columns = int(input("Enter how many columns you want your table to have: "))
        rows = int(input("Enter how many rows you want your table to have: "))
    except ValueError:
        print("Invalid. Can not contain any character and only integer number only.")
        continue
    else:
        break

getValue(columns, rows)