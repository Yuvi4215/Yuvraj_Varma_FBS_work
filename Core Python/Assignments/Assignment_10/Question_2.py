### Write a program to find maximum and minimum element in a list.


def getMaxMin(li):
    max_val = min_val = li[0]

    for ele in li[1:]:
        if max_val == None:
            if str(type(ele)) == "<class 'int'>" or str(type(ele)) == "<class 'float'>":
                max_val = min_val = ele
        if str(type(ele)) == "<class 'int'>" or str(type(ele)) == "<class 'float'>":
            if max_val < ele:
                max_val = ele
            elif min_val > ele:
                min_val = ele

    return max_val, min_val


li = [21, 78, 33, 65, 77, 41, 1, 23, -26, 888, 3]
high, low = getMaxMin(li)
print(f"Max Value :: {high}")
print(f"Min Value :: {low}")
# print(getMaxMin(li))
