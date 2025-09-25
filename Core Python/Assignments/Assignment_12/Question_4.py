### 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged


def swapFirstLastChar(word):

    if len(word) < 2:
        return word
    else:
        new_word = word[len(word) - 1] + word[1 : len(word) - 1] + word[0]
        return new_word


strng = "Iron-Man"

new_str = swapFirstLastChar(strng)
print(f"original String : {strng}")
print(f"Replace chars : {new_str}")
