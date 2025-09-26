### 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
def getWordCount(string_word):
    string_word += " "
    di = {}
    word = ""
    for char in string_word:
        if char == " ":
            # print(word)
            if word in di:
                di[word] += 1
            else:
                di[word] = 1
            word = ""
        else:
            word += char
    return di


strng = "tester tester tester keeps saying bug bug bug"
d = getWordCount(strng)
print(
    f"""
Dictionary with words as key and count as value
--------------------------------------------------
{d}
--------------------------------------------------
"""
)