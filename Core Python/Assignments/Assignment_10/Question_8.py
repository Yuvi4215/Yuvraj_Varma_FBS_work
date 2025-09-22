### 8. Write a program to create a duplicate of an existing list. It should not point to same list.

def getDuplicateList(li):
    duplicate_li=[]
    for ele in li:
        duplicate_li+=[ele]
    return duplicate_li


li=[1,2,3,4,5,6,7]

print(f"Orginal list   :: {li}, and memory address ::{id(li)}")
duplicate_list=getDuplicateList(li)
print(f"Duplicate list :: {duplicate_list}, and memory address ::{id(duplicate_list)}")
print(f"Both List points to same object :: {li is duplicate_list}")