############################
# Author:   Epamelis Aosinery
# Date:     May/8/2020
# Desr:     Exam 4.3
############################


def getDivisibleNum(prompt):
    while True:
        try:
            div_num = int(input(prompt))
        except ValueError:
            print("Invalid input. This is not an integer number.")
        else:
            break
    return div_num

def validiateIntRange(prompt):
    while True:
        try:
            max = int(input(prompt))
            total = 0

            for num in range(1, max):
                if (num % div_num == 0):
                    total += num
                    print(num, "divisible by", div_num)
                else:
                    pass

        except ValueError:
            print("Invalid input.")
            continue
        else:
            print("Total of numbers is:", total)
            break

# Main
choice = "Y"
valid = ("YES", "Y", "N", "NO")
yeslist = ("YES", "Y")
while choice in yeslist:
    div_num = getDivisibleNum("\nEnter a number to check divisibility:")
    max_num = validiateIntRange("\nEnter maximum number:")
    choice = input("Would you like to run the program again [Y to continue or N to quit]? ").upper()
    while choice not in valid:
        choice = input("Invalid input. Enter [Y] to continue and [N] to quit: ").upper()
print("\nGoodbye!")



