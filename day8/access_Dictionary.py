thisdict={
    "brand":"Ford",
    "modle":"mustage",
    "year":1964
    }

x=thisdict['modle']
print(x)

# there is also a method called get() that will give you the same result

# get the value "model" key
x=thisdict.get("modle")
print(x)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

thisdict["year"]=2330
print(thisdict.values())

# add a new item to the dictioary
thisdict['color']="red"

print(thisdict.items())

print(thisdict.get("color"))


# add a new item  to the origainal and see that items list gets updated as well 
car={
    "brand":"Ford",
    "Model":"mustage",
    "year":1974
}

x=car.items()
print(x)# before the change

car['color']="red"

print(x)# after the change 


# check if hey exists  
# To determain if a specified key is present in a dictionary use the in keyword
# check if modle is present in the dictionary 

if "modle" in thisdict:
    print("yes" "modle is one of the keyw in the thiddic")
