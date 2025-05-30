# copy lists 
# use the copy() method 
# you can use the built in  list method copy() to copy a list 

thislist=['apple','banana','cherry']
mylist=thislist.copy()
print(mylist)

thislist=['apple','banana','mango']
mylist=list(thislist)
print(mylist)
print(thislist)

# using the slice Operators 
my_list1=thislist[:]
print(my_list1)
