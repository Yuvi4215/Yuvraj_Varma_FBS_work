def sortAndMerge(li, start, mid, end):
    lhs = []
    rhs = []

    for ele in li[start : mid + 1]:
        lhs.append(ele)
    for ele in li[mid + 1 : end + 1]:
        rhs.append(ele)

    i, j, k = 0, 0, start

    while i < len(lhs) and j < len(rhs):
        if lhs[i] > rhs[j]:
            li[k] = rhs[j]
            j += 1
        else:
            li[k] = lhs[i]
            i += 1
        k += 1

    while i < len(lhs):
        li[k] = lhs[i]
        k += 1
        i += 1

    while j < len(rhs):
        li[k] = rhs[j]
        k += 1
        j += 1


def devide(li, start, end):
    if start < end:
        mid = (start + end) // 2

        devide(li, start, mid)
        devide(li, mid + 1, end)
        sortAndMerge(li, start, mid, end)


li = [78,515,654,4,3,2,1]
print(li)
start = 0
end = len(li) - 1
devide(li, start, end)
print(li)
