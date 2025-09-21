### Write a program to reverse the list.

def reverseList(li, end):
    #creating new list and copying elements.
    copy1=[]
    for i in range(len(li)-1, -1,-1):
        copy1+=[li[i]]
    print(f"Copy List using rev loop: {copy1}")
   

    # new list by slicing
    copy2=li[len(li)-1::-1]
    print(f"Copy List using Slicing list :: {copy2}")

    # changeing original List
    for i in range(0, end + 1):
        # print(i)
        last = len(li) - 1 - i
        li[i], li[last] = li[last], li[i]
    print("Original Reversed List :: ", li)
    print("-------------------------------------------------------------------------------------")
    





li = [24, 15, 54, True, "string", 42, False, 3.45, 3.1415]
print("-------------------------------------------------------------------------------------")
print("Original List :: ", li)
print("-------------------------------------------------------------------------------------")
reverseList(li, len(li) // 2)
