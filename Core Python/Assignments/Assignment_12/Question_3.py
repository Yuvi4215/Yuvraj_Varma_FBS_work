## 3. Python Program to Detect if Two Strings are Anagrams
def checkStringAnagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in word1:
        if char not in word2:
            return False

    return True


strng1 = "listen"
strng2 = "silent"

if checkStringAnagram(strng1, strng2):
    print(f"String : '{strng1}' and '{strng2}' are :: 'ANAGRAM'")
else:
    print(f"String : '{strng1}' and '{strng2}' are :: 'NOT ANAGRAM'")
