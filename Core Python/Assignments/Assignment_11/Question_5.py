### 5. Python Program to Sort a List According to the Length of the Elements within the list.

def sortList(lst):
    for i in range(0, len(lst)):
        for j in range(i+1,len(lst)):
            if len(lst[i])>len(lst[j]):
                lst[i],lst[j]=lst[j],lst[i]
    



text_list = ["Thor", "IronMan", "Hulk", "SpiderMan", "AntMan", "Loki"]


print("Original list:", text_list)
sortList(text_list)
print("Sorted by length:", text_list)