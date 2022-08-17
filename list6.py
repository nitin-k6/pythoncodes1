thislist=["nitin", "conor","khabib", "joker"]
thislist.sort()
print(thislist)

# print(thislist.sort())  --> It will print none


# Doing it numerically
thislist=[100,46,44,22,99]
thislist.sort()
print(thislist)

# Descending sort
thislist=[100,46,44,22,99]
thislist.sort(reverse= True)
print(thislist)


thislist=["nitin", "conor", "zebra", "giraffe"]
thislist.sort(reverse = True)
print(thislist)


#  sort function is case sensitive
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist=["Nitin", "conor", "zebra", "Giraffe"]
thislist.sort()
print(thislist) #Nitin is the first number that gets sorted first


# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist=["nitin", "conor", "zebra", "Giraffe"]
thislist.sort(key=str.lower)
print(thislist)

'''To reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()     #result would be cherry,orange,kiwi,cherry
print(thislist)

#customize sort not understood
