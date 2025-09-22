### 6. Write a program to remove duplicates from the list.

def removeDuplicate(li):
    unique=[]
    for ele in li:
        for val in unique:
            if ele==val:
                break
        else:
            unique+=[ele]

    print("Unique elements list :",unique)

li=[56,15,5,45,75,84,52,15,5,45,8,145,48,56,8]
print("Original List :",li)
removeDuplicate(li)


