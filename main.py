# Check if string starts with a substring
#we receive answer in true or false
text="Hellow world"
print(text.startswith("Hellow"))

# Check if string ends with a substring
#we receive answer in true or false
text="Hellow World"
print(text.endswith("Hellow"))

#Find the position of substring
print(text.find("world"))

#Count occurrences of a substring
print(text.find("o"))

#Check all character are alphanumeric
print(text.isalnum())

#Check all character are alphabetic
print(text.isalpha())

#Check all character are digit
print(text.isdigit())

#check is the string are titlecased
print(text.istitle())