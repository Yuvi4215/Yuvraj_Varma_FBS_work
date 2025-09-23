### 3. Python Program to Sort the List According to the Second Element in Sublist


def getsortedList(li):

    for i in range(0, len(li)):
        for j in range(i + 1, len(li)):
            if li[i][1] > li[j][1]:
                li[i], li[j] = li[j], li[i]


li = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [44, 4], [52, 3], [88, 2], [1111, 1]]
print(f"Original list(before sorting)              : {li}")
getsortedList(li)
print(f"List after Sorting based on second element : {li}")
