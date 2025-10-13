### 3. A list contains sublist with Emp information as follows :
#       Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
#       [210,”Tannu”,14000],[320,”Suresh”,35000]]
#       Write a program to sort the list based on salary.


def selectionSort(li):

    for i in range(0, len(li)):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[min_index][2] > li[j][2]:
                min_index = j
        li[min_index], li[i] = li[i], li[min_index]
    # print(li)


li = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Tannu", 14000],
    [320, "Suresh", 35000],
]
print(f"List before Sorting                : {li}")
selectionSort(li)
print(f"List after Sorting based on salary : {li}")
