#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1," ",arg2)

# TODO: function that returns a value
def cube(x):
    return x*x*x

# TODO: function with default value for an argument
def power(num, x=1): # x=1 is the default value
    result = 1 # this is the default value
    for i in range(x):
        result = result * num
    return result 

# TODO: function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


# func1() # this will print the function
# print(func1()) # this will print the function and then None
# print(func1) # this will print the memory location of the function

# func2(10,20)
# print(func2(10,20)) # this will print the function and then None
# print(cube(3)) # this will print the cube of 3  
# print(cube) # this will print the memory location of the function   

# print(power(2)) # this will print the power of 2 to the power of 1
# print(power (2,3)) # this will print the power of 2 to the power of 3   

# print(power(x=3, num=2)) # this will print the power of 2 to the power of 3 
# this is because we are passing the values of the arguments in the function    
# in a different order but we are specifying the name of the arguments  

print(multi_add(4,5,10,4)) # this will print the sum of the numbers passed in the function  
# this is because we are passing the values of the arguments in the function    
# in a different order but we are specifying the name of the arguments  
# we are also passing multiple arguments in the function    
# this is done by using the *args in the function definition    
# this is called a variable number of arguments 
