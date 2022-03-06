str=input("Enter any string")
char = str[0]
str1 = str.replace(char, '$')
newstr = char+str1[1:]
print(newstr)