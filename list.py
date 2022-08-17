thislist =["apple","banana", "cherry", "banana"]
thislist[0]="Mango"
print(thislist)
print(len(thislist)) #determines the length of the list
print(type(thislist))

#Using the list() constructor to make a List:
thislist=list(("Nitin", "Pokemon", "Jack"))
print(thislist)

#access list items
#Negaive indexing

thislist=["hi", "bye", "hello"]
print(thislist[-1]) #print last item


thislist=["pirates", "Johnny", "Tom", "Jerry"]
# if "pirates" in thislist:
#     print("Yes it is present")

print("pirates" in thislist)  #It will return True