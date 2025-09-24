### 10. Write a program to print list after removing even numbers.


def removeEvenNums(li):
    lst = []

    for ele in li:
        if ele % 2 != 0:
            lst += [ele]
    return lst


li = [1, 2, 3, 4, 5, 77, 31, 69, 41, 11, 12, 13, 31, 74, 22, 17, 91]

print(f"Original List : {li}")
new_li = removeEvenNums(li)
print(f"List after removeing even numbers : {new_li}")
