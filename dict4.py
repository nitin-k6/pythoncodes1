#key names are the written in the left and the value define one which is written in

car={
    "model": "lambo",
    "year": 2001,
    "color": "white",
    "variant":"petrol"
}
'''for x in car:
    print(x) #Print all key names in the dictionary, one by one:
'''

for x in car:  
    print(car[x])   #Print all values in the dictionary, one by one:


'''
for x in car.values():
 print(x)     #print values
'''
'''
for x in car.keys():
    print(x)   #print key names
'''

for x, y in car.items():
        print(x,y)   #print both key names and values