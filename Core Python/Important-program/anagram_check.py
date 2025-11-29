def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}

    # manual character frequency
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    print(freq1)
    print(freq2)
    return freq1 == freq2

s1 = input("String 1: ")
s2 = input("String 2: ")

print("Anagram" if is_anagram(s1, s2) else "Not Anagram")
