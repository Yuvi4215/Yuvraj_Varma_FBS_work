### 5. Write a Python program to find the longest common prefix of all strings. Use the Python set.


def longestCommonPrefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for i in range(len(prefix)):
        char_list = []
        for word in strings:
            if i < len(word):
                if word[i] not in char_list:
                    char_list.append(word[i])
            else:
                return prefix[:i]
        if len(char_list) > 1:
            return prefix[:i]
    return prefix


str_li = ["Abhishek", "Abhijit", "Abhinav"]
print("Longest prefix:", longestCommonPrefix(str_li))
