### 1. Python Program to Put Even and Odd elements of a List into two Different Lists


def getOddEvenList(li):
    lst1, lst2 = [], []
    for ele in li:
        if ele % 2 == 0:
            lst1 += [ele]
        else:
            lst2 += [ele]
    return lst2, lst1


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(f"Original List : {li}")
odd, even = getOddEvenList(li)
print(
    f"""
Odd List  : {odd}
Even List : {even}
"""
)