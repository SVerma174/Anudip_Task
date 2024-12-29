# Write a Python program to remove duplicate characters of a given string.

#Input = “String and String Function”

apl=input("Enter the string :")
i=0
ch=""

for x in apl:
    if apl.index(x)==i:
        ch+=x

    i +=1
print(ch)