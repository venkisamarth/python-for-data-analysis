
# add the element at end of the list 
thislist=['apple',"banana","cherry"]
thislist.append("orage")
print(thislist)

# isndert the element at the at a specific useing insert the method
thislist=['apple','banana','cherry']
thislist.insert(1,'range')
print(thislist)


# extend list  
# to append ellement from antoher list to the current list 
# add the element of tripcal to thislist 

thislist=["apple",'banana','cherrry']
tropical=['mango','pineappele','paparya']
thislist.extend(tropical)
print(thislist)
# add the element of the tuple also

thislist=["apple",'banana','cherry']
thistupe=('kiwi',"orange")
thislist.extend(thistupe)
thislist.extend(thislist)
print(thislist)


