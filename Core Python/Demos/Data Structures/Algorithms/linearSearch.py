### search the element present or not in list

def searchEle(li,ele):
    for i in range(1,len(li)):
        if ele==li[i]:
            return i
    else:
        return None
    
li=[24,44,8,6,88,774,41,69,99]
ele=int(input("Enter the Number you want to search :: "))

result=searchEle(li, ele)

if result==None:
    print("Element not found!")
else:
    print(f"Element found at index : {result}")