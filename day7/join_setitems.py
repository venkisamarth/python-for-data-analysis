# union and update 
# intersection()

#  the diffrence()

# union()
set1={"a","b","c"}
set2 ={1,2,3,4}

set3 ={1,2,3,4}

# you can use the | operators instad of the union() method and you will

# set1 ={'a',"b","c"}
# set2={1,2,3}
# set3=set|set2
# print(set3)


set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)


# use | to join the sets 
set1={'a',"b","c"}
set2={1,2,3,3,4}
set3=set1|set2
print(set3)

# join multiple sets 
set1={"a","b","c"}
set2={1,2,3,4}
set3={"johan","elena"}
set4={"apple","banana","cherry"}
myset=set.union(set2,set3,set4)
print(myset)

# use | to join two sets alsoe  
myset=set1|set2|set3|set3
print(myset)


# join a set and tuple in python 
# The union() method allows you to join a set with other data tyep in a ist or tuples

# the resul will be a set 
x={"a","b","c"}
y={1,2,3,4,4}
z=x.union(y)
print(z)

# update() 
# The update method insert all items from one set into another 
# the update changes the original set and does not returns a new set  
set1={"a","b","c"}
set2={1,2,3,4,4}
set1.update(set2)
print(set1)

# iintersection 
# keep only the duplicates  

set3=set.intersection(set2)
print(set3)

set3=set1&set2
print(set3)

# intersection_update() 
# the intersection_update() method will also keep only the duplciated but it will change the origrinal set insted of returning a new set

set1 ={"a","banana","cherry"}
set2={"google","microsoft","apple"}
set1.intersection_update(set2)
print(set1)

# The values Truw and 1 are considerd as same value the same goes gor false and 0
# diffrence()
set1={"apple","banana","cherry"}
set2={"google","microosoft","apple"}
set3=set1.difference(set2)
print(set3)


# you can use the - operators insted of the diffrence() method, and you will get the same result.
set1={'apple',"banana","apple"}
set2={'google',"microsoft","apple"}
set3 =set1-set2
print(set3)

# use the diffrence_update() method to keep the items that are not present in both sets

set1={"apple","banana",'cherrry'}
set2={'google',"microsoft","apple"}
set1.difference_update(set2)
print(set1)


# symatric_diffremce  
set1={"apple","banana","cherry"}
set2={"goole","microsoft","apple"}

set3=set1.symmetric_difference(set2)
print(set3)

set1={"apple","banan",'cherry'}
set2={"google","microsoft","apple"}
set3=set2^set2
print(set3)

# symetric_diffrece_update() 
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print(set1)