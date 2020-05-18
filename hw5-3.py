############################
# Author:   Epamelis Aosinery
# Date:     4/22/2020
# Desr:     Homework 5.3
############################

employeenames = ["Jim Bailey", "Amy Dillon", "Ali Nassar", "Jose Martinez", "Lenard Phillips"]

print("List 1\n"
      "-------------------")
for name in employeenames:
    print("Name: ", name)


print("\nList 2\n"
      "-------------------")
for i in range (len(employeenames)):
    print("Name: ", employeenames[i] )


print("\nList 3\n"
      "-------------------")
i = 0
while i < len(employeenames):
    print("Name: ", employeenames[i])
    i += 1

print("\nList 4\n"
      "-------------------")
employeenames.append(input("Enter a new employee: "))
employeenames.sort()
for name in employeenames:
    print("Name: ", name)


