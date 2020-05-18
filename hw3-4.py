############################
# Author:   Epamelis Aosinery
# Date:     2/27/2020
# Desr:     Homework 3.4
############################

def menu():
    print("   MATH QUIZ ")
    print("===============")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication\n")
    operation = input("Please enter menu choice: ")
    while operation not in ("1", "2", "3"):
        operation = input("Please chose 1-3: ")
    return operation


def displayProblem(operation):
    import random
    num1 = random.randint(3,21)
    num2 = random.randint(3,21)
    if operation == "1":
        print(" ", num1)
        print("+", num2)
        print("  ----")
        result = num1 + num2
        return result

    elif operation == "2":
        print(" ", num1)
        print("-", num2)
        print("  ----")
        result = num1 - num2
        return result

    else:
        print(" ", num1)
        print("*", num2)
        print("  ----")
        result = num1 * num2
        return result

def checkAnswer(result):
    check = int(input("Please enter your answer: "))
    if check == result:
        print("You have the correct answer.")
    else:
        print("Incorrect. The answer is: ", result)


operation = menu()
result = displayProblem(operation)
checkAnswer(result)