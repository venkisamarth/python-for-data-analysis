# sort list aphpanumarica

# lsit objects hava a sort method that will sort the list phphanumarically as default 
thislist=['orange','mango','banana','kiwi','papaya']
thislist.sort()
print(thislist)

# sort the list numraically
thislist=[1,2,3,3,4,45]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

# sorting  Descending
thislist =['orange','mango','kiwi','pineapple','banana']
thislist.sort(reverse=True)
print(thislist)


# sorting the list abse on hwo close te numer is to 50 
def myfunc(n): 
    return abs(n-50)
thislist=[100,40,50,65,82]
thislist.sort(key=myfunc)
print(thislist)

# case insensitive sort 
thislist =['banana','orange','kiwi','cherry']
thislist.sort()
print(thislist)

# lukily we can use built as key function when sorting a list  
# so if you want a case inssensitive sort functio use str.lower as key function

# perform a case-insensitive sort of the list  

thislist =['banana','orange','kiwi','cherry']
thislist.sort(key=str.lower)
print(thislist)


# reversed order 
thislist=['banana','orange','kiwi','cherry']
thislist.reverse()
print(thislist)


