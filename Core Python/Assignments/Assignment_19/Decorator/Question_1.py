### 1. Develop a memoization decorator that caches the results of function calls and returns the cached
#      result when the same inputs occur again. This can greatly improve the performance of recursive or
#      computationally intensive functions.


def myDecorator(fun):
    def wrapper(word1, word2):
        return fun(word1, word2)

    return wrapper


@myDecorator
def isAnagram(word1, word2):
    if len(word1)==len(word2):
        di = {}
        for char1, char2 in zip(word1, word2):
            if char1 in di:
                di[char1] = di[char1] + 1
            else:
                di[char1] = 1

            if char2 in di:
                di[char2] = di[char2] - 1
            else:
                di[char2] = -1
        # print(di)
        for val in di.values():
            if val != 0:
                return False
        else:
            return True
    else:
        return False
    


str1 = input("Enter First String : ")
str2 = input("Enter First String : ")
# print(isAnagram(str1, str2))
if isAnagram(str1, str2):
    print(f"{str1} and {str2} are : 'Anagram'")
else:
    print(f"{str1} and {str2} are : 'Not Anagram'")