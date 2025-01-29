#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    # print(os.name)

    # # Check for item existence and type
    # print("Item exists: " + str(path.exists("textfile.txt")))
    # print("Item is a file: " + str(path.isfile("textfile.txt")))
    # print("Item is a directory: " + str(path.isdir("textfile.txt")))
    
    # # Work with file paths
    # print("Item's path: " + str(path.realpath("textfile.txt"))) # get the full path of the file
    # print("Item's path and name: " + str(path.split(path.realpath("textfile.txt")))) # split the path and the file name

    
    # Get the modification time
    # t = time.ctime(path.getmtime("textfile.txt")) # get the modification time of the file
    # print(t)
    # print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) # convert the time to a readable format
    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")) # get the current time and subtract the modification time
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")

  
if __name__ == "__main__":
    main()
