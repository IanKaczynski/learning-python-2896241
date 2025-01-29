#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime 

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is ", today)

    # TODO: print out the date's individual components
    print("Date components: ", "Day:", today.day, "Month:",today.month, "Year",today.year)

    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is: ", today.weekday())
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    print("Which is a: ", days[today.weekday()]) # Indexes into the today's list using today.weekday()

    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is", today) # Prints the current date and time from the datetime class
    
    # TODO: Get the current time
    time = datetime.time(datetime.now())
    print("The current time is", time) # Prints the current time from the datetime class

 
if __name__ == "__main__":
    main()
  