# python conditiona and of statments  

a=33
b=200
if b>a:
    print("b is greater that a ")

# indentation  
# python relies on indentation 

a=33
b=200
if b>a:
    print("b is greater that a")# you will get an erro

# elif  
# the elif keyword in python's way of saying if the previos constions were tru then try this conditon 
a=33
b=33 
if b >a: 
    print("b is greater than a")
elif a ==b: 
    print('a and b are equal')

# else 
# the else  keyword cateches anyting whcih is'nt caught the preceding 

a=200
b=33
if b >a:
    print("b is greater thatn a ")
elif a==b: 
    print("a and b are equal")
else: 
    print(" a is greater that b")
# In this example a 

a=200
b=33 
if b>a: 
    print("b is greater that a ")
else: 
    print("b is not greater that a")

# short hand if  
if a>b: print("a is greater that b")

# sort hand if else 
# if you have only one statment to execute one for if, and one for else , you can put it all on the same line

a=2 
b=303
print("a") if a>b else print("b")

# you can also  have multipe statment on the same line 
a=330
b=330
print("a") if a>b else print("=") if a==b else print("B")

a=200
b=33
c=500
if a>b and c>a:
    print("Bote conditions are True")


# or The keword is a logical operators and  is used to cobine conditional statments

# Test if a greater that b,or if a is greater that c 

a=200
b=33
c=500
if a>b or a>c:
    print("At least one of the condiions if True")

# The not keword is a logical operator and is used to revers the result of the conditional statement  
# Test if a is NOT greater thta b: 

a=33 
b=200
if not a>b: 
    print("a is Not greater than b")

# nested if  
x=41 
if x>10: 
    print("Above ten")
    if x>20: 
        print("and also above 20!")
    else: 
        print("but not above 20.")


# The pass statment
# if statments cnnot be empty, but uf you form some resone have an if statment with no content put in the  pass statment to avoid getting an error

a=33
b=200
if b>a: 
    pass