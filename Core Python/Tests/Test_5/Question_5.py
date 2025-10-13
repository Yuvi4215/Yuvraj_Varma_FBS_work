### 5. Python Program to Find the Union of two Lists without using set concept.

def unionOfList(li1,li2):
    union=[]
    for ele in li1:
        if not (ele in union):
            union.append(ele)
    for ele in li2:
        if not (ele in union):
            union.append(ele)
    return union

li1=[10,20,30,40,50,60,70]
li2=[40,50,60,70,80,90,100,110,120]
print(f"List-1 : {li1}")
print(f"List-2 : {li2}")
union=unionOfList(li1,li2)
print(f"Union of List-1 and List-2 : {union}")
