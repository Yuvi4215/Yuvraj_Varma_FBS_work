### add each ele form two list

def addEleOfLists(li1,li2):
    index, end=0,0
    add_ele=[]
    if len(li1)>len(li2):
        end=len(li2)
        while(index<end):
            add_ele+=[li1[index]+li2[index]]
            index+=1
        end=len(li1)
        while(index<end):
            add_ele+=[li1[index]]
            index+=1

    else:
        end=len(li1)
        while(index<end):
            add_ele+=[li1[index]+li2[index]]
            index+=1
        end=len(li2)
        while(index<end):
            add_ele+=[li2[index]]
            index+=1
    return add_ele





li1=[1,2,3,4,5,6,7,8,9,10]
li2=[2,5,9,8,7,1]
ouput=[]


final=addEleOfLists(li1,li2)
print(final)






# for ele1, ele2 in zip(li1,li2):
#     ele=ele1+ele2
#     ouput+=[ele]
# print(ouput)



# ### Lambda Expession
# add = lambda a,b:a+b
# ls1 = [11, 12, 13, 14, 18]
# ls2 = [10, 20, 30, 40, 50,12,18]
# ans = map(add, ls1, ls2)
# print("Addition of list elements is : ", list(ans))




