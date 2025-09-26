### 8. Python Program to Remove the Characters of Odd Index Values in a String


def removeOddIndexString(word):
    new_word = ""
    index = 0
    for char in word:
        if index % 2 == 0:
            new_word += char
        index += 1
    # print(index)
    return new_word


strng = "A tester walks into a string… finds an 'a', replaces it with $, and calls it feature testing"
print(f"Original string : {strng}")
str1 = removeOddIndexString(strng)
print(f"String with only even index chars : {str1}")