### 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String


def replaceChars(word):
    new_str = ""
    for char in word:
        if char == "a":
            new_str += "$"
        else:
            new_str += char
    return new_str


strng="A tester walks into a string… finds an 'a', replaces it with $, and calls it feature testing."

replace_char = replaceChars(strng)
print(
    f"""
Original String     : {strng}
Replace char String : {replace_char}

"""
)