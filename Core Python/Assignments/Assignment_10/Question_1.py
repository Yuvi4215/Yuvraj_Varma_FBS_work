### Write a program to find sum of all elements of list

li=[10,22,35,69,48,57,25,63,22,"a", 3.1415,85.52]

def getSum(li):
    sum=0

    for ele in li:
        if str(type(ele))=="<class 'int'>" or str(type(ele))=="<class 'float'>":
            sum+=ele

    return sum


