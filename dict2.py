'''thisdict={
    "model":"bmw",
    "color":"white",
    "year":2016,
    "owner":"joker"
}
print(thisdict)
print(len(thisdict))
print(thisdict["color"])
thisdict["color"] = "black"
print(thisdict)'''

car={
    "model":"bmw",
    "color":"white",
    "owner":"joker"
}
print(car)
car["year"]=2015  #year has been added to the car 
print(car)
print(car.items()) #The items() method will return each item in a dictionary, as tuples in a list.
if "model" in car:  #To determine if a specified key is present in a dictionary use the in keyword:
    print("Yes it is present")
    car.update({"color":"red"})
    print(car)