set1={"RAm", "Shyam", "Hari", "Gopal"}
set2= {"Gopal", "krishna", "MOhan","Hari"}
set3=set1.union(set2)
print("After Joining the two sets:\n",set3)

print("Keep Only Duplicates:")
set4=set1.intersection(set2)
print(set4)

print("Keep all But Not Duplicate:")
set5=set1.symmetric_difference(set2)
print(set5)
