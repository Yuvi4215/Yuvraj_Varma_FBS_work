### 10. Write a program to remove all occurrences of a given element in the list.


def removeOccurrence(li, num):
    new_list = []

    for ele in li:
        if ele != num:
            new_list += [ele]
    return new_list


li = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
number = int(input("Enter the number : "))
print(f"Original List : {li}")
# print(id(li))
li = removeOccurrence(li, number)
# print(id(li))
print(f"After removing occurrence : {li}")
