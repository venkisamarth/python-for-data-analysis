myset={"apple","banana","cherry"}
print(myset)

# set items
# set items are unorderd , unchangeble, and do not allow duplicate vlaues

# unorderd  
# unorderd mean that the items in a set do not have a defind orderd
# set items can appear in a diffrent order very time you use them and cannot be refferd to by index or key.


# unchangeable 
# set items are unchangble meaning that we  cannot change the items after the set has been creadted

# Duplicated Not allowed
thisset={'apple',"banana","cherry","apple"}
print(thisset)


# True and 1 is cinsiderd the same ValueError
thisset={"apple","banana",'cherry',True,1,2}
print(thisset)

thisset={"apple","banana",'cherry',False,True,0}
print(thisset)


# get the lenght of a set
# To determain how many items a set has, use the len() function

# Get the number of items in a set 
thisset={"apple","banan","cherry"}
print(len(thisset))

# String, int and boolean data types
set1={"apple","bana","cherry"}
set2={1,5,6,4}
set3={True,False,False}

# a set can contain diffrent data types
# a set with strings , intergers and boolean values

set1 ={"abc",34,True,40,'male'}
print(type(set))

# what is the data type of a set 
myset ={"apple",'banana','cherry'}
print(type(myset))


# The is also possible to  use the set() constructor to make  a  set

thiset =set(("apple","banana","cherry"))
# round-brackets

print(thiset)





