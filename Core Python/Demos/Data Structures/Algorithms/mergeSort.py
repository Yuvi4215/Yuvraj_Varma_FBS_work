### Merge sort


def merge(li, start, end, mid):
    lhs = []
    rhs = []

    for ele in li[start : mid + 1]:  # LHS list
        lhs.append(ele)
    # print(lhs)
    for ele in li[mid + 1 :end+1]:
        rhs.append(ele)
    # print(lhs)
    i, j, k = 0, 0, start

    while i < len(lhs) and j < len(rhs):

        if lhs[i] < rhs[j]:
            li[k] = lhs[i]
            i += 1
            k += 1
        else:
            li[k] = rhs[j]
            j += 1
            k += 1

    while i < len(lhs):
        li[k] = lhs[i]
        i += 1
        k += 1

    while j < len(rhs):
        li[k] = rhs[j]
        j += 1
        k += 1


def divide(li, start, end):
    if start < end:
        mid = (start + end) // 2
        # print(mid)
        divide(li, start, mid)
        divide(li, mid + 1, end)
        merge(li, start, end, mid)


li = [90, 80, 70, 60, 50, 40, 30, 20, 10]
print("Original List :: ", li)
start = 0
end = len(li) - 1
divide(li, start, end)

print("Sorted List :: ", li)
