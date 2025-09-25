### List methods practic

li=[99,88,77,66,55,44,33,22,11,9,8,7,6,4,3,2,1]
print(li)
print("-----------------append---------------")
li.append(111)
print(li)
print("---------------------extend-----------")
li.extend((115,117,119))
print(li)
print("----------------insert(index,ele)----------------")
li.insert(10,999)
print(li)
print("--------------remove------------------")
li.remove(55)
print(li)
print("-------------pop-------------------")
li.pop()
print(li)
print("-------------pop(index)-------------------")
li.pop(5)
print(li)
print("-------------index(ele)-------------------")

print(li.index(7))
print("--------------count(ele)------------------")

print(li.count(99))
print("-------------sort-------------------")
li.sort()
print(li)
print("--------------reverse------------------")
li.reverse()
print(li)
print("-------------li.copy()-------------------")

print(li.copy())
print("-------------clear()-------------------")



li.clear()
print(li)
print("--------------------------------")
