a=23
b=66

if (a>b):
    print("a is greater than b")

elif  a==b:  #The elif keyword means "if the previous conditions were not true, then try this condition".
    print(" a and b are equal")

else:
    print("b is greater than a")

# Nested if
x=32
if x>10:
    print("Above ten")
    if x>20:
        print("Above twenty")
    else:
        print("Less than 10")