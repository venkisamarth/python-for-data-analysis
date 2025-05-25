# python -loops list 
# you can loop throught the list items by using a for loop 
new_list=[1,2,3,4,4,5]
print(new_list)

for x in new_list: 
    print(x)

# loops throught the index of the list 

for i in range(len(new_list)):
    print(new_list[i])

# the iteralbe created in the example above is [0,1,2]

# using a while loop  also using a while loop 

# example 

i=0
while i<len(new_list):
    print(new_list[i])
    i=i+1

