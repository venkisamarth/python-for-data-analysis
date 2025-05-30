car ={
    "brand":"Ford",
    "modle":"mustage",
    "year":1964
}

car["color"]="white"
print(car['color'])

# update() method will updatethe dictionary with the items from a   given argument. if the items does not exist the item will e add

# the argument must be a dictionary or an iterable or an iterable object with key: value


thisdict={"brand":"Ford","modle":"mustage","year":2023}
thisdict.update({"color":"red"})
print(thisdict)


thisdict["type"]="electric"
print(thisdict.items())




