### 4. Remove all of the vowels in a string (take input from user)
strng=input("Enter the String : ")
# strng = "aa bb ee dd ii ff oo gg uu"
li = [ele for ele in strng if ele not in "aeiou"]
# print(li)
print(f"""Final String after removing vowels : 
{"".join(li)}""")