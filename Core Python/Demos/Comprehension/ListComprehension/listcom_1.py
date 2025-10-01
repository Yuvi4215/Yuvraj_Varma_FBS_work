###
li = [ele for ele in range(1, 7)]
print(li)

li = [ele * ele for ele in range(1, 9)]
print(li)

li = [ele for ele in range(1, 21) if ele % 2 == 0]
print(li)

li = [ele for ele in range(1, 11) if ele % 2 == 0]
print(li)

li=[[ele for ele in range((i*10)+1,(i*10)+11)] for i in range(0,10)]
print(li)
