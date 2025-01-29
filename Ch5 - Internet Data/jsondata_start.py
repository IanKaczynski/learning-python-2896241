# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#
 #getting many ERRORS in this code so please refer to the finished code in the same folder!!! *****

import urllib.request
import json # import the JSON library 

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    
    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]: # check if the "title" key is in the metadata
        print(theJSON["metadata"]["title"]) # print the title of the feed 

    # output the number of events, plus the magnitude and each event name  
    count = theJSON["metadata"]["count"] # get the value associated with the key "count"
    print(str(count) + " events recorded") # print the number of events recorded

    # for each event, print the place where it occurred


    # print the events that only have a magnitude greater than 4


    # print only the events where at least 1 person reported feeling something

  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
  

if __name__ == "__main__":
    main()
