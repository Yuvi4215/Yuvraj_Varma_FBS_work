### 2. Python Program to Merge Two Lists and Sort it


def mergeList(lst, start, end, mid):
    lhs = []
    rhs = []
    i, j, k = 0, 0, start

    for ele in lst[start : mid + 1]:
        lhs += [ele]

    for ele in lst[mid + 1 : end + 1]:
        rhs += [ele]

    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:
            lst[k] = lhs[i]
            i += 1
        else:
            lst[k] = rhs[j]
            j += 1
        k += 1

    while i < len(lhs):
        lst[k] = lhs[i]
        k += 1
        i += 1

    while j < len(rhs):
        lst[k] < rhs[j]
        k += 1
        j += 1


def sortList(lst, start, end):
    if start < end:
        mid = (start + end) // 2
        sortList(lst, start, mid)  # LHS
        sortList(lst, mid + 1, end)
        mergeList(lst, start, end, mid)


def mergeSortedList(li1, li2):
    merge_list = []
    sortList(li1, 0, len(li1))
    sortList(li2, 0, len(li2))
    i, j = 0, 0

    while i < len(li1) and j < len(li2):
        # if li1[i]==li2[j]:
        #     merge_list+=[li1[i]]
        #     i+=1
        #     j+=1
        if li1[i] < li2[j]:
            merge_list += [li1[i]]
            i += 1
        else:
            merge_list += [li2[j]]
            j += 1

    while i < len(li1):
        merge_list += [li1[i]]
        i += 1

    while j < len(li2):
        merge_list += [li2[j]]
        j += 1

    return merge_list


li1 = [22, 21, 1, 20, 3, 4, 16, 13, 10, 9, 8, 7, 20, 26, 45, 222, 2]
li2 = [40, 36, 5, 7, 4, 88, 23, 66, 27, 1]
li = mergeSortedList(li1, li2)
print(
    f"""
List-1 :: {li1}
List-2 :: {li2}
---------------------------------------------
Merged List : {li}

"""
)
