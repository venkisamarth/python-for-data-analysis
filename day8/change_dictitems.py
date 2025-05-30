car={
    "barand":"Ford",
    "modle":"mustage",
    "year":1964
    }

car["year"]=2018
print(car["year"])

# update the "year" of the car by using the update() method:

car ={
    "brand":"Ford",
    "modle":"mustage",
    "year":1964
}

car.update({"year":2020})
print(car.values())

print(car.items())