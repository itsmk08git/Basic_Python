#Tuples

#Adding Items in tuples
print("Initial Tuple")
thistuple = ("Mohan", "Ram", "Krishna", "Gopal")
newlist = list(thistuple)
print(newlist)
newlist.append("Govinda")
thistuple = tuple(newlist)
print("\nAfter Adding Items in the tuples:")
print(thistuple)

#Removing Items form the Tupels
newlist2 =list(thistuple)
del newlist2[1]
thistuple =tuple(newlist2)
print("After Deleting Item form tuple:")
print(thistuple)

fruits = ("apple", "banana", "cherry")
newlist3=list(fruits)
newlist3=newlist3*3
print(newlist3)
print(type(newlist))
mytuple = fruits * 2
fruits.count()

print(mytuple)