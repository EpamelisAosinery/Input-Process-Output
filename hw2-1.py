############################
# Author:   Epamelis Aosinery
# Date:     1/17/2020
# Desr:     Homework 2.1
############################

"""There are many ways to find weekday, day of month, month, and year
Here are some examples of how to find them.
Learn more at https://www.w3schools.com/python/python_datetime.asp"""

#Use function datetime 
import datetime
x = datetime.datetime.now()                                   # from datetime find datetime and find now (day, date, month, year)
print("Today is:", x.strftime("%A"))                      # display the current day of the week. Ex: Today is: Friday
print("Today date:", x.strftime("%d"))                   # display the date
print("Today date is:", x.strftime("%B"))               # display the month name
print("Current year:", x.strftime("%Y"))                # display the year
print("Current year:", x.strftime("%c"))                 # display local version of date and time. Mon Dec 31 17:41:00 2018   
print("Current year:", x.strftime("%x"))                 # display local version of date.	12/31/18
print("Current year:", x.strftime("%X"))                 # display local version of time.	17:41:00
print("Current year:", x.strftime("%Z"))                 # display Timezone

# use function calendar and datetime to find how days of the current month and year
import calendar
import datetime
now = datetime.datetime.now()
print (calendar.monthrange (now.year, now.month)[1])    

# More cool ways to use functions date and calendar 
from datetime import date
import calendar
today = date.today()
print(today)                                                                              # This will print out the current year-month-date
# This is what it look like: 2020-05-18
print("Today is:", calendar.day_name[today.weekday()])       # This is another way to print out the current day

