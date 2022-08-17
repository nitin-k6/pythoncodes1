'''def myfunction():  #function is defined here
    print("Hello from a function")
myfunction() #Function is called'''

def myfunction(name):
    print(name + " Kumar")

myfunction("Nitin")
myfunction("Conor")
myfunction("Jack")

#From a function's perspective:
'''
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.'''

def myfunction(fname, lname):
    print(fname + " " +lname)
    
myfunction("Nitin", "Kumar")
myfunction("Conor" , "Mcgregor")
myfunction("Jack" , "Sparrow")

def my_function(*kids):
 print("The youngest child is" +kids[1])

my_function("Nitin","Sparrow","Eddy")

 #key=value syntax

def my_children(child1 , child2, child3):
 print("The youngest kid  is " +child2)

my_children(child1 ="Nitin", child2 ="Jack", child3 = "John")

#Kargs still to read