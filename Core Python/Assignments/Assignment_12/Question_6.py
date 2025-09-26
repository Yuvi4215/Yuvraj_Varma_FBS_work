### 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen


def replaceSpaces(word):
    new_word = ""
    for char in word:
        if char == " ":
            new_word += "-"
        else:
            new_word += char
    return new_word


strng = input("Enter the String :: ")
print(f"Original string : {strng}")
str1 = replaceSpaces(strng)
print(f"""
--------------------------------------------------------------------------------------------
String after replacing ' ' with '-' : {str1}
--------------------------------------------------------------------------------------------
""")
