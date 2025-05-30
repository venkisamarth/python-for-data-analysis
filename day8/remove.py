# remove the dictioanry items  
# Removing items  
# example  
# there are several method  to remove items from a dictionary
thisdict={
    "brand":"Ford",
    "modle":"mustage",
    "year":1934
}

thisdict.pop("modle")
print(thisdict)

# the popitem() method removes the last inserted (in version before  3.7 a random item is removed insted)

thisdict={
    "brand":"Ford",
    "modle":"mustage",
    "year":1964
}

thisdict.popitem()
print(thisdict)

# the del keyword removes the itesm with the specified key name 
thidict ={
    "brand":"Ford",
    "modle":'mustage',
    "year":1964
}

print(thidict["modle"])
print(thidict)

del thidict['modle']
print(thidict)

# the delete keyword also usid to delete the all the dictioannry

# del thidict
print(thidict)

# this will cause an erro becaues "thisdict" no longer exits


# clear() method empties the dictionary

thidict={
    "brand":"Ford",
    "modle":"mustage",
    "year":1964
}

thidict.clear()
print(thidict)


