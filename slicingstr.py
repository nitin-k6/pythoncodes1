from operator import index


a="Jackass"  #The first character has index 0.
print(a[2:4])  # It will print ck from index 2 to 3

b="Hello World"
print(b[4:8]) #Here index 5th is empty so in place of 5th index blank will be printed

c="Hello,World"
print(b[4:8])  # print commma as blank


d="jackeranthem"
print(d[:4])   #will print from index 0 to index 3

e="jokerpulkit"
print(e[4:])   # will print from pulkit 4 till end


#Negative indexing
# slice fron the end
f="hollester"
print(f[-7:-4])  #index 7 to index 5 from the end