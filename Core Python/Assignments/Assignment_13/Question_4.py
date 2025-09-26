### 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).


def getDict(num):
    dict1 = {}
    for ele in range(1, num + 1):
        dict1[ele] = ele * ele
    return dict1


num = int(input("Enter the value of N : "))
d = getDict(num)
print(f"Generated Dictionary :: {d}")