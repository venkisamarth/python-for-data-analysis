# Remobe items to remove an item in a aset,use  the remov() or the discrab() methodt
thisset={'apple',"banana","herry"}
thisset.remove("banana")
print(thisset)

# example  
# remove banana by using the discrid() method

thisset ={'apple',"banana",'cherry'}
thisset.discard("banana")
print(thisset)

# you can also use the pop() method to rome an item but thise method will removea rando item , so you cannot be sure what items item that gets removed


# remove a random item by using the pop() method
thiset ={'apple',"banana",'cherry'}
x=thiset.pop()
print(x)
print(thiset)

# The clear() method empties the set  
thiset ={'apple',"banana",'cherry'}
thiset.clear()
print(thiset)

# example del keyword will delete the set completerly 
del thiset
print(thiset)