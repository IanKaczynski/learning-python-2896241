# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
# myint = "abc"
# print(myint)

# to access a member of a sequence type, use []
# print(mylist[2])
# print(mytuple[1])

# # use slices to get parts of a sequence
# print(mylist[1:5]) 
# print(mylist[1:5:2]) # start, stop, step

# # you can use slices to reverse a sequence
# print(mylist[::-1]) #not specifing a start or stop, but only the step value which is telling python to go through the list in reverse order

# dictionaries are accessed via keys
#(dictionaries give you the item associated with the key)
# print(mydict["one"]) #this would print the value associated with the key "one" in the dictionary mydict

# ERROR: variables of different types cannot be combined
# print("string type" + 123) #this would give a TYPE error because you cannot concatenate a string and an integer
# print("string type" + str(123)) #this would work because you are converting the integer to a string before concatenating it with the string

# Global vs. local variables in functions
def someFunction():
    global mystr #this would make mystr a global variable and it can be accessed outside the function
    mystr = "def"
    print(mystr)

someFunction() #this would print the value of mystr in the function someFunction
print(mystr) #this would give an error because mystr is a local variable in the function someFunction and cannot be accessed outside the function

del mystr #this would delete the variable mystr
print(mystr) #this would give an error because mystr has been deleted and cannot be accessed