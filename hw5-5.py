############################
# Author:   Epamelis Aosinery
# Date:     4/22/2020
# Desr:     Homework 5.5
############################

vehicles = []
vehicles.append(["2020","Chevy Silverado","Blue",3105])
vehicles.append(["2019","Ford Mustang","White",10302])
vehicles.append(["2018","Toyota RAV4","Gray",25132])
for x in range (len(vehicles)):
    print("Year:%-10s" % vehicles[x][0], "Make/Model%-20s" % vehicles[x][1], "Color:%-10s" % vehicles[x][2], "Miles: %-10s" % vehicles[x][3] )
