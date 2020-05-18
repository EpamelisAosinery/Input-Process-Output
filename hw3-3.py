############################
# Author:   Epamelis Aosinery
# Date:     2/21/2020
# Desr:     Homework 3.3
############################

def securitypass(passw):
    valid = True # true if password valid
    import re
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if len(passw) <10:
        print("Password too short. Must be at least 10 characters long.")
        valid = False
    if passw.islower() or passw.isupper():
        print("Password must include both lower and upper case character.")
        valid = False
    if any(char.isdigit() for char in passw) == False:
        print("Password must include characters and at least 1 number.")
        valid = False
    if (string_check.search(passw) == None):
        print("Password must include at least 1 special character.")
        valid = False
    if (' ' in passw) == True:
            print("Password must not include space.")
            valid == False
    if valid == True:
         print("Thank you. Your password is valid.")


passw = input("Please enter your password: ")
securitypass(passw)


