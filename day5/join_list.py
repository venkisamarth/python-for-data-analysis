# join Two lists
# there are severl ways to join ,or concatenate two or more lists in python
# join two list:

list1=['a','b','c']
list2=[1,2,3,3]
list3=list1+list2
print(list3)

# another way to join the list are  
# append way
for x in list1: 
    list2.append(x)
print(list2)


# use the extend() method to add two list in python 
list1.extend(list2)
print(list1)

list1=[1,2,2,3,3,4,4]
list2=['raju','ravi','nayana','harsith']
list1.append(list2)
print(list1)

list1.clear()
print(list1)

list1.copy(list2)
print(list1)


