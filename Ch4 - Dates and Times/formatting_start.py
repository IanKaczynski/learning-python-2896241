#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime # import the datetime class from the datetime module

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now() # get the current date and time

    
    #### Date Formatting #### using strftime function ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The Current year is: %Y")) # %Y - 4 digit year
    print(now.strftime("The Current year is: %a, %d %B, %Y")) # %a - weekday, %B - month, %d - day of month %Y - 4 digit year

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Local date and time: %c")) # %c - locale's date and time
    print(now.strftime("Local date: %x")) # %x - locale's date
    print(now.strftime("Local time: %X")) # %X - locale's time

    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p")) # %I - 12 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("24-hour time: %H:%M")) # %H - 24 Hour, %M - minute

if __name__ == "__main__":
    main()
