first ="venkatesh jayappa mariyappanaver"
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[4:9])
print(first[1:9])

# some mehtods returns boolean data 
print(first.startswith("d"))
print(first.endswith("r"))

print(first)

# Boolean data type
myvalue=True
x=bool(False)
print(type(x))
print(isinstance(myvalue,bool))


# numarica data types
price=100 
best_price= int(80)
print(type(price))
print(isinstance(best_price,int))
# float type 
gpa=3.28 
y=float(1.14)
print(type(gpa))

print(type(gpa))
# complex  type of data in python 
comp_value=5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers 
print(abs(gpa))
print(round(gpa))
print(round(gpa,1))
print(abs(gpa*-1))

import math

print(math.pi)
print(math.sqrt(23))
print(math.ceil(2))
print(math.floor(23))

# casting a stirng to a numbers 
zipcode ="10001"
zip_value=int(zipcode)
print(type(zip_value))

# Error if you attemtp to cas incorredt data 
zip_value =int("new Yourk")


