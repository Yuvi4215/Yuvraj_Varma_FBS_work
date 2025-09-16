###
li=[[10,20,40,22],[77,49,69,93,88,72]]
# for row in li:
#     for ele in row:
#         print(ele, end=" ")
#     print()

# ### Research on- how to itrate indivisual elements from following list
li2=[69,[11,21],[10,20],40,22,[77],49,69,[93,88,72]]

for i in li2:
    if str(type(i))=="<class 'int'>":
        print(i, end=" ")
    else:
        for j in i:
            print(j, end="-")

# print(type(1))

# ### research on deep copy and shallow copy
# li2=li.copy()   #it is shallow copy
# li[0][3]=998
# print("Original-List",li)
# print("copy-List",li2)


# li=[25,[14,8],96,[96,5,418,54],1221,[3,452]]
# stack=li
# print(stack)
# stack.pop()
# print(stack)