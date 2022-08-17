# format() combines numbers with string

from logging.handlers import BufferingHandler


age=21
txt="I am Nitin Kumar, I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity=35
itemno=233
price=230
txt="I want {} pieces of item {} for {} dollars"
print(txt.format(quantity,itemno,price))

#can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
#This concept is unclear