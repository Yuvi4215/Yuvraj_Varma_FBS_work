### Write a program to find the second largest element in the list.


def getSecondMax(li):
    max_val = second_max = None

    for ele in li:
        if max_val == None:
            if str(type(ele)) == "<class 'int'>" or str(type(ele)) == "<class 'float'>":
                max_val = second_max = ele
        else:
            if str(type(ele)) == "<class 'int'>" or str(type(ele)) == "<class 'float'>":
                if max_val < ele:
                    second_max, max_val = max_val, ele
                elif second_max < ele:
                    second_max = ele
    return max_val, second_max


li = ["a", 10, True, 22, 35, 84.52, 48, 63, 22, "a", 3.1415, 85.52]
high, second_high = getSecondMax(li)
print(f"Highest value is :: {high}")
print(f"Second High value is :: {second_high}")
# print(getSecondMax(li))
