text= "Hello World"
print(text.upper())

text= "HELLO WORLD"
print(text.lower())

text= "hello world"
print(text.capitalize())

text= "hello world"
print(text.title())

text= "hello world"
print(text.swapcase())

#replace a substrings
text= "hello world"
print(text.replace("world", "Mehedi"))

text= "hello-world-with-python"
print(text.split("-"))

text= ['hello', 'world', 'with', 'python']
print ("-".join(text))

#strip whitespace from both ends
text=" hellow world "
print(text.strip())

#remove leading whitespace
print(text.lstrip())

#remove trailing whitespace
print(text.rstrip())