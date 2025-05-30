list1=['venkai','raju','ravi','anith']
list2=['sneha','savithri','palavi']

list1.append(list2)
print(list1)

for x in list2: 
    list1.append(x)
print(list1)

list2.clear()
print(list2)
list2=list1.copy()
print(list2)

list1.extend(list2)
print(list1)

print(list1.index('raju'))

list1.insert(3,"revi")
print(list1)

list1.pop()
print(list1)

list1.remove("savithri")
print(list1)