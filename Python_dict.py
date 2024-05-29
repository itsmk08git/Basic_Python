thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "Batch": 2000
}
print(thisdict)
thisdict2=thisdict

thisdict.popitem()

print(thisdict2)

#Nested Dictionary
print("\nNested Dictionary:")
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#Another Way of making dictionary
print("\nNested Dictionary:")
myfamily = {
"Child1" : {
  "name" : "Emil",
  "year" : 2004
},
"Child2" :{
  "name" : "Tobias",
  "year" : 2007
},
"Child3" : {
  "name" : "Mohan",
  "year" : 2011
},
}

print(myfamily["Child3"]["name"])
print(myfamily)
x=myfamily.items()
print(x)
print(list(x))
