############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 2.5
############################

def calchanges(change):
    print("Number of quaters" , change , "cents change")
    quarter = change // 25      # return float into int
    print("Quater:\t", quarter)
    change = change % 25         # modulus operator
    dimes = change //10
    print("Dimes:\t", dimes)
    change = change % 10
    nickels = change // 5
    print("Nickels:", nickels)
    change = change % 5
    penny = change // 1
    print("pennies:", penny)

change = int(input("Please enter amount of change between 0-99: "))
calchanges(change)