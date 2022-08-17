txt=["nitin","conor","khabib","mike"]
txt.append("adesyna") #To add an item to the end of the list, use the append() method:
print(txt)


#To append elements from another list to the current list, use the extend() method.
# txt=["nitin","conor","khabib","mike"]
# txt2=["mike","floyd","manny"]
# txt.extend(txt2)
# print(txt)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

tt=["nitin","conor","khabib","mike"]
tt2=("mike","floyd","manny")
tt.extend(tt2)
print(tt)


