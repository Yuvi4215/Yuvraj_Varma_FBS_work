### 15. Python Program to find larger string without using built-in functions.
def stringLength(string_word):
    count = 0
    for _ in string_word:
        count += 1
    return count


def getLongerString(word1, word2):
    len1 = stringLength(word1)
    len2 = stringLength(word2)
    if len1 >= len2:
        return word1
    else:
        return word2

str1="A Sample String Used for Coding consist of !@#$%^&*() and 1234567890"
str2="A tester walks into a string… finds an 'a', replaces it with $, and calls it feature testing."

final_str=getLongerString(str1,str2)
print(f"Longer String is :: {final_str}")