from stat import FILE_ATTRIBUTE_SPARSE_FILE


print("Hi")
print("Hello")

# Asssining a string value to the variable

a="I am Nitin"
print(a)


b=''' The Ultimate Fighting Championship (UFC) is an American mixed martial arts (MMA) promotion company based in Las Vegas, Nevada. 
It is owned and operated by Zuffa, LLC, a wholly owned subsidiary of Endeavor Group Holdings.
 It is the largest MMA promotion company in the world as of 2011.
  It produces events worldwide that showcase 12 weight divisions (eight men's and four women's) and abides by the Unified Rules of Mixed Martial Arts.
   As of 2022, it had held over 600 events. Dana White has been its president since 2001. Under White's stewardship, it has grown into a global multi-billion-dollar enterprise.'''
print(b)

# Python strings --> Python does not have character data type
# Strings in python are ararys of bytes representing unicode characters
# First character has position 0

a="Hello world"
print(a[1])
print(a[0])



# looping through string
#  Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
   print(x)

