# list comprehension
# list comprehension ofers a shorts sysntax when you watn to create a new list

fruits=['apple','banana','cherry','kiwi','mango']
newlist=[]
print(newlist) 

for x in fruits: 
    if "a" in x: 
        newlist.append(x)
print(newlist)



fruits=['apple','banana','cherry','kiwi','mango']
newlist=[x for x in fruits if 'a' in x]
print(newlist)

# with list comprehension you can do all that with only one line of code 
# the syntax 

# new list =respression
# newlist =[expression for item in iterable if condition ==True]

# newlist=[x for x in fruits if codiition ==True]


newlist=[x for x in fruits]
print(newlist)

# newlist=[expression for item in iterable if condition ==true]

# newlist =[x for x in fruits if x! ='apple']


newlist=[x for x in fruits]
print(x)

# you can use the range() function to create an iterable
newlist=[x for x in range(10)]
print(newlist)


# same example but with a condition 

newlist=[x for x in range(10) if x <5]
print(newlist)

new_list=[x*2 for x in newlist]
print(newlist)

newlist=['hello' for x in fruits]
print( x)

# newlist=[x uf x!='banana' else 'orange' for x in fruits]
# print(newlist)


