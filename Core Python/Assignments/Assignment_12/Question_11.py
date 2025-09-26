### 11. Python Program to replace every blank space with hyphen in a string.

def replaceSpaces(word):
    new_word = ""
    for char in word:
        if char == " ":
            new_word += "-"
        else:
            new_word += char
    return new_word


strng = "A tester walks into a string… finds an 'a', replaces it with $, and calls it feature testing."
print(f"Original string : {strng}")
str1 = replaceSpaces(strng)
print(f"""
--------------------------------------------------------------------------------------------
String after replacing ' ' with '-' : {str1}
--------------------------------------------------------------------------------------------
""")

