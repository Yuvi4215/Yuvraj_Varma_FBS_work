### bubble and selection sort

def bubbleSort(li):
    li_length= len(li)

    for i in range(0, li_length):
        for j in range(i+1, li_length):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]


def selectionSort(li):
    li_len=len(li)
    for i in range(0,li_len):
        min_index=i
        for j in range(i+1,li_len):
            if li[min_index]>li[j]:
                min_index=j
        li[min_index],li[i]=li[i],li[min_index]


li=[9,8,7,6,5,4,3,2,1,0]
print(li)
# bubbleSort(li)
selectionSort(li)
print(li)