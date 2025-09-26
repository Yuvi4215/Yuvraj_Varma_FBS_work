### 14. Python Program to count the occurrences of ach word in a string.


def getLetterOccurrence(string):
    string = string + " "
    word, output = [], []
    text = ""

    for char in string:
        if char == " ":
            # print(text)
            word += [text]
            text = ""
        else:
            text += char

    for i in range(0, len(word)):
        count = 1
        if word[i] != "":
            for j in range(i + 1, len(word)):
                if word[i] == word[j]:
                    count += 1
                    word[j] = ""
            output += [word[i] + ":: Count :" + str(count)]
    return output


strng = "tester tester tester keeps saying bug bug bug"
print(getLetterOccurrence(strng))