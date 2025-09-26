### 7. Python Program to Calculate the Length of a String Without Using a Library Function


def calculateLength(word):
    count = 0
    for _ in word:
        count += 1
    return count

    # if len(word)%2!=0:
    #     count=1

    # for numbs in word[0:(len(word)//2)]:
    #     count+=2
    # return count


strng = "A tester walks into a string… finds an 'a', replaces it with $, and calls it feature testing"
print(f"String : {strng}")
length = calculateLength(strng)
print(f"The length of String : {length}")