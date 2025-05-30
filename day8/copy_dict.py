# copy  dictionary
# you cannot copy a dictionary simple by typing 

# you cannot a dictionary 
# make a copy of dictinary

thisdict={
    "brand":"ford",
    "modle":"mustage",
    "year":1964
}

mydict=thisdict.copy()
print(mydict)


# make  a copy of a dictinary with the dict() function
thisdict={
    "brand": "ford",
    "modle":"mustage",
    "year":"mustage"
}

mydict=dict(thisdict)

print(mydict)