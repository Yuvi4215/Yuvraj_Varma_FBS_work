### max num

li=[1,2,5,54,87,0,22,888,95,77,12]
min=9999999 #taking max num as possible
max=0
for ele in li:
    if max<ele:
        max=ele
    if min>ele:
        min=ele

print("MAX :: ",max)
print("MIN :: " ,min)