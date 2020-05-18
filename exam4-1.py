############################
# Author:   Epamelis Aosinery
# Date:     May/8/2020
# Desr:     Exam 4.1
############################



while True:
    try:
        num_Exam = int(input("How many exam scores would you like to enter: "))
        if num_Exam <= 0:
            print("\nGoodbye!")
    except ValueError:
        print("Invalid input. This is not a number.")
        continue
    else:
        num_Exam += 0
        break

total = 0
for i in range(num_Exam):
    while True:
        try:
            score = float(input("Enter exam score:"))
            total += score
        except ValueError:
            print("Invalid input. Please only enter positive integer.")
        else:
            average = total / num_Exam
            break


print("Exam average: %.0f"% average)