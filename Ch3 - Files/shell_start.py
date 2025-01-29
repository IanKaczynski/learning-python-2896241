#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil # shell utilities for file operations
from shutil import make_archive # shell utilities for file operations

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt") # get the full path to the file 

    #     # let's make a backup copy by appending "bak" to the name
    #     dst = src + ".bak" # append the .bak to the file name 
    #     shutil.copy(src, dst) # copy the file to the new file name
        
        # rename the original file
        os.rename("textfile.txt", "newfile.txt") # rename the file to newfile.txt
        
        # now put things into a ZIP archive
        # root_dir, tail = path.split(src) # get the path and the file name
        # shutil.make_archive("archive", "zip", root_dir) # create a ZIP file with the contents of the root_dir

        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")

      
if __name__ == "__main__":
    main()
