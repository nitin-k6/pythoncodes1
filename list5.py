#looping through the list
#loop through the list items by using a for loop:
thislist=["Banana","Mango", "Watermelon", "cherry"]
for x in thislist:
    print(x)

#loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
thislist=["banana", "mango", "apple", "watermelon"]
for i in range(len(thislist)):
 print(thislist[i])

'''You can loop through the list items by using a while loop.
 Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
Remember to increase the index by 1 after each iteration.'''

thislist=["orange", "apple", "mango", "cherry"]
i=0
while i< len(thislist):
    print(thislist[i])
    i=i+1

# List Comprehension offers the shortest syntax for looping through lists:

thislist=["nitin", "conor", "khabib"]
[print(x) for x in thislist]