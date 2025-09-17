### reverse the string

strng="qwerty uiopas dfgh jkl zxcvbnm"

# 1. slicing
str1= strng[::-1]
print(str1)



# 2. contatination  for loop
rev=""

for chars in strng:
    rev=chars+rev
print(rev)

# 3. reverse for loop

for chars in strng:
    print(chars, end="")
print("\n\n-----------------------------------------------")

for i in range(len(strng)-1,-1,-1):
    print(strng[i], end="")


count=0
for i in range(0, len(strng)):
    if(ord(strng[i])==32):
        count+=1
    
print("\n\n",count)