### 12. Python Program to count number of lowercase characters in a string.


def getLowerCaseCount(word):
    case_count = 0
    for char in word:
        if "a" <= char <= "z":
            case_count += 1
    return case_count


strng = "A Tester Walks Into A String… Finds An 'A', Replaces It With $, And Calls It Feature Testing."
# print(strng.title())
print(f"String : {strng}")
count = getLowerCaseCount(strng)
print(
    f"""
----------------------------------------
Lower case char count : {count}
----------------------------------------
"""
)