############################
# Author:   Epamelis Aosinery
# Date:     3/7/2020
# Desr:     Homework 3.ec3
############################

def caldollars():
    dollar = total // 1
    hundreds = dollar // 100

    dollar = total % 100
    fifties = dollar //50

    dollar = total % 50
    twenties = dollar // 20

    dollar = total % 20
    tens = dollar // 10

    dollar = total % 10
    fives = dollar // 5

    dollar = total % 5
    singles = dollar // 1
    print("Number of hundreds:........", hundreds)
    print("Number of 50s:........", fifties)
    print("Number of 20s:........", twenties)
    print("Number of tens:........", tens)
    print("Number of fives:........", fives)
    print("Number of singles:........", singles)

    return hundreds, fifties, twenties, tens, fives, singles


def calchanges():
    import math
    change = (math.floor(total*100)%100)
    quarter = change // 25      # //- return float into int. This will display the result before the decimal.
    change = change % 25         # %- modulus operator, this function will display the remainder.
    dimes = change //10
    change = change % 10
    nickels = change // 5
    change = change % 5
    penny = change // 1
    print("Number of quarter:........", quarter)
    print("Number of dimes:........", dimes)
    print("Number of nickels:........", nickels)
    print("Number of pennies:........", penny)
    return quarter, dimes, nickels, penny

def getChanges2():
    while True:
            try:
                total = float(input("Please enter the amount to make change for: $ "))
                if total > 0:
                    return total
                else:
                    print("The amount can not be negative. Please enter again.")
            except ValueError:
                print("Please only enter numbers. ")

total = getChanges2()
caldollars()
calchanges()






#def calDollar():
    #hundreds = 0
    #fifties = 0
    #twenties = 0
    #tens = 0
    #fives = 0
    #dollar = "{:,.0f}".format(total)
    #while dollar > "99":
    #   hundreds += 1
    #    dollar -= 100
    #
    #while dollar > "49":
    #   fifties += 1
    #   dollar -= 50
    #
    #while dollar > "19":
    #   twenties += 1
    #   dollar -= 20
    #
    #while dollar > "9":
    #   tens += 1
    #   dollar -= 10
    #
    #while dollar > "4":
    #   fives += 1
    #   dollar -=5
    #
    #print("Number of hundreds:......", hundreds )
    #print("Number of 50s:......", fifties)
    #print("Number of 20s:......", twenties)
    #print("Number of tens:......", tens)
    #print("Number of fives:......", fives)
