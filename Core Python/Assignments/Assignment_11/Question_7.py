### 7. Python Program to Find the Intersection of Two Lists


def getIntersectionList(lst1, lst2):
    intersection_list = []

    for ele in lst1:
        if ele in lst2 and ele not in intersection_list:
            intersection_list += [ele]
    return intersection_list


li1 = [10, 20, 30, 40, 50]
li2 = [40, 50, 60, 70, 80]


print(
    f"""
1st-List : {li1}
2nd-List : {li2}
---------------------------------------
Intersection-List : {getIntersectionList(li1,li2)}
---------------------------------------

"""
)