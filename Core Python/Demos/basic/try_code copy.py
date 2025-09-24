text="asdfghjkl"
# print(enumerate(text))
# for index, char in enumerate(text):
#     print(index,char)
# print(text[::])
# d={1:"a", 2:"b",3:"c"}
# print(d)
# d.update({4:"d",5:"12"})
# print(d)

# s={1,2,3,4,"a","b",True,False}
# print(s)


A = {10, 20, 30,40}
B = {30, 40, 50,60}

# print("A|B",A | B)   # Union → {10, 20, 30, 40, 50}
# print("A&B",A & B)   # Intersection → {20, 30}
print("A-B",A - B)   # Difference → {10}
print(f"A:{A} and B:{B}")
# print("B-A",B - A)   # Difference → {40, 50}
# print("A^B",A ^ B)   # Symmetric Difference → {10, 40, 50}

s1=set([1,2,3,4,5,6,7,8,9])
print(s1)

s2={1,2,3,4,5,6,7,8,9}
print(s2)

