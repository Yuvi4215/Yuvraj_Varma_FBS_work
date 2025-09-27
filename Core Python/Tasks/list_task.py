### WAP to remove dulicate elements in list

def removeDuplicate(li):
    n_li=[]
    for ele in li:
        if ele not in n_li:
            n_li+=[ele]
    return n_li

li=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
print(removeDuplicate(li))