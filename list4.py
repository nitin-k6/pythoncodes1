txt=["nitin", "gym", "banana","protein"]
txt.remove("nitin") #removes the specified item
print(txt)

txt1=["nitin", "gym", "banana","protein"]
txt1.pop(1) #removes the specified index
print(txt1)


txt2=["nitin", "gym", "banana","protein"]
txt2.pop() #removes the last item
print(txt2)



txt3=["nitin", "gym", "banana","protein"]
del txt3[2]  #removes the specified index
print(txt1)


thislist=["nitin", "joker" , "Gym"]
del thislist


'''The clear() method empties the list.
The list still remains, but it has no content.
'''

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
