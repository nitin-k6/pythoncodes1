list1= ["css","javacript","html"]
list2= ["node.js", "mysql", "express.js"]
list =list1 + list2
print(list) #By using + operator

list1= ["css","javacript","html"]
list2= ["node.js", "mysql", "express.js"]
for x in list2:
     list1.append(list2)
     print(list1) #appends one by one

list2= ["node.js", "mysql", "express.js"]
# print(list2.clear())  #clears the list
print(list2.count("node.js"))

list2= ["node.js", "mysql", "express.js"]
print(list2.index("node.js"))
