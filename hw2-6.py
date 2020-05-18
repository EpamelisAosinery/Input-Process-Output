############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 2.6
############################

import math
sentence = input("Enter a sentence: ")
number = float(input("Enter a number: "))
areaC = math.pi * math.pow(number, 2)

def factorial(num):
    return 1 if (num == 1 or num == 0) else num * factorial(num - 1)

num = number

print("The length of the sentence is", len(sentence), "characters long." )
word_count = len(sentence.split())
print("There are", str(word_count), "words in the sentence.")
print(sentence.upper())
print("The sentence in complete reverse is" , sentence[::-1])
print (number , "squared is" , int(number*number))
print("The factorial of", number , "is" , factorial(number))
print("A circle with a radius of", number , "would have the area of %.2f" % areaC +".")
