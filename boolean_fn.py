#Print "YES!" if the function returns True, otherwise print "NO!":
from operator import truediv


def myFunction():
    return True

if myFunction():
        print("Yes")
else:
        print("No")

    #Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
#To check if it is integer or not
x=36
print(isinstance(x,int))

#we can create functions that return boolean values

def myfunction2():
    return True

print(myfunction2())

