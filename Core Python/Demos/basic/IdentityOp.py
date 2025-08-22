x=10
y=20
z=10

li1=[1,2,4,3,5]
li2=[1,2,4,3,5]

### 1. is 
print(x is z)       #since int type is imutable only one object is created and x,z are pointing towords value 10
print(x is y)

print(li1 is li2)       #since list type is mutable two objects is created and li1,li2 are pointing towords two seperate objects
print(id(li1))
print(id(li2))

### 1. is not
print(x is not z)       
print(x is not y)