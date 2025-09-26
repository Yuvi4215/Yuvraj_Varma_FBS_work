### 5. Python Program to Count the Number of Vowels in a String


def getVowelCount(word):
    count = 0
    for char in word:
        if char in "aeiouAEIOU":
            print(char, end=" ")
            count += 1
    return count


strng = "A tester walks into a string… finds an 'a', replaces it with $, and calls it feature testing."

count = getVowelCount(strng)
print(f"The total count of vowels are :: {count}")
