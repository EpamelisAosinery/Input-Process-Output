########################################
# Author:   Epamelis Aosinery
# Date:     May/8/2020
# Desr:     Final Exam - Weather System
########################################

# Import time to delay the process time between the loops, so the user can see what they type and the error they made
import time

# Function 2. Converting the temperatures
def convertTempature():
    option = ("CELSIUS", "C", "FAHRENHEIT", "F" )
    cel = ("CELSIUS", "C")
    fah = ("FAHRENHEIT", "F")
    temp = input("What temperature would you like to convert into [Celsius(°C) or Fahrenheit(°F)]: ").upper()
    while temp not in option:
        temp = input("Invalid respond. Please type Celsius(°C) or Fahrenheit(°F): ").upper()

    while True:
        try:
            # u"\u2103" is °C simple | and "\u00b0" is a degree "°" simple
            # "{}".format() is automatically round 1 decimal place. Can't change even put "%.2f" % in the front
            if temp in fah:
                cel = float(input("Please enter your Celsius temperature: "))
                fah = (cel * 9/5) + 32
                print("\nThe temperature", "{}".format(cel) + u"\u2103", "=", "%.2f" % fah + "\u00b0F")
                time.sleep(2)
            else:
                fah = float(input("Please enter your Fahrenheit temperature: "))
                cel = (fah - 32) * (5 / 9)
                print("\nThe temperature", "{}".format(fah) + "\u00b0F", "=", "%.2f" % cel + u"\u2103")
                time.sleep(2)
        except ValueError:
            print("\nInvalid input. Please re-enter.")
            continue
        else:
            again()
            break

# Function 3. Calculating the temperature in Fahrenheit with wind speed
def calWindChill():
    while True:
        try:
            # Using the while function to repeat as many time as needed until get the right answer
            # If using the "IF" function, after the 2nd or 3rd tries, it causing a bug and let the input pass
            degree_num = float(input("Please enter Fahrenheit temperature (50°F or below): "))
            while degree_num >= 50:
                print("Temperature must be 50°F or below. Try again.")
                degree_num = float(input("Please enter Fahrenheit temperature (50°F or below): "))

            wind_speed = float(input("Please enter wind speed (mph; greater than 3):"))
            while wind_speed <= 3:
                print("Wind speed must be greater than 3. Try again. ")
                wind_speed = float(input("Please enter wind speed (mph; greater than 3):"))
        except ValueError:
            print("\nInvalid number. Try again\n")
            continue
        else:
            f2 = 35.74 + (0.6215 * degree_num) - (35.75 * (wind_speed ** 0.16)) + ((0.4275 * degree_num) * (degree_num ** 0.16))
            print("\n{}".format(degree_num) + "\u00b0F with a wind speed of", wind_speed, "= %.2f" % f2, "\u00b0F with wind chill")
            again()
            break

# Function 4. Option choice will pop up after user finish with Menu 1 or 2.
def again():
    choice = "Y"
    valid = ("YES", "Y", "N", "NO")
    yeslist = ("YES", "Y")

    choice = input("\nWould you like to run the program again [Y to continue or N to quit]? ").upper()
    while choice not in valid:
        choice = input("Invalid input. Enter [Y] to continue and [N] to quit: ").upper()
    if choice in yeslist:
        getInfor()
    else:
        print("\nGoodbye!")

# Function 1, prompt and validate user input
def getInfor():
    while True:
        try:
            a = ("\n\tWeather Menu\n"
                 "-----------------------------------------\n"
                 "1. Converting Temperature\n"
                 "2. Calculate Temperature with Wind Chill\n"
                 "3. Exit")

            print(a)
            num = int( input("\nWhat would you like to do? "))
            if num not in range(1, 4) :                                          # Create an if loop until user type exactly what I want
                print("\nInvalid menu choice. Please try again [1-3].\n" )
                time.sleep(0.8)
                getInfor()                                                       # After type in what I want move on
            elif num == 1:                                                       # If type 1, this will call the convertTempature() function
                print("\nConverting temperature in Celsius to Fahrenheit\n"
                      "--------------------------------------------------")
                convertTempature()
            elif num == 2:
                print("\nTemperature with Wind Chill Converter\n"
                      "--------------------------------------------------")
                calWindChill()                                                   # If the user type 2 this function wil be call
            else:                                                                # If user doesn't want to run anymore, type 3 break out the loop
                print("\nGoodbye!")
                break
        except ValueError:
            print("\nInvalid menu choice. Please Try again [1-3].\n")
            time.sleep(.8)
            continue
        else:
            break

# Main
getInfor()

