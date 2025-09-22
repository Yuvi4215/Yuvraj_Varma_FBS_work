### 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.


def getOddEvenList(li):
    odd_list = []
    even_list = []

    for ele in li:
        if ele % 2 == 0:
            even_list += [ele]
        else:
            odd_list += [ele]
    return odd_list, even_list


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(f"Original List : {li}")
odd_li, even_li = getOddEvenList(li)
print(f"Odd List      : {odd_li}")
print(f"Even List     : {even_li}")