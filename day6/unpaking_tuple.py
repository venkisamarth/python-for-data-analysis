fruits=("apple","banana",'cherry')
print(type(fruits))
print(fruits)

fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

# using asteric  
# if the number of varaible is less that the number of values you can add an varaible ma,es and the values and the values be assigned to the varaible as a list 


fruits =("apple","banana","cherry","strawberry", 'easpberry')
(green ,yellow,*red)=fruits

print(green)
print(yellow)
print(red)

# add a list of values the tropic variable

fruits =('apple',"mango","papaya",'pinaple')
(green,*tropic,red)=fruits
print(green)
print(red)
print(tropic)






