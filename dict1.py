thisdict={
    "brand": "audi",
    "color":"white",
    "year":2022
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict ))



thisdict={
    "brand": "audi",
    "color":"white",
    "year":2022,
    "year":2021
}
print(thisdict)

print(thisdict["year"])   #Duplicate value will overwrite existing value
# or
x=thisdict["color"]
print(x)
# or
x=thisdict.get("color")
print(x)





