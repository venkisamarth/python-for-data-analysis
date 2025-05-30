# nested dictrianry 
# a dictionary can contain dictionaries this is called nested dictionaryes

# create a dictinary that contains three dictionares
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

print(myfamily["child1"]['name'])

for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y+":",obj[y])

