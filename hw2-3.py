############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 2.3
############################

def areaofCircle(radius):
    import math
    PI = math.pi
    area = PI * radius ** 2
    return area

radius = float(input("Enter the radius of the circle? "))
area = areaofCircle(radius)
print("The area of the circle is: %.2f" % area)
