
def selectionSort(li):
    for i in range(0, len(li)):
        min=i
        for j in range(i+1, len(li)):
            if li[min]>li[j]:
                min=j
        li[min],li[i]=li[i],li[min]



li=[13,12,11,10,9,8,7,6,5,4,3,2,1,0]
print("Original List : ",li)
selectionSort(li)
print("List after Sorting : ",li )