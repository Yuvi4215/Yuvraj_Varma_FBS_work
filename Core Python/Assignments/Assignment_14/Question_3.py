### 3. Write a Python program to find all the unique words and count the frequency of occurrence
# from a given list of strings. Use Python set data type.


def getWordsFrequency(lst):
    freq = {}
    unique = set()
    for strng in lst:
        word = ""
        for charr in strng + " ":
            if charr != " ":
                word += charr
            else:
                if word != "":
                    unique |= {word}
                    if word in freq:
                        freq[word] += 1
                    else:
                        freq[word] = 1
    return freq, unique


li = [
    "String",
    "integer",
    "char",
    "boolen",
    "String",
    "integer",
    "char",
    "boolen",
    "integer",
]
di_freq, set_unique = words, count = getWordsFrequency(li)
print(
    f"""
------------------------------------------------------------------------------
unique strings : {set_unique}
frequency      : {di_freq}   
------------------------------------------------------------------------------

"""
)