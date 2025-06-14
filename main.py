#imutable data type
#immutable object cannot be modified after their correction
#integer, floating,strings,tuples,frozen set
a=6
first_location=id(a)
a=6
second_location=id(a)
print(first_location)
print(second_location)