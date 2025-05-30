# access tuple items
thistuple=("apple","banana",'cherry')
print(thistuple[1])

# negative indexing
# negative indexing means statrt from the end 
# -1 refers to the last item  -2 refers to the second last item etc

thistuple=("apple","banana",'cherry')
print(thistuple[-1])


# range of indexes 
# you can specify a range of indexes by specifying where to start and where to  end the range

thistuple=("apple","banana","cherry","kiwi","melon","mango")
print(thistuple[2:5])

# example  
thistuple=("apple","banana","cherry","orange","kiwi","melon","manage")
print(thistuple[:4])

# by leaving out the end vlaue the range will got on to the end of the tuple 

thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:])

# Range of negative indexes
# specify negative if you want to statrt the search from the end of the tuple

thistuple =("apple","banana","cherry")
print(tuple[-3:-1])

# check if item exits or not in the tuple 
thistuple =("apple","banana","cherry")
if "apple" in thistuple: 
    print("yes, 'apple is in the fruits tuple" )


