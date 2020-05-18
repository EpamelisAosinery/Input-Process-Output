############################
# Author:   Epamelis Aosinery
# Date:     3/30/2020
# Desr:     Homework 4.3
############################

def getValue(house, percent, year):
    print("Current price is:", "${:,.2f}".format(house))
    year_value = (house * percent) + house
    for x in range(1, year + 1):
        print("Price will be " + "${:,.2f}".format(year_value), "in", x, "year")
        year_value = (year_value * percent) + year_value
        #year_value = year_value * (1 + percent) get teh same answer

while True:
    try:
        house = float(input("Please enter house price: "))
        percent = float(input("Please e enter percentage of increase (e.g. .02): "))
        year = int(input("Please enter  number of years for forecast: "))
    except ValueError:
        print("Cannot include any character, please enter number only.")
        continue
    else:
        break
getValue(house, percent, year)
