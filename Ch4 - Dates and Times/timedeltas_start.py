#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta # timedelta is a class in the datetime module that represents a duration of time rather than a specific moment in time


# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1)) # 365 days, 5 hours, 1 minute

# TODO: print today's date
now = datetime.now() # current date and time
print("today is:", now)

# TODO: print today's date one year from now
print("one year from now it will be:", now + timedelta(days=365))

# TODO: create a timedelta that uses more than one argument
print("In two weeks and 3 days it will be:", now + timedelta(weeks=2, days=3)) # 2 weeks and 3 days from now 

# TODO: calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1) # 1 week ago
s = t.strftime("%A %B %d, %Y") # format the date as a string
print("One week ago it was:", s)

### How many days until April Fools' Day?
today = date.today() # get the current date
afd = date(today.year, 4, 1) # get April Fool's Day for the current year
# if April Fool's Day has already gone for this year, use the replace() function to get the date for next year
if afd < today:
    print("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year+1)
# Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print("It's just", time_to_afd.days, "days until April Fool's Day")


# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# TODO: Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print ("It's just", time_to_afd.days, "days until next April Fools' Day!")
