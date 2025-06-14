#Mutable data type
#List,Dictionary,sets
l=[1,2,3,4]
first_location=id(l)
print(first_location)
l[0]=4
second_location=id(l)
print(second_location)