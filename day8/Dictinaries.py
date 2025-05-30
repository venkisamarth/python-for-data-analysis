thisdict={
    'brand':"Ford",
    "model":'mustage',
    "year":1964
}
print(thisdict)

# dictionary are used to sotre  to the data valuew in key:value paris 
# a dictionary is a collectop which is orderd* ,changble and do not allow duplicated 

# creating the dictionary 
thisdict={
    "brand":"Ford",
    "model":"mustage",
    "year": 1964
}
print(thisdict)
# dictionary items 
print(thisdict["brand"])

# orderd or unorderd  
# as python version 3.7 dictionares are orders in python 3.6 and erlier  dictionares are inorderd


# changeble 
# dictionaries are changeble meaning that we can add or or remoe the items after the dictionary has been created  

# duplicatees not allowd  

thissidt={
    "brand":"Ford",
    "model":"mustage",
    "year":1964,
    "year":2020
}
print(thisdict)


# dictionary lenght 
print(len(thisdict))

# dictionary items datatype 
# the values in dictionary items can be onf nay data type 

# example 
thisdict={
    "brand":"ford",
    "electric": False,
    "year":1964,
    "color":["red","white","Blue"]

}
print(type(thisdict))

# The dict() constructor 
# it is also possible to use the dict() constructor to make a dictionary 

thisdict=dict(name="johan",age=36,country="norway")
print(thisdict)