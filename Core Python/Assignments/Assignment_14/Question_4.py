### 4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

num=16

lst=[10,9,8,7,6,5,6,7,8,9,10]
for index1 in range(0, len(lst)):
    for index2 in range(index1, len(lst)):
        if (lst[index1]+lst[index2])==num:
            print(lst[index1],"-----",lst[index2])