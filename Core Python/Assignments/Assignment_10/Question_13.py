### 13 . Write a program to print list after removing even numbers.


def removeEvenNums(li):
    lst = []

    for ele in li:
        if ele % 2 != 0:
            lst += [ele]
    return lst


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(f"Original List : {li}")
new_li = removeEvenNums(li)
print(f"List after removeing even numbers : {new_li}")