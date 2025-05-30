thisset={'apple',"banana",'cherry'}
thisset.add(('orange'))
print(thisset)

# add elements from tropical into thiset
thiset ={'apple',"banana","cherry"}
tropical ={'pineapple',"mango","papaya"}
thiset.update(tropical)
print(thiset)


# Add any itrable 
# The object in the update method does not habe to be a set it ca be any iterable object(tuples,list dictionaries etc)

# add element of a list  to st set  
thisset={'apple','banana','cherry'}
mylist=['kiwi',"orange"]

thiset.update(mylist)
print(thiset)

