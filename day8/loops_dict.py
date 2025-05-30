# Loop Through a dictionary 
# you can loop through a dictionary by using a for loop
# when looping through a dictionary by using a  for loop 
# when looping throught a dictionary the return value are the keys of the  dictionary but there are mehtod to retun the vvalues as well
# print all the name in the dictinary one by one 

thisdict={
    "brnad":"Ford",
    "color":"red",
    "year":1243,
    "type":"fulea",
"model":"mustage"
}
print(thisdict)
for x in thisdict:
    print(thisdict[x])


# you can also use the values() method to return values of a dictioanry

for x in thisdict.values():
    print(x)
for x in thisdict.items():
     print(x)

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x,y)


