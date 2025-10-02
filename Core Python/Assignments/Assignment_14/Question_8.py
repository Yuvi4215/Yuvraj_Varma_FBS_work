### 8. Write a Python program to find all the anagrams and group them together from a given list of strings.

def grouptheAnagrams(words):
    groups = {}
    for word in words:
        signature = "".join(sorted(word))
        if signature in groups:
            groups[signature].append(word)
        else:
            groups[signature] = [word]
    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Anagram groups:", grouptheAnagrams(words))