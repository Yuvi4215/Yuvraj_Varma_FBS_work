### reverse the string

strng="qwerty uiopasdfghjkl zxcvbnm"

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

