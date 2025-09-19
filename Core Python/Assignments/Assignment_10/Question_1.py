### Write a program to find sum of all elements of list
def getSum(li):
    sum = 0

    for ele in li:
        if str(type(ele)) == "<class 'int'>" or str(type(ele)) == "<class 'float'>":
            sum += ele
    return sum


li = [10, 22,True, 35, 69, 48, 63, 22, "a", 3.1415, 85.52]
print(f"Sum of Elements :: {getSum(li)}")