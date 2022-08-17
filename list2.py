txt=["apple", "Mango","Cherry", "grapes","banana"]
txt[2:4]=["strawberry", "orange"]
print(txt)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert item

thislist=["abc","def", "ijk","mnb","hgf"]
thislist.insert(2,"watermelon")
print(thislist)

