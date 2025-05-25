# access items  in the list as shown in the below  methods


# accessing the element by using the index in the 
thislist=['apple','banana','cherry']
print(thislist[1])

# negative indexing 
# negative indexing mean start from th end  


list1=[1,2,3,3,4,4]
print(list1[-1])
print(list1[-2])


# range if indexes 
# you can specify a range of indexes by specifying whre to start and where to end in the list 
list1=["apple","banana","cherry","banana",'venki',"raju"]
print(list1[2:5])

# by leving returns the items from the begginning to but not including start 
print(thislist[:4])
print


# by leavinf out the end  value the range will fo on to the end of the list

thislist=['apple','banana','orange','kiwi',"melon"]
print(thislist[2:])

# range of negative indexing
thislist=[thislist[-4:-1]]


# check if apple is present in the list 
thislist=["apple","banana",'cherry']
if "apple" in thislist: 
    print("yes,'apple' is in the fruites list")
for x in thislist:
    print(x)

if "apple" in thislist: 
    print("yes present")

#   check if apple is present in the list
thislist =['apple',"banana","cherry"]
if "apple" in thislist:
    print("yes, 'apple' is in the fruites list")
      





