# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.google.com") # open a connection to a URL using urllib
    print("result code: " + str(weburl.getcode())) # get the result code and print it
    data = weburl.read() # read the data from the URL and print it
    print(data)

if __name__ == "__main__":
    main()
