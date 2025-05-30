# python update tuples
# change tuple values 
# once a tuple is created you cannot change its values tuple are uncahngeble  immutable as it also called 
# but ther ar a workaround you canvert this to list to change the element within it 

x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
print(y)

print(type(x))
print(type(y))
x=tuple(y)
print(type(x))


# add items
# since tuples are immutable they do not have a built in apped() method but other ways to add to ites to a tuple 
thituple=('apple',"banana","cherry")
y=list(thituple)
y.append('orange')
thituple=tuple(y)

print(type(thituple))

# add tuple to a tuple
thistuple =("apple","banana","cherry")
y=("orange",)
thistuple +=y
print(thistuple)


# remove items
# tuples are unchangeble 

thistuple=("apple","banana","cherry")
y=list(thistuple)
y.remove('apple')

thistuple=tuple(y)
print(thistuple)
print(type(thistuple))

# or you can change the tuple completely
# example del keyword cn delelet the tuple compleatyle

thistuple=("apple",'banana','cherry')
del thistuple
print(thistuple)

# this will raise an erro becasue the tuple no longeer4