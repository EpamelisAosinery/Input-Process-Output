############################
# Author:   Epamelis Aosinery
# Date:     2/13/2020
# Desr:     Homework 3.1
############################

BLUE = "\033[1;34m"
RESET = "\033[0;0m"
def findCategory(wind_speed):
    if wind_speed >= 0 and wind_speed <= 74:
        print(BLUE + "There is below hurricane level wind speed." + RESET)
    elif wind_speed <= 95:
        print(BLUE + "This is a category 1 hurricane\n " + RESET +
              "Very dangerous winds will produce some damage: "
              "Well-constructed frame homes could have damage to roof,"
              " shingles, vinyl siding and gutters. Large branches of "
              "trees will snap and shallowly rooted trees may be toppled. "
              "Extensive damage to power lines and poles likely will result"
              " in power outages that could last a few to several days.")
    elif wind_speed <=110:
        print(BLUE + "This is a category 2 hurrican\n" + RESET +
              "Extremely dangerous winds will cause extensive damage:"
              " Well-constructed frame homes could sustain major roof and "
              "siding damage. Many shallowly rooted trees will be snapped or "
              "uprooted and block numerous roads. Near-total power loss is "
              "expected with outages that could last from several days to weeks.")
    elif wind_speed <= 129:
        print(BLUE + "This is a category 3 hurrican\n" + RESET +
              "Devastating damage will occur: Well-built framed "
              "homes may incur major damage or removal of roof decking"
              " and gable ends. Many trees will be snapped or uprooted, "
              "blocking numerous roads. Electricity and water will be unavailable"
              "for several days to weeks after the storm passes.")
    elif wind_speed <= 156:
        print(BLUE + "This is a category 4 hurrican\n" + RESET +
              "Catastrophic damage will occur: Well-built framed"
              " homes can sustain severe damage with loss of most "
              "of the roof structure and/or some exterior walls."
              " Most trees will be snapped or uprooted and power poles "
              "downed. Fallen trees and power poles will isolate residential areas."
              " Power outages will last weeks to possibly months. Most of the area"
              " will be uninhabitable for weeks or months.")
    else:
        print(BLUE + "This is a category 5 hurrican\n" + RESET +
              "Catastrophic damage will occur: A high percentage of framed homes will be destroyed, with total roof failure and wall collapse. Fallen trees and power poles will isolate residential areas. Power outages will last for weeks to possibly months. Most of the area will be uninhabitable for weeks or months.")

wind_speed = int(input("Please enter sustained wind speed: "))
findCategory(wind_speed)