### 6. Python Program to Find the Union of two Lists


def getUnion(li1, li2):
    union = []

    for ele in li1:
        if ele not in union:
            union += [ele]

    for ele in li2:
        if ele not in union:
            union += [ele]
    return union


lst1 = [10, 20, 30, 40, 50, 10, 20]
lst2 = [40, 50, 60, 70, 80, 90, 10]


print(
    f"""
1st List : {lst1}
2nd List : {lst2}
-------------------------------------------------
Union List : {getUnion(lst1,lst2)}
-------------------------------------------------

"""
)