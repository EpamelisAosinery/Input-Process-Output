############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 1-10
############################


fah = float(input("Please enter your temperature in Fahrenheit: "))
cel = round((fah-32) * (5/9), 2)
print ("The temperature", "{}".format(fah) + "\u00b0F" , "=", "{}".format(cel) + u"\u2103")
