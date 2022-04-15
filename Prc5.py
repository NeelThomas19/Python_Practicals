str=input()
str1=""
for i in str:
    if (i.isupper()):
        str1=str1+i.lower()
    else:
        str1=str1+i.upper()

print(str1)    