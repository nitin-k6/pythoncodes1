# Python strings

# Check if "free" is present in the following text:
# If present it will print true
txt= "The best things in life are free"
print("free" in txt)

txt= "The best things in life are free"
print("expensive" in  txt)  #It will print false

# Check if NOT
# Check if "expensive" is NOT present in the following text:
t="Nitin is good"
print("bad" not in t)

# Use it in an if statement: 
# print only if "expensive" is NOT present:

tt="the price of the goods are cheap"
if "expensive" not in tt:
    print("no, expensive is not present")