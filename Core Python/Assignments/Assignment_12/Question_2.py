### 2. Python Program to Remove the nth Index Character from a Non-Empty String
def removeCharAtIndex(word, length, index):
    new_word = ""
    for i in range(0, length):
        if i != index:
            new_word += word[i]
    return new_word


strng = "A tester walks into a string… finds an 'a', replaces it with $, and calls it feature testing."
print("String : ", strng)
index = int(input("Enter the Index :: "))
new_str = removeCharAtIndex(strng, len(strng), index)
print(
    f"""
Old String : {strng}
New String : {new_str}

"""
)