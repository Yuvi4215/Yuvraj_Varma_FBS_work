###

def sortList(li, start, end, mid):
    print(start, end,mid)
    lhs = []
    rhs = []

    for ele in li[start : mid + 1]:
        lhs.append(ele)
    for ele in li[mid + 1 : end + 1]:
        rhs.append(ele)
    # lhs=li[start:mid+1]
    # rhs=li[mid+1:end+1]

    i, j, k = 0, 0, start

    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:
            li[k] = lhs[i]
            i += 1

        else:
            li[k] = rhs[j]
            j += 1
        k+=1

    while i < len(lhs):
        li[k] = lhs[i]
        i += 1
        k += 1
    while j < len(rhs):
        li[k] = lhs[j]
        j += 1
        k += 1


def mergeSort(li, start, end):
    if start < end:
        mid = (start + end) // 2

        mergeSort(li, start, mid)
        mergeSort(li, mid + 1, end)
        sortList(li, start, end, mid)


li = [90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6]
# print(f"Original List :: {li}")
start = 0
end = len(li) - 1
mergeSort(li, start, end)
# print(f"SOrted List :: {li}")
