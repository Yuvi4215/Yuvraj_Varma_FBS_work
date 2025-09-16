###
li=[[10,20,40,22],[77,49,69,93,88,72]]
# for row in li:
#     for ele in row:
#         print(ele, end=" ")
#     print()

### Research on- how to itrate indivisual elements from following list
# li2=[69,[11,21],[10,20,40,22],[77,49,69,93,88,72]]


### research on deep copy and shallow copy
li2=li.copy()   #it is shallow copy
li[0][3]=998
print("Original-List",li)
print("copy-List",li2)