#string repetition
name="ostad "
repeat=name *10
print(repeat)

#string concatenation
str1="Iam "
str2="Mehedi"

combine=str1+str2
print(combine)

combine="{} {} !".format(str1,str2)
print(combine)

combine="".join((str1 ,str2))+"!!"
print(combine)

combine="%s %s !!!"% (str1,str2)
print(combine)