############################
# Author:   Epamelis Aosinery
# Date:     May/8/2020
# Desr:     Exam 4.2
############################


dog_names = ['Zeus', 'Sammy', 'Pedro', 'Filo', 'Bandit']

print("\nDog 2:", dog_names[1])

print("\nAll dogs:")
for name in dog_names:
    print("\tDog:", name)

dog_names.append(input("\nPlease enter a new dog name:"))
dog_names.sort()
dog_count = len(dog_names)

print("\nAll", dog_count , "dogs: ")
for name in dog_names:
    print("\tDog:", name)

print("\nTotal number of dogs:", dog_count)